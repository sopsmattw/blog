Title: Jugando con KXDocker otra vez
Date: 2006-07-13 19:41:09
Category: Spanish
Tags: dock, kxdocker
Author: frommelmak

Tras un tiempo sin KXDocker debido a la actualización de [OpenSuSE](http://www.opensuse.org/) 10 a 10.1, tenia ganas de volver a instalar esta aplicación que ya encontraba a faltar. Hoy por fin he tenido un ratito para volver a compilar, instalar y configurar esta impresionante barra de tareas.

Me he llevado una grata sorpresa al ver las nuevas funcionalidades que se han añadido, la mejora conseguida en el rendimiento y sobretodo la facilidad de configuración que es ahora totalmente [gráfica](http://nomeriasdeti.no-ip.com/photos/albums/32/kxdocker5.png) y muy intuitiva.

![KXDocker](/images/old_blog/kxdocker_1.png)

Bueno, sin más os explico cómo se instala y configura la aplicación sin tener que perderse buceando por la desordenada web del proyecto.

##Compilar e instalar KXDocker

Como ya he dicho, la [web oficial](http://www.xiaprojects.com/www/prodotti/kxdocker/main.php) es un poco complicada, y a veces cuesta encontrar la información que estas buscando. Asi que trataré de ahorraros tiempo a la hora de instalar la última versión de KXDocker, que en el momento de escribir esto es la 1.1.4a.

Antes de nada hemos de saber que la última version de los paquetes esta siempre en la sección de downloads que es [esta](http://www.xiaprojects.com/www/prodotti/kxdocker/main.php?action=download):

Desde alli descargaremos el [código fuente](http://www.xiaprojects.com/www/downloads/files/kxdocker/1.0.0/kxdocker-1.1.4a.tar.bz2) de KXDocker y lo compilaremos como root:

    :::bash
    mkdir /tmp/kxdocker
    cd /tmp/kxdocker
    wget http://www.xiaprojects.com/www/downloads
    /files/kxdocker/1.0.0/kxdocker-1.1.4a.tar.bz2
    tar -jxvf kxdocker-1.1.4a.tar.bz2
    cd kxdocker-1.1.4a
    ./configure --prefix=/opt/kxdocker
    make
    make install

Tras esto, estaremos en disposición de lanzar KXDocker (recuerda hacerlo con tu usuario no como root):

    :::bash
    /opt/kxdocker/bin/kxdocker &

Para lanzar KXDocker al iniciar tu sesion de usuario puedes crear el siguiente enlace simbólico:

    :::bash
    ln -s /opt/kxdocker/bin/kxdocker ~/.kde/Autostart/

Antes de entrar en detalles relacionados con la configuración, has de saber que la mayoria de funcionalidades "extra" de KXDocker -más alla de mostrar iconos en la barra- se consigue mediante la utilización de plugins.

Los plugins recomomendados por el autor son estos: [kxdocker-resources-1.1.0.tar.bz2](http://www.xiaprojects.com/www/downloads/files/kxdocker/1.0.0/kxdocker-resources-1.1.0.tar.bz2), [kxdocker-configurator-1.0.2.tar.bz2](http://www.xiaprojects.com/www/downloads/files/kxdocker/1.0.0/kxdocker-configurator-1.0.2.tar.bz2), [kxdocker-dcop-1.0.0.tar.bz2](http://www.xiaprojects.com/www/downloads/files/kxdocker/1.0.0/kxdocker-i18n-1.0.2.tar.bz2), [kxdocker-i18n-1.0.2.tar.bz2](http://www.xiaprojects.com/www/downloads/files/kxdocker/1.0.0/kxdocker-trayiconlogger-1.0.0.tar.bz2) y [kxdocker-trayiconlogger-1.0.0.tar.bz2](http://www.xiaprojects.com/www/downloads/files/kxdocker/1.0.0/kxdocker-trayiconlogger-1.0.0.tar.bz2).

Para instalar los plugins, ya sean los recomendados o cualquier otro, seguiremos el siguiente procedimiento:

    :::bash
    cd /tmp/kxdocker
    wget www.xiaprojects.com/www/downloads
    /files/kxdocker/1.0.0/<desired-plugin>.tar.bz2
    tar -jxvf <desired-plugin>.tar.bz2
    cd <desired-plugin>
    ./configure --prefix=/opt/kxdocker --with-extra-libs=/opt/kxdocker/lib --with-extra-includes=/opt/kxdocker/include
    make 
    make install

Repetiremos estos últimos pasos para el resto de plugins.

**NOTA**:
Es probable que al compilar alguno de los plugins te aparezca el siguiente mensaje:

    :::console
    Warning: you chose to install this package in /opt/kxdocker,
    but KDE was found in /opt/kde3.
    For this to work, you will need to tell KDE about the new prefix, by ensuring
    that KDEDIRS contains it, e.g. export KDEDIRS=/opt/kxdocker:/opt/kde3
    Then restart KDE.

Para solventar el problema puedes hacer dos cosas: Cambiar el `--prefix` al hacer el `./Configure` -para que apunte a `/opt/kde3`- o bien asegurar que antes de ejecutar KDE, la variable de entorno `KDEDIRS` contiene el path a `/opt/kxdocker`. Puedes crear un fichero en `/etc/profile.d` para tal efecto. Tan solo deberá contener esto:

    :::bash
    export KDEDIRS=/opt/kxdocker:/opt/kde3


##Configurando la de la barra a golpe de ratón

Cuando lanzamos KXDocker, nos aparecerá una barra con un solo icono. Para añadir aplicaciones a la barra, y para controlar el [tamaño](http://nomeriasdeti.no-ip.com/photos/albums/32/kxdocker5.png) y [posicion](http://nomeriasdeti.no-ip.com/photos/albums/32/kxdocker6.png) de la misma etc, lo mas recomendable es tener instalado el plugin [kxdocker-configurator-1.0.2.tar.bz2](http://www.xiaprojects.com/www/downloads/files/kxdocker/1.0.0/kxdocker-configurator-1.0.2.tar.bz2).

Si además hemos instalado [kxdocker-trayiconlogger](http://www.xiaprojects.com/www/downloads/files/kxdocker/1.0.0/kxdocker-trayiconlogger-1.0.0.tar.bz2), al lanzar la aplicación nos saldrá un [iconito](http://nomeriasdeti.no-ip.com/photos/albums/32/low-kxdocker7.png) en la barra de herramientas de KDE, si pulsamos el boton derecho del mouse sobre el mismo, tendremos acceso al menu de "Configurator", desde el cual podremos añadir a [golpe de raton](http://nomeriasdeti.no-ip.com/photos/albums/32/low-kxdocker2.png) nuevos iconos a nuestro Dock.
Por defecto la aplicación nos mostrará los iconos de KDE (KDElibs). No obstante, podemos utilizar los que proporciona KXDocker -mucho más vistosos- que estan ubicados aqui:

    :::console
    /opt/kxdocker/share/apps/kxdocker/themes/icons/

###Cambiar el orden de los iconos en la Dock 
Es tan fácil como arrastrarlos con el raton a la posición que queramos.
Una de las caracteristicas a destacar de KXDocker es que agrupará todos aquellos iconos que pertenezcan al mismo grupo en la misma posición del dock. Asi, es posible agrupar todos los programas de comunicación (Skype, AMSN, Kopete, etc) bajo un mismo grupo/categoria. De esta manera podremos mostrarlos a modo de carrusel con la rueda del mouse. 
No obstante, los iconos pertenecientes a un mismo grupo no se agrupan hasta que no se cierra la aplicación y se vuelve a lanzar.

##Plugins Interesantes

He encontrado de especial interes los siguientes plugins: `kxdocker-gaclock`, `kxdocker-gbattery`, `kxdocker-gdate`, `kxdocker-gtrash`.

**Gaclock**
El primero de ellos nos muestra un bonito reloj analógico que podemos utilizar para sincronizar nuestro sistema via NTP, además de mostrarnos la hora del sistema en todo momento. 

**Gbattery**
El segundo nos muestra el estado de la bateria de nuestro portatil, asi como información de si estamos conectados a la red electrica o no.

**Gdate**
Muestra la fecha utilizando uno de esos calendarios en los que se ha de arrancar una hoja cada dia (me encanta!).  

**Gtrash**
Finalmente, Gtrash es la famosa papelera de reciclaje del sistema. Esta se llena cuando borramos algun fichero de nuestro escritorio o filesystem.

##Puntos a mejorar

A pesar de las mejoras, hay muchas cosas que aun pueden mejorarse. Para empezar la web del proyecto, que sigue siendo muy poco intuitiva.

Para ver las aplicaciones que tienes abiertas minimizadas en la dock, tan solo hay que compilar e instalar el plugin kxdocker-taskmanager de la siguiente manera:

    :::console
    ./configure --prefix=/opt/kxdocker/ --with-extra-libs=/opt/kxdocker/lib/ --with-extra-includes=/opt/kxdocker/include
    make
    make install

Otra de las carencias del proyecto se deriaba de la falta de paquetes precompilados para las diferentes distros. Pese a que esto último es más achacable a "la comunidad" que al lider del proyecto, estoy seguro de que si la compilación fuera más sencilla, habria más de un gente dispuesta a mantener paquetes para las diferentes distros.

Bueno, si consigo tenerlo full equip, igual hasta me tomo la molestia de crear los RPM para SuSE 10.1.
