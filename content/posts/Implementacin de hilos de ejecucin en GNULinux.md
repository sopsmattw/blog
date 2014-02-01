Title: Implementación de hilos de ejecución en GNU/Linux
Date: 2007-01-25 19:01:52
Category: Spanish
Tags: threads, hilos
Author: frommelmak

Llevo muchísimo tiempo lidiando con el sistema de paquetes RPM de Red Hat y la verdad es que nunca antes me haba encontrado con nada parecido al problema con el que me encontré a principios de semana.

El problema se resume así: Trabajando en un sistema vía SSH (Putty), me di cuenta que al hacer `RPM -q <paquete>` me retornaba una versión de paquete distinta que si en ese mismo sistema lanzaba un `ssh rpm -q <paquete>` desde otra máquina. Dado que lo único que podía cambiar de uno a otro escenario eran las variables de entorno bajo las cuales se ejecutaba la orden, me puse a ver cual era la que originaba el problema. Tras unas cuantas pruebas vi que la culpable era una variable llamada `LD_ASSUME_KERNEL`.

Como no tenia ni idea de en que manera podía esto afectar al resultado de una *query* tan simple a la base de datos RPM, empecé a documentarme sobre qué demonios hacía esta variable. Tras un buen rato tirando del **HILO** di con la respuesta. 

El documento que viene a continuación intenta resumir todo lo que he aprendido a raíz de la dichosa variable.

