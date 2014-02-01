Title: Incoherencias entre los comandos df y du
Date: 2007-07-02 20:03:02
Category: Spanish
Tags: disk, filesystem, du, df, fsck
Author: frommelmak

Siempre había pensado que cuando los comandos `du -hsx .` y `df -h .` reportaban tamaños significativamente diferentes, estábamos ante un filesystem corrrupto, y que en estos casos la solución pasaba por hacer un `fsck` de dicho filesystem.

Pues bien, hoy me he encontrado con los mismos síntomas, pero en esta ocasión el problema no era un filesystem corrupto sino algo bastante más simple. Algo tan tonto como que el punto de montaje de mi filesystem no estaba vacío y además contenía folders que se llamaban igual que los folders que contenía el filesytem que estaba montando encima.

Como no hay mal que por bien no venga, el problema me ha servidor para aprender diferentes formas de forzar un `fsck` en un folder que no podemos desmontar...

##Opcion 1: 

Forzar un `fsck` en el siguiente reboot (hay hasta 5 maneras diferentes de hacerlo).

###Shutdown

    :::console
    shutdown -rF now

Esto realizar un `fsck` en tiempo de arranque en todas las particiones.

###tune2fs

Podemos modificar los valores de máximo numero de montajes sin realizar `fsck` o tiempo máximo entre fscks.

    :::console
    debugfs -w -R dirty /dev/hda3

Interesantísima utilidad que nos permite entre otras muchas cosas marcar el filsystem como dirty para forzar un `fsck` en el siguiente `reboot`. También nos permite hacer un `undelete` de un fichero o directorio borrado en filesystems tipo ext3.

###.autofsck

Consiste en crear un fichero `.autofsck` en el filesystem en el que queremos forzar el `fsck`. Sólo funciona en algunas distribuciones.

###Fecha BIOS

Modificando la fecha en la BIOS**  No lo he probado, y a primera vista parece feo de narices pero por lo visto funciona.

##Opcion 2

Arrancar el sistema afectado con un livecd y hacer el fsck desde allí.

En mi caso el sistema tenia todas las particiones en LVM por lo que antes he tenido que hacer un `vgscan` y luego un `vgchange -a y` para poder montar el *logical volume* desde la Knoppix.

En cualquier caso nada de esto era en realidad necesario pues como ya he dicho al principio, al filesystem no le pasaba nada.
