Title: Instalar Xgl + Compiz en SuSE 10.x con KDE
Date: 2006-04-10 20:54:30
Category: Spanish
Tags: xgl, compiz
Author: frommelmak

Hoy, tras mucho tiempo con ganas de probarlo me he decidido a instalar Xgl + Compiz en SuSE 10.x.

Primero lo he instalado en una SuSE 10.1 Beta 9 sobre un hardware sobrado de potencia (Intel Xeon 2.8GHz 2GB RAM + NVidia Quadro FX 1300) y en vista del éxito, me he decidido a probarlo también en mi portatil SuSE 10.0 (Centrino a 1.73GHz 1GB RAM + Intel GMA 900).

La última información referente a Xgl en SuSE la encontrareis siempre aquí: [http://en.opensuse.org/Xgl](http://en.opensuse.org/Xgl)

Desde allí, llegareis a esta otra pagina en la que explican cómo instalar y utilizar Xgl en SuSE. Tanto si utilizas KDE o Gnome: [http://en.opensuse.org/Using_Xgl_on_SUSE_Linux](http://en.opensuse.org/Using_Xgl_on_SUSE_Linux) A continuación os detallo el procedimiento que he seguido en ambos casos, y los resultados obtenidos. De esta manera podreis haceros una idea de lo que podeis esperar de vuestros sistemas. Os dejo también [esta](http://nomeriasdeti.no-ip.com/index.php?top_tab=2&section_type=3&num=&task=view&id_album=26) galería de imagenes con algunas capturas.

**Actualización**: He actualizado Xgl, Compiz y algunas librerias a la versión de la Release Candidate 1 de SuSE 10.1. No he encontrado mejoras radicales, slo alguna mejora con las knotes asi que habrá que esperar a la version 10.1 y ver si el kernel y los nuevos drivers solventan los problemas con Intel.

Por otro lado, he encontrado [este](http://www.tuxpan.com/fcatrin/es/comments.php?guid=20060311) interesantisimo articulo que aclara conceptos a veces confusos sobre los nuevos composite manager versus los windown-managers tradicionales. MUY RECOMENDABLE!

**Actualización 2**: Me comentan desde Mexico que algunos de los RPM referenciados en este articulo ya no se encuentran disponibles. Si es tu caso mira a ver si es uno de los que he podido rescatar de mi portatil y poner en este tarball [Xgl-SuSE-10.x-RPMS.tar.gz](http://nomeriasdeti.no-ip.com/files/Xgl-SuSE-10.x-RPMS.tar.gz)

#Instalación en SuSE 10.1 (Beta 9)

La instalación sobre una SuSE 10.1 no tiene ningun misterio. Los Pasos a seguir serian estos:

##Instalar el driver de NVidia oficial

Si dispones de una tarjeta de video NVidia, SuSE 10.1 cargar por defecto el módulo de NVidia que viene con el kernel (`nv`). Sin embargo para hacer funcionar Xgl es necesario instalar los drivers oficiales de NVidia. Por otro lado, es importante hacer esto antes de instalar el paquete Xgl.

Antes de bajarte e instalar el driver oficial de NVidia, asegurate que has instalado las fuentes del kernel y el compilador gcc, ya que son necesarias para compilar el modulo nvidia, pues no viene uno precompilado en el paquete oficial y ser necesario compilar uno especifico para nuestro kernel.

La forma más sencialla de instalar las fuentes es via YaST. Para instalar el driver oficial de Nvidia haz esto:

    :::console
    init 3
    wget http://download.nvidia.com/XFree86/Linux-x86/ 1.0-8756/NVIDIA-Linux-x86-1.0-8756-pkg1.run
    chmod u+x NVIDIA-Linux-x86-1.0-8756-pkg1.run
    ./NVIDIA-Linux-x86-1.0-8756-pkg1.run 

El proceso de instalación de NVidia nos informar de que no existe un módulo precompilado para nuestra distribución y nos preguntará si queremos compilar uno. Le decimos que sí.

Finalmente nos pregunta si queremos modificar el fichero `xorg.conf` para que cargue el nuevo módulo. Le diremos tambin que sí.

Ahora volvemos a lanzar el entorno gráfico, tras lo cual podremos seguir con la instalación del server gráfico OpenGL Xgl.

    ::::console
    init 5

##Instalar Xgl + Compiz (via Yast)

Si queremos evitar problemas de dependencias, lo más sencillo es instalar Xgl y Compiz via YaST. Haciendolo de esta manera, no tendremos ningún problema.

Hay que tener en cuenta que si no tenemos instalado Gnome en nuestro sistema, se instalarán varios componentes de Gnome (`control-center2`, `gnome-window-decorator`...) así como algunas librerias (`libsvg`, `libsvg-cairo`...). En cualquier caso, sera YaST el encargado de resolver dichas dependencias.

##Configurar Xgl como servidor de X principal

Ahora ya sólo queda configurar el sistema para ejecutar Xgl y cargar los plugins de Compiz con los efectos que queramos.

Para ejecutar Xgl deberemos decirle a kdm que ejecute Xgl en lugar del servidor de X. En SuSE 10.1 esto es muy fácil, ya que disponemos de una variable en `/etc/sysconfig/displaymanager` que nos permite hacerlo. Así, pondremos el valor de la variable `DISPLAYMANAGER_XSERVER` a `Xgl`. Hecho esto, ejecutaremos:

    :::console
    SuSEconfig --module xdm

Y reiniciaremos las X. Lo sé, tras reiniciar has movido una de las ventanas y te has llevado una desilusión al ver que no ha pasado nada. No se ha deformado ni nada expectacular. No te preocupes, es normal porque no hemos cargado ningun plugin de Compiz.

Hay multitud de opciones que pueden modificar muy mucho el funcionamiento del servidor Xgl. Muchas de ellas dependen del hardware utilizado. Para ver la lista de opciones, puedes consultar este Documento `/usr/share/doc/packages/xgl/README.SUSE`

##Configurar Compiz como gestor de ventanas

Todas las funcionalizades de Xgl, se explotan via plugins del composite manager Compiz. Tan slo has de cargar los que quieras para porder utilizarlos.
Por ejemplo, para conseguir el efecto de elasticidad en las ventanas cargariamos los plugins bsicos (decoration move resize place minimize) y además el wobbly.
Para cargar todas las opciones utilizariamos un comando como este:

    :::console
    compiz --replace gconf decoration wobbly fade minimize cube rotate zoom scale move resize
    place switcher  &
    gnome-window-decorator &

**NOTA**:Cuando cargamos el plugin gconf por primera vez, Gconf guarda un registro con los plugins cargados. De esta manera, en posteriores llamadas a Compiz

    :::console
    compiz --replace gconf decoration wobbly...

Los módulos que aparecen tras `gconf` son ignorados, ya que la configuracin de los modulos a cargar se lee de un registro que guarda `gconf`.

Posteriormente los cambios deberiamos realizarlos mediante el editor gconf-editor. Lamentablemente, este **NO** esta disponible para KDE, por lo que para arrancar Compiz al arranque editaremos el archivo `~/.kde/Autostart/compiz.desktop`:

    :::console
    [Desktop Entry]
    Encoding=UTF-8
    Exec=compiz --replace decoration wobbly fade minimize cube rotate zoom scale move resize place switcher &  gnome-window-decorator &
    GenericName[en_US]=
    StartupNotify=false
    Terminal=false
    TerminalOptions=
    Type=Application
    X-KDE-autostart-after=kdesktop 

#Instalación en SuSE 10.0

Como ya he comentado al principio de este articulo, la instalacin sobre SuSE 10.0 la he llevado a cabo sobre mi portatil, un **Compaq Presario V4000**.
Dado que la targeta gráfica del Compaq es una Intel GMA900 (driver i915). Nos podemos saltar el paso de la instalacin de los drivers oficiales de NVidia.

##Instalar Xgl + Compiz

Tal y como aparece en la web de [OpenSuSE](http://www.opensuse.org/), la manera ms rpida de instalar el software en SuSE 10.0 es esta: Actualizacin:Antes de nada, debes instalar estos paquetes de compatibilidad(gracias a Jose Alberto por sufrir la primera version de este manual ;o) ) 

  * xgl_compat100
  * libdrm

Instalamos via YaST el `control-center2` y luego descargamos e instalamos los siguientes paquetes:

    :::console
    wget http://ftp.gwdg.de/pub/opensuse/distribution/SL-OSS-factory/ inst-source/suse/i586/xgl-cvs_060405-4.i586.rpm
    wget http://ftp.gwdg.de/pub/opensuse/distribution/SL-OSS-factory/ inst-source/suse/i586/compiz-cvs_060407-3.i586.rpm
    wget http://ftp.gwdg.de/pub/opensuse/distribution/SL-OSS-factory/ inst-source/suse/i586/libsvg-0.1.4-11.i586.rpm
    wget http://ftp.gwdg.de/pub/opensuse/distribution/SL-OSS-factory/ inst-source/suse/i586/libsvg-cairo-0.1.6-11.i586.rpm
    wget http://ftp.gwdg.de/pub/opensuse/distribution/SL-OSS-factory/ inst-source/suse/i586/libwnck-2.12.2-19.i586.rpm
    rpm -ivh xgl-cvs_060405-4.i586.rpm compiz-cvs_060407-3.i586.rpm libsvg-0.1.4-11.i586.rpm libsvg-cairo-0.1.6-11.i586.rpm libwnck-2.12.2-19.i586.rpm 

Vamos ahora con la configuración.

##Configurar Xgl como servidor de X principal

En SuSE 10.0 no existe la variable `DISPLAYMANAGER_XSERVER` en el fichero `/etc/sysconfig/displaymanager`. En su lugar editaremos el fichero `/etc/opt/kde3/share/config/kdm/kdmrc` modificando el valor de la variable `ServerCmd`.

    :::console
    ServerCmd=/usr/X11R6/bin/Xgl -br

Tras esto ejecutamos:

    :::console
    SuSEconfig --module xdm

Ahora ya esta todo listo para que tras reiniciar las X (int 3; init 5) podamos cargar los plugins de Compiz.

##Configurar Compiz como gestor de ventanas

Para cargar los plugins de Compiz al arrancar KDE, podemos seguir un proceso anlogo al descrito para 10.1.

#Jugando con Compiz

Muchos de los plugins de Compiz se activan intrinsecamente con tan solo cargarlos. Por ejemplo, el efecto **Wobbly** deformar sin ms nuestras ventanas cada vez que movamos una de ellas. Por el contrario, hay una serie de funcionalidades ocultas que se activan mediante la combinacin de teclas y/o la accin del mouse. A continuacin os muestro las que me han parecido ms interesantes:

![Cube](/images/old_blog/hsm54_botton.png)

![Cube](/images/old_blog/hsm52_botton.png)

![Cube](/images/old_blog/compiz_water02.png)

##Scale (el Expose de MacOSX)

Esta función redimensiona todas las ventanas que tengamos en pantalla de manera que quepan todas en pantalla. Esta funcion es extremadamente útil, sobretodo en portatiles con poca área de visualización, ya que nos permite ver de una vez el contenido de todas las ventanas que tengamos abierta. Luego al hacer click sobre una de las ventanas, esta pasa a primer plano. IMHO, el efecto mejora bastante el de MacOSX.

Activación: F11 Combinable con el Switcher una vez escladas las ventanas.

##Switcher

Es la legendaria opción de cambio de tarea `Alt+Tab` per mejorada muy mucho. La principal novedad es que no vemos un carrusel de iconos, sino que veremos una previsualización de las aplicaciones!. En el caso de un reproductor de video, veremos el video ejecutandose, en el caso de Amarok o XMMS, veremos incluso las visualizaciones tipo espectro y el display de segmentos mostrando la canción que suena sin más!!! Sin duda muy útil y espectacular. Activación:

Alt+Tab

##Rotate

Esta es sin duda una de las opciones ms espectaculare y que ms ha dado que hablar, si bien no creo que sea de las ms tiles. Consiste en la posibilidad de cambiar de desktop haciendo girar toda la pantalla como si de un cubo se tratara. Es posible incluso poner una aplicacin en una de las esquinas del cubo y hacerlo rotar!. La informacin que muestran las ventanas es completamente en tiempo real. Veamos como utilizarlo

Activación: 

  * Ctrl + Alt + Teclas Iqz/Derecha  (Rotamos el desktop utilizando el teclado)
  * Ctrl + Shift + Alt + Teclas Izq/Dercha (Rotamos el desktop utilizando el teclado. La ventana activa se queda fuera del cubo llendo a parar al nuevo desktop)
  * Ctrl + Alt + boton mouse izq (rota el desktop manualmente. Hemos de tener el fondo de pantalla en el foco del mouse)

##Otras combinaciones de teclas para activar modulos de Compiz

  * Slow-motion = Shift + F10 (Activa y descativo todos los movimientos a velocidad super lenta o normal)
  * Transparencias = Ctrl + Alt + ruedecita del mouse. (varia el grado de transparencia de la ventana que esta en primer plano)
  * Zoom = Windows Key + wheel mouse (Solo me ha funcionado en NVidia)
  * Water = Crtl + WinKey Es necesario cargar el plugin water. En su modalidad Rain (shift + F9) simula el efecto de las gotas de lluvia al caer sobre el desktop, como si de un lago se tratara.

#Rendimiento

Ni que decir tiene que el rendimiento en un Xeon con 2GBytes de RAM y una NVidia Quadro FX es realmente expectacular y que la carga del sistema apenas se ve afectada. Por contra, en mi modesto portatil la cosa cambia bastante. Sobretodo si lo intento utilizar junto a kxdocker (barra de herramientas tipo MacOS X. Pese a que en el portatil no se ve tan suelto como en la workstation, la principal limitacin es que que la aceleracin XVideo no funciona para las tarjetas i915 y i945. El scroll de una web larga en el navegador se vuelve desesperante.
Por todo esto, se recomienda esperar a las versiones Xgl y Compiz de la Release Candidate 1 de SuSE 10.1 si utilizas el driver i914  i945 de Intel.

#Bugs y limitaciones

Tanto utilizando el driver de NVidia como el Intel, hay situaciones que Xgl no maneja bien o directamente se cuelga. Por ejemplo: 

  * En ambos casos, juegos como Frozen Bubble no se muestran correctamente.
  * Las notas de Knotes (No se visualizan correctamente con el driver de intel). Actualización: Tras actualizar xgl, compiz y algunas librerias a 10.1 RC1, se han solventado los problemas.
  * No es posible ver videos AVI (mplayer + drivers xv o xdivx) con el modulo de Intel.

**Nota**: Poco a poco ir añadiendo aquí los fallos que me vaya encontrando.

#Conclusión

De todas todas, si lo que quieres es utilizar xgl y compiz en un entrono de trabajo REAL lo deseable seria esperar a que se libere 10.1 y disponer de una tarjeta grafica completamente soportada. No obstante, si no deseas ejecutar todos los plugins disponibles, quizas puedas ir utilizando aquellos modulos que no te den problemas.

En el portatil, muchas aplicaciones que hacian uso de aceleraion XVideo producian un cuelgue total del sistema.

Así, no he conseguido reproducir  video con mplayer ni ejecutar muchos juegos.

Por el contrario, el trabajo con la workstation y el driver NVidia ha sido realmente increible. Sólo he medio-colgado una vez el sistema al ejecutar un juego.
El resto de funciones se han comportado muy bien (increiblemente rpido y movimientos suaves y sin saltos).
La carga de la máquina era siempre la misma hiciera lo que hiciera. Muy, muy recomendable si dispones de un equipo potente y soportado.