Si lo preferís, podéis descargarlo en PDF desde [aquí](http://nomeriasdeti.no-ip.com/files/docs/IHEGL.pdf).



#Implementación de hilos de ejecución en sistemas GNU/Linux
##LinuxThreads vs Native POSIX Threads (NPTL)
23-Jan-2007
<frommelmak@gmail.com>


###Diferencias entre hilos de ejecución (threads) y procesos

A grandes rasgos, la principal diferencia entre un proceso y un *thread* es que en la mayoría de los sistemas operativos, un proceso es una entidad relativamente independiente que dispone de su propio espacio de direcciones, su propia información de estado y que utiliza los mecanismos de comunicación entre procesos que le proporciona el sistema operativo para comunicarse con otros procesos.

Por otro lado, un *thread* seria una entidad más reducida capaz de convivir junto a otros *threads* bajo el contexto de un único proceso, permitiendo compartir la información de estado, el área de memoria y/o los recursos asociados a ese proceso.

Así, un *thread* no sería más que la habilidad de un proceso o programa para dividirse en varios hilos de ejecución simultáneos o aparentemente simultáneos.

Desde el punto de vista del algoritmo de scheduling del kernel -que decide que proceso ha de pasar a la CPU en cada momento- el proceso seria la unidad más grande capaz de ser manejada por el scheduler, mientras que el hilo seria la unidad más pequea capaz de ser llevada a la CPU por el scheduler del kernel.


###Hilos de ejecución en GNU/Linux

Antes de la versión 2.6 del kernel Linux, no haba soporte real para manejar hilos a nivel de kernel. Las primeras versiones para el manejo de hilos en Linux (LinuxThreads) se implementaron en el área de usuario mediante llamadas a una función de sistema `clone()`, capaz de crear una copia de un proceso. Esta primera implementación además estaba muy lejos de ser compatible con los estándares POSIX de hilos de ejecución (POSIX threading standards).

Para mejorar el soporte de hilos en Linux, fueron necesarios retoques tanto a nivel de kernel (y su ABI) como a nivel de las libreras GNU C Library (Glibc) que implementaban el concepto de hilo.

Esto dio lugar a varios modelos/proyectos para la gestin de hilos, dependiendo de lo nuevo que fuera el sistema:
 
    
  * LinuxThreads (with fixed stack size) 
  * LinuxThreads (with floating stacks) 
  * NGPT (Next Generation POSIX Threads) liderado por IBM y abandonado 	por NPTL.
  * NPTL (Native POSIX Thread) Proyecto liderado por Red Hat y liberado	en 2003.
    
    
Al añadir nuevas posibilidades al trabajo con hilos en el kernel de linux, se inició una etapa de transición en la que algunas aplicaciones requerían un esquema de hilos moderno (NPTL), mientras que otras utilizaban otro más tradicional como LinuxThreads. Todo ello, teniendo el sistema que poder correr aplicaciones basadas en un modelo de hilos más o menos avanzado.

Como se ha comentado al inicio, los nuevos modelos de soporte de hilos requerían cambios también a nivel de kernel. As, las diferentes libreras dinámicas (DSO Dinamic Shared Objects/Shared Libraries), además de una librera de hilos concreta, requerirán de una versión del kernel con una interfaz capaz de trabajar con dicha librera. A esta interfaz se la conoce con el nombre de Application Binary Interface (ABI).

Una ABI define la interfaz de bajo nivel entre la Aplicación y el sistema operativo o kernel , mientras que una API define el interfaz entre el código fuente y las libreras. 

De la misma forma que una API permite que un código fuente sea compilado en cualquier sistema que soporte para dicha API, la ABI permite que un objeto binario pueda funcionar en un sistema con una ABI compatible.
    
Los DSO incluyen información relativa a la versión de ABI requerida, de manera que el enlazador o cargador dinámico (LD) de las Glibc (`ld.so/ld-linux.so`) sabe la versión ABI requerida por el DSO.

Las ABIs disponibles dependen de la versión del kernel que utilice el sistema, mientras que el modelo de hilos utilizado depende de las libreras de hilos (`libpthread.so`) disponibles. La decisión de qué libreras utilizar la toma el enlazador dinámico.

Así, la incursión de un nuevo modelo de hilos requería también de retoques en el enlazador dinámico de libreras, a fin de asegurar la compatibilidad total con las aplicaciones ya existentes, además de los ya mencionados cambios en el sistema (kernel y librera de implementación de hilos).

El enlazador dinámico (`ld-linux.so`) de DSOs (Dynamic Share Object .so) forma parte de las Glibc, y es capaz de ver los requerimientos en cuanto a kernel/ABI de un DSO y llamar a las librerías necesarias/compatibles en cada caso. En Red Hat 9, Fedora Core 1 y 2, estas libreras están en `/lib`, `/lib/i686` y `/lib/tls` en función de si implementan un sistema de hilos LinuxTread (fixed stacks), LinuxTread (floating stacks) o NPTL respectivamente.


###La variable `LD_ASSUME_KERNEL`

En los sistemas Red Hat Linux en los que conviven los diferentes acercamientos al modelo de hilos (LinuxThread y NPTL), existe una variable de entorno llamada `LD_ASSUME_KERNEL`  capaz de modificar el comportamiento normal del enlazador dinámico de las Glibc para utilizar los DSO/ABI de uno u otro modelo de hilos.

En sistemas relativamente modernos, las libreras Glibc incluyen diferentes versiones de libreras capaces de implementar uno u otro modelo de hilos: 

  * `/lib/libpthread.so.0` 		(LinuxThreads fixed stack size)
  * `/lib/i686/libpthread-0.10.so` (LinuxThreads floating stacks)
  * `/lib/tls/libpthread-0.34.so` 	(NPTL disponible por primera vez en Red Hat 9)

Para saber el modelo de hilos utilizado podemos utilizar el comando getconf.
    
    :::Console 
    getconf GNU_LIBPTHREAD_VERSION
    NPTL 0.34

Como hemos dicho, si bien en Red Hat 9 NPTL es el modelo de hilos utilizado por defecto, utilizando la variable `LD_ASSUME_KERNEL`, es posible forzar al enlazador dinámico (Dynamic Linker LD) a la hora de cargar los DSOs requeridos por un programa, de manera que cargue los correspondientes a un modelo de threads u otro al ASUMIR que la ABI que le ofrecer el kernel es de una versión anterior a la del kernel actualmente en ejecución.

```    
LD_ASSUME_KERNEL=2.2.5
getconf GNU_LIBPTHREAD_VERSION
linuxthreads-0.10
```

```
LD_ASSUME_KERNEL=2.4.1
getconf GNU_LIBPTHREAD_VERSION
linuxthreads-0.10
```

```
LD_ASSUME_KERNEL=2.4.20
getconf GNU_LIBPTHREAD_VERSION
NPTL 0.34 
```	

Mediante el comando `eu-readelf` presente en el paquete `elfutil`s, es posible saber el modelo de ABI requerido por un DSO.

    :::Console
    eu-readelf -n /lib/libnss_nis.so.1
    
    Note segment of 32 bytes at offset 0x000000f4:
    Owner          Data size  Type
    GNU                   16  VERSION
    OS: Linux, ABI: 2.2.5


En el ejemplo anterior, la librera `libnss_nis.so.1` requiere de una ABI/Kernel superior o igual a la que ofrecía un kernel de la versión 2.2.5.

Otros ejemplos:

```
eu-readelf -n /lib/i686/libc-2.3.2.so

Note segment of 32 bytes at offset 0x00000114:
Owner          Data size  Type
GNU                   16  VERSIONOS: Linux, ABI: 2.4.1
```

```
eu-readelf -n /lib/tls/libc-2.3.2.so
Note segment of 32 bytes at offset 0x00000134:
Owner          Data size  Type
GNU                   16  VERSIONOS: Linux, ABI: 2.4.20
```

 
###Errores derivados de un mal uso de `LD_ASSUME_KERNEL`

Las utilidades del sistema de paquetes RPM dependen de libreras que requieren una ABI y libreras con capacidades NPTL. Si utilizamos la variable `LD_ASSUME_KERNEL` para forzar al enlazador dinámico a utilizar las libreras de la implementación de hilos LinuxThreads, corremos el riesgo de obtener resultados inesperados o incluso de corromper la base de datos Berkley DB del sistema RPM, ya que esta base de datos está pensada y optimizada para su ejecución en un entorno de hilos NPTL.

Es por este motivo que es recomendable estar seguros de que NO hemos modificado el valor de dicha variable de entorno antes de proceder a construir, o instalar un paquete mediante las herramientas del sistema de paquetes RPM.

Las capturas siguientes muestran la estrecha relación que existe entre las herramientas RPM y el modelo de hilos NPTL.
    
```    
ldd /bin/rpm
librpm-4.2.so = /usr/lib/librpm-4.2.so (0x4002a000)
librpmdb-4.2.so = /usr/lib/librpmdb-4.2.so (0x4007e000)
librpmio-4.2.so = /usr/lib/librpmio-4.2.so (0x4015d000)
libpopt.so.0 = /usr/lib/libpopt.so.0 (0x401bb000)
libelf.so.1 = /usr/lib/libelf.so.1 (0x401c3000)
libpthread.so.0 = tls/libpthread.so.0 (0x401d3000)
librt.so.1 = tls/librt.so.1 (0x401e2000)
libbz2.so.1 = /usr/lib/libbz2.so.1 (0x401f4000)
libc.so.6 = tls/libc.so.6 (0x42000000)
/lib/ld-linux.so.2 = /lib/ld-linux.so.2 (0x40000000)
```

```
ldd /usr/bin/rpmbuild
librpmbuild-4.2.so = /usr/lib/librpmbuild-4.2.so (0x00bba000)
librpm-4.2.so = /usr/lib/librpm-4.2.so (0x008a3000)
librpmdb-4.2.so = /usr/lib/librpmdb-4.2.so (0x00252000)
librpmio-4.2.so = /usr/lib/librpmio-4.2.so (0x00380000)
libpopt.so.0 = /usr/lib/libpopt.so.0 (0x00d26000)
libelf.so.1 = /usr/lib/libelf.so.1 (0x00aef000)
libbeecrypt.so.6 = /usr/lib/libbeecrypt.so.6 (0x0061a000)
librt.so.1 = /lib/tls/librt.so.1 (0x00d56000)
libpthread.so.0 = /lib/tls/libpthread.so.0 (0x005ac000)
libz.so.1 = /usr/lib/libz.so.1 (0x00c0e000)
libbz2.so.1 = /usr/lib/libbz2.so.1 (0x00e55000)
libc.so.6 = /lib/tls/libc.so.6 (0x00111000)
/lib/ld-linux.so.2 = /lib/ld-linux.so.2 (0x00364000)
```
    
``` 
eu-readelf -n /lib/tls/librt.so.1
Note segment of 32 bytes at offset 0x00000134:
Owner          Data size  Type
GNU                   16  VERSION
OS: Linux, ABI: 2.4.20
```
    
```
eu-readelf -n /lib/tls/libpthread.so.0
Note segment of 32 bytes at offset 0x00000114:
Owner          Data size  Type
GNU                   16  VERSION
OS: Linux, ABI: 2.4.20
```

La conclusión que cabe sacar de todo esto es que un abuso de la variable `LD_ASSUME_KERNEL` puede tener consecuencias inesperadas y hacernos perder mucho tiempo tratando de averiguar qué es lo que esta provocando el problema.

La regla sera dejar que sea el sistema el encargado de establecer el modelo de hilos bajo en que se ha de ejecutar cada aplicación y solo forzar un modelo distinto cuando estemos seguros que es eso lo que requiere nuestra aplicación.
    
    
###Bibliografa:

*Wikipedia*

  * [http://en.wikipedia.org/wiki/Thread_%28computer_science%29]()

*Red Hat*

  * [http://people.redhat.com/drepper/assumekernel.html]()

*IBM*

  * [http://publib.boulder.ibm.com/infocenter/wasinfo/v5r1//index.jsp?topic=/com.ibm.websphere.base.doc/info/aes/ae/cins_nptl.html]()
  * [http://www-128.ibm.com/developerworks/linux/library/l-threading.html?ca=dgr-lnxw07LinuxThreadsAndNPTL]()
