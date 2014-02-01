Title: Backup completo de un guest Linux mediante tar
Date: 2010-05-03 17:25:39
Category: Spanish
Tags: backup, tar
Author: frommelmak

Clonar una mquina virtual mediante *VMWare Converter* suele ser un proceso lento, especialmente si la máquina tiene un disco grande, este el espacio ocupado o no. En ocasiones, ya no es que sea lento, sino que directamente el *VMWare Converter* falla inexplicablemente. En estos caso tenemos dos opciones. O bien copiar el disco de la máquina mediante SSH (si tenemos acceso `ssh` al *ESXi*) o bien hacer un *tarball* de todo el sistema y extraerlo en una nueva máquina.

A continuacóin detallo los pasos para realizar este último procedimiento.

En primer lugar hay que crear el `tar.gz` de la máquina origen. Para ello, conectamos por SSH y nos aseguramos de que disponemos de espacio. Luego ejecutamos el comando que vuelca toda la raiz del sistema a un *tarball*:

    :::console
    cd /
    tar cvlz --exclude=./tmp/* --exclude=./var/tmp/* --exclude=./proc/* --exclude=./sys/* --exclude=./mnt/* -f /var/tmp/guest_backup.tar.gz .

En primer lugar necesitamos una ISO bootable de un sistema Linux con las herramientas necesarias para hacer la extracción y restauración del *tarball*. Una buena distro para estos menesteres es RIP Linux.

[RIP Linux Image](http://rip.7bf.de/current/RIPLinux-9.3-non-X.iso)

Copiaremos esta ISO al datastore del ESXi de destino.

Ahora creamos una máquina en el ESXi de destino con un disco de igual tamao al que queremos copiar y configuraremos esta máquina para que arranque con la ISO de RIP Linux.

Particionamos el disco `sda` de la máquina y lo formateamos.

    :::console
    fdisk /dev/sda
    mkfs.ext3 /dev/sda1
    mkswap /dev/sda2
    mount /dev/sda1 /mnt/sda1

Nos asignamos una IP y copiamos el `tar.gz` a la via `scp` y extraemos el *tarball*.

    :::console
    ifconfig eth0 x.x.x.x
    cd /mnt/sda1
    scp user@host:/guest_backup.tar.gz .
    tar zxvf guest_backup.tar.gz
    chroot /mnt/sda1
    grub-mkconfig /boot/grub/grub.cfg
    grub-install /dev/sda

Ahora ya podemos reiniciar el equipo.

Si teniamos *mysql* corriendo, deberemos restablecer el owner de los siguientes directorios, ya que el UID de mysql en diferente en Debian al de RIP Linux.

    :::console
    chown -R mysql /var/run/mysqld
    chown -R mysql /var/log/mysql
    chown -R mysql /var/log/mysql.*
    chown -R mysql.mysql /var/lib/mysql

Es posible que tengamos que repetir el mismo procedimiento si utilizabamos servicios que corran bajo un usuario cuyo UID difiera del que utiliza RIP Linux.

Finalmente, si nuestro `fstab` hacia referencia a UUIDs en lugar de a devices, lo mejor es modificarlo y asegurarnos que utiliza los devices que toca.

