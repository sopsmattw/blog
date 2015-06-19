Title: Modificar ficheros de una imagen de disco particionada
Date: 2015-06-12 11:28:00
Category: Spanish 
Tags: dd, mount, fdisk, raspberrypi 
Author: frommelmak

En ocasiones disponemos de una imagen RAW de disco sobre la que queremos realizar cambios, pero queremos ahorrarnos el proceso de: 

  - Copiar el fichero de imagen a un dispositivo con ''dd''.
  - Montar el dispositivo para tener acceso a los filesystems del mismo.
  - Realizar cambios sobre los ficheros.
  - Volver a generar el fichero de imagen volcando el contenido de device con dd.

Si dispones de una RaspberryPi, seguro que estás cansado de tener que realizar todo este proceso cada vez que quieres hacer cambios sobre algun fichero de la imagen fuente. 

Seguro que has escuchado mil veces que en Linux todo es un fichero, incluidos los dispositivos. Pues bien, gracias a esto podemos ahorrarnos el proceso de tener que recurrir a un dispositivo físico, ya que vamos a utilizar un fichero en su lugar.

El procedimiento es tan simple como hacer esto:

Listamos las particiones que contiene el fichero de imagen:

    ::::bash
    fdisk -l image-file.img

    Disk image-file.img: 16.0 GB, 16012804096 bytes
    255 heads, 63 sectors/track, 1946 cylinders, total 31275008 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x0009bf4f

                                Device Boot      Start         End      Blocks   Id  System
    image-file.img1                               8192      122879       57344    c  W95 FAT32 (LBA)
    image-file.img2                             122880    31275007    15576064   83  Linux


Multiplicamos el tamaño del bloque (512 bytes) por el número de sectores en el que empieza la partición linux.

Utilizaremos este número para montar sólo el filesystem que nos interesa.

    ::::bash
    sudo mount -o loop,offset=62914560 image-file.img IMG/

Hacemos los cambios y desmontamos.

Ahora la próxima vez que volquemos la imagen a un dispositivo, los nuevos cambios estarán reflejados.
