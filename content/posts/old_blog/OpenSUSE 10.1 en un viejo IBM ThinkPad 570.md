Title: OpenSUSE 10.1 en un viejo IBM ThinkPad 570
Date: 2006-10-11 21:10:13
Category: Spanish
Tags: opensuse, grub
Author: frommelmak

Hace ya algún tiempo llego a mis manos un viejo IBM ThinkPad 570 (gracias Lluis !) que había caído en el olvido , hasta que hoy mi hermano me ha pedido que le instalara una distro GNU/Linux para salir de un apuro. Sí! Lo has adivinado, este post explica el proceso para instalar OpenSUSE 10.1 en un IBM ThinkPad 570. La gracia del tema, es que el portátil en cuestión carece de lector de CD/DVD ni tarjeta de RED. El único dispositivo de entrada/salida disponible es una disquetera externa del siglo pasado.

El procedimiento que he seguido ha consistido en pinchar el disco duro del IBM en mi actual portatil, que sí que dispone de lector de DVD, e instalar entonces la OpenSuse sobre el disco del IBM desde el DVD.

Hasta aquí todo perfecto, el problema ha sido que tras volver a poner el disco duro al IBM, este no arrancaba, ya que no encontraba el boot loader (grub) por ningún sitio. Tras googlear un rato, he encontrado esta solución:

He arracado una knoppix en el ordenador de mi padre, ya que mi flamante portatil carece de disquetera. Una vez allí, he hecho lo siguiente:

    :::Console
    mk2efs -m 0 /dev/fd0
    mkdir /mnt/floppy
    mount /dev/fd0 /mnt/floppy
    grub-install --force-lba --root-directory=/mnt/floppy fd0

Esto crea el `/boot/grub` con todos los ficheros necesarios en el floppy (básicamente los mismos que hay en `/lib/grub/i386-pc`).

El fichero que no copia es el `menu.lst`, así que lo que creado basándome en el de mi portatil. Ha quedado así: 

    :::Console 
    default 0
    timeout 8
    title SUSE Linux 10.1
          root (hd0,1)
          kernel /boot/vmlinuz
          boot=/dev/hda2
          initrd /boot/initrd

Finalmente, desmontamos el floppy: `umount /mny/floppy`

Esto ha sido suficiente para poder arrancar el sistema desde el floppy. Tras esto, ya sólo he tenido que instalar el *grub* en el disco duro de la siguiente manera:

    :::Console
    grub-install /dev/hda

Los últimos retoques han consistido en configurar las X vía Yast2 (en modo texto, runlevel3)y deshabilitar algunos servicios inútiles, ya que el portatil es muy pero que muy justo para mover un KDE.De todo el proceso, lo más complicado ha sido encontrar un disquete que poder meter en la disquetera.
