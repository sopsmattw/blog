Title: Instalar GNU/Linux en el iPod con el iPodLinux Installer
Date: 2006-05-02 21:00:35
Category: Spanish
Tags: ipod, linux
Author: frommelmak

Instalar GNU/Linux en el iPod es cada dia más fácil. Para demostrarlo, os voy a explicar cómo utilizar la última version del instalador gráfico [iPodLinux Installer](http://ipodlinux.org/Installer_2) bajo GNU/Linux.

Antes de empezar, a seguir los sencillos pasos aquí descritos, te recomiendo que te des un paseo por [ipodlinux.org](ipodlinux.org), la web de referencia en esto de meter al pingüino dentro del iPod.

Como siempre, os dejo la obligada [galeria de imagenes](http://nomeriasdeti.no-ip.com/index.php?top_tab=2&section_type=3&task=view&id_album=27) con todo el proceso y este video.

http://www.youtube.com/watch?feature=player_embedded&v=WqcSUly6oG0

El método descrito a continuación, lo he aplicado a un iPod Photo de 20GBytes (La primrea generación con pantalla a color), así que es muy probable que los problemas que te encuentres no sean los mismos que los que he tenido yo, ya que el soporte difiere bastante de un modelo de iPod a otro.

Primer intento fallido

El primer intento lo hice la semana pasada utilizando la version 2.0 (build 1094) del instalador gráfico para GNU/Linux:

`ipl-installer-linux-svn-1094.run`

El procedimiento para instalar el IpodLinux Installer es muy sencillo. Tan sólo hemos de descargar el fichero ipl-installer-linux-svn-1094.run, darle permisos de ejecución, y lanzarlo como root.

Tras esto, el instalador queda ubicado en en: `/opt/iPodLinux/installer`.

Para iniciar la instalación de GNU/Linux en el iPod, sólo has de pinchar tu iPod al PC y asegurarte de que ninguna aplicación monta el filesystem del iPod. En mi caso, KDE/SuSE lo monta por defecto nada más pincharlo, asi que hay que desmontarlo a mano

    ::::Console
    umount /media/ipod (en mi caso) 

Al ejecutar el installer, aparece una pantalla muy bonita de bienvenida. Tras pulsar SIGUIENTE, aparece otra diciendo que ha detectado tu iPod y que pulses SIGUIENTE para iniciar la instalación de GNU/Linux.

El problema de esta versión aparece durante la copia de ficheros al iPod. Concretamente, la instalación falla con este mensaje:

    ::::Console
    /bin/podzilla not found

Si intentamos volver a instalar con esta vesión del instalador, éste detecta que ya parece haber un Linux (o parte de él) instalado en el iPod, y sólo nos la la opción de actualizarlo, cambiar el orden de arraque o bien desinstalar Linux. Pues bien, da igual lo que selecciones porque ya no es capaz de realizar mucho mas. Afortunadamente, es posible seguir utilizando el firmware de Apple sin más.

Segundo Intento (...casi!)

Hoy me ha dado por mirar en la web del proyecto y he visto que ya habia una nueva versión 2.1 (build 1153) disponible. 

`ipl-installer-linux-svn-1153.run`

Lo mejor de todo es que además decian en una nota que esta versión  solventaba el fallo que yo estaba teniendo!

Bueno, he repetido el procedimiento con la nueva versión, pero al ejecutar el installer, me he encontrado con un problema de dependencias con unas librerias `libQt` que forman parte del paquete `qt-x11` y que no tenia isntalado.

Tras instalar dichas librerias, he podido ejecutar el instalador gráfico sin más.

Aparentemente, el proceso de instalación finaliza sin problemas, pero tras reiniciar el iPod, no hay manera de que arranque con Linux.

A la tercera va la vencida

Tras mirar un rato qué es lo que había copiado en el iPod, me he dado cuenta que el owner del `loader.bin` era un usuario con UID 1000, en lugar de root, como el resto.

    ::::Console
    chown root:root loader.bin

Tras cambiar el owner a root y despues de un reboot del iPod (mantener pulsado **menu + select**), el iPod ha arrancado con Linux!

Bueno, son muchas las aplicaciones con las que he de trastear aun, así que en breve ire ańadiendo mis impresiones acerca de meter al pigüino en el iPod.

**Nota**: En ocasiones, no queda más remedio que hacer un restore del firmware de Apple utilizando el software oficial del fabricante (sólo disponible para Windows). Por ejemplo, antes de intenar con la nueva versión del iPodLinux Installer, me vi obligado a eliminar por completo todo resto anterior de Linux (canciones incluidas), antes de volver a intentar la instalación de Linux. Así que ya sabeis, aseguraros de tener a buen recaudo vuestra bilbioteca de canciones antes de poneros a jugar con el intaller.
