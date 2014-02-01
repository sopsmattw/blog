Title: Grabando DVDs en FreeBSD 5.3
Date: 2006-02-02 23:13:12
Category: Spanish
Tags: freebsd, dvd, burn
Author: frommelmak

Hace tiempo que el backup de los ficheros sensibles de mi server no cabe en un único CDROM. El resultado práctico de esto es que el proceso automatico de backup requiere ahora de intervención humana, por lo que hace tiempo que no hago backups a soportes fisicos.

Hoy por fin, me he decidido a solventar el problema. Para ello he sustituido la actual unidad de CDs, por una de DVDs. Concretamente una regrabadora de DVDs/CDs 16x de **LG GSA-4167B**.

A continuación explico como instalar una grabadora de DVDs/CDs en **FreeBSD 5.3** y como utilizar `growisofs` para quemar DVDs.

Grabando CDs en FreeBSD:

Actualmente, utilizaba un sencillo script que metia todos los datos sensibles del server (las webs básicamente) en en tarball, creaba la imagen mediante `mkisofs` y lo volcaba todo al CD mediante `burncd`.

Esta tool forma parte de la base del sistema FreeBSD, por lo que suele funcionar sin problemas si tienes las suerte de que tu grabadora este entre las soportadas. Si no lo está, simpre te queda la opción de tratar de acceder al dispositivo a traves del subsistema SCSI. Para ello, hemos de recompilar el kernel y ańadir soporte ATAPI/CAM.

Una vez hecho esto, deberiamos poder utilizar el programa `cdrecord` para para quemar nuestros CDs.

##Grabando DVDs en FreeBSD:

Para trabajar con DVDs, utilizaremos `growisofs`.

Esta tool es en realidad un frontend a `mkisofs` pero además nos brinda la posibilidad de quemar directamente los DVDs. De esta manera, con `growisofs` podemos crear la imagen ISO y quemarla al DVD en un sólo paso. 

`growisofs` es parte del paquete `dvd+rw-tools`, y accede a la grabadora utilizando el subsistema SCSI. Así pues necesitaremos un kernel con soporte ATAPI/CAM.

En primer lugar, instalaremos las `dvd+rw-tools` en nuestros sistema:

    ::::Console
    cd /usr/ports/sysutils/dvd+rw-tools
    make install && make clean

Ahora necesitamos compilar un kernel con soporte ATAPI/CAM:

    ::::Console
    cd /usr/src/sys/i386/conf/
    cp GENERIC GENERIC_wtih_ATAPI_CAM

Editamos el fichero `GENERIC_wtih_ATAPI_CAM` y ańadimos esto:

    ::::Console
    device          atapicam        # ATAPI/CAM Support using the SCSI subsystem
    
    config GENERIC_wtih_ATAPI_CAM
    cd ../compile/GENERIC_wtih_ATAPI_CAM/
    make depend
    make
    make install

Ahora, tras rebotar deberiamos tener acceso a nuestra grabadora utilizando el subsistema SCSI:

Antes de rebotar vemos esto:

    ::::Console
    root@patxi:~# camcontrol devlist
    QUANTUM ATLAS10K2-TY184L DA40    at scbus0 target 0 lun 0 (pass0,da0)
    
    root@patxi:~# cdrecord --scanbus
    Cdrecord 2.00.3 (i386-unknown-freebsd5.3) Copyright (C) 1995-2002 Jg Schilling 
    Using libscg version 'schily-0.7'
            0,0,0     0) 'QUANTUM ' 'ATLAS10K2-TY184L' 'DA40' Disk
            0,1,0     1) *
            0,2,0     2) *
            0,3,0     3) *
            0,4,0     4) *
            0,5,0     5) *
            0,6,0     6) *
            0,7,0     7) *

Si todo va bien, tras reiniciar el sistema deberiamos ver algo asi como:

    ::::Console
    root@patxi:~# cdrecord --scanbus
    Cdrecord 2.00.3 (i386-unknown-freebsd5.3) Copyright (C) 1995-2002 Jg Schilling
    Using libscg version 'schily-0.7'
    scsibus0:
            0,0,0     0) 'QUANTUM ' 'ATLAS10K2-TY184L' 'DA40' Disk
            0,1,0     1) *
            0,2,0     2) *
            0,3,0     3) *
            0,4,0     4) *
            0,5,0     5) *
            0,6,0     6) *
            0,7,0     7) *
    scsibus1:
            1,0,0   100) 'HL-DT-ST' 'CD-RW GCE-8400B ' '1.02' Removable CD-ROM
            1,1,0   101) *
            1,2,0   102) *
            1,3,0   103) *
            1,4,0   104) *
            1,5,0   105) *
            1,6,0   106) *
            1,7,0   107) *

Bien! Ya tenemos soporte. Ahora sólo hemos de pinchar la grabadora de DVDs y ver si el sistema también es capaz de detectarla.

    ::::Console
    root@patxi:~# cdrecord --scanbus
    Cdrecord 2.00.3 (i386-unknown-freebsd5.3) Copyright (C) 1995-2002 Jg Schilling
    Using libscg version 'schily-0.7'
    scsibus0:
           0,0,0     0) 'QUANTUM ' 'ATLAS10K2-TY184L' 'DA40' Disk
           0,1,0     1) *
           0,2,0     2) *
           0,3,0     3) *
           0,4,0     4) *
           0,5,0     5) *
           0,6,0     6) *
           0,7,0     7) *
    scsibus1:
           1,0,0   100) 'HL-DT-ST' 'CD-RW GCE-8400B ' '1.02' Removable CD-ROM
           1,1,0   101) *
           1,2,0   102) *
           1,3,0   103) *
           1,4,0   104) *
           1,5,0   105) *
           1,6,0   106) *
           1,7,0   107) *

Bueno, parece que vamos por el buen camino. A ver si además de verlo somos capaces de leer y/o grabar algo.
En primer lugar hemos de saber a traves de qué dispositivo accederemos a la unidad. Para ello, el comando camcontrol puede sernos de utilidad:

    ::::Console
    root@patxi:~# camcontrol devlist
    QUANTUM ATLAS10K2-TY184L DA40    at scbus0 target 0 lun 0 (pass0,da0)
    HL-DT-ST DVDRAM GSA-4167B DL12   at scbus1 target 0 lun 0 (pass1,cd0)

Ahora ya lo sabemos (`/dev/cd0`) introducimos un DVD en la unidad y utilizando el siguiente comando veremos si somos capaces de reconocer el DVD que hemos introducido:

    ::::Console
    root@patxi:~# dvd+rw-mediainfo /dev/cd0
    INQUIRY:                [HL-DT-ST][DVDRAM GSA-4167B][DL12]
    GET [CURRENT] CONFIGURATION:
     Mounted Media:         10h, DVD-ROM
     Speed Descriptor#0:    02/404849 R@2.5x1385=3503KB/s W@6.1x1385=8467KB/s
     Speed Descriptor#1:    02/404849 R@2.5x1385=3503KB/s W@5.1x1385=7056KB/s
     Speed Descriptor#2:    02/404849 R@2.5x1385=3503KB/s W@4.1x1385=5645KB/s
     Speed Descriptor#3:    02/404849 R@2.5x1385=3503KB/s W@3.1x1385=4234KB/s
     Speed Descriptor#4:    02/404849 R@2.5x1385=3503KB/s W@2.0x1385=2822KB/s
     Speed Descriptor#5:    02/404849 R@2.5x1385=3503KB/s W@1.0x1385=1411KB/s
     Speed Descriptor#6:    02/404849 R@2.5x1385=3503KB/s W@0.5x1385=706KB/s
    READ DVD STRUCTURE[#0h]:
     Media Book Type:       01h, DVD-ROM book [revision 1]
     Legacy lead-out at:    2080080*2KB=4260003840
    READ DISC INFORMATION:
     Disc status:           complete
     Number of Sessions:    1
     State of Last Session: complete
     Number of Tracks:      1
    READ TRACK INFORMATION[#1]:
     Track State:           complete
     Track Start Address:   0*2KB
     Free Blocks:           0*2KB
     Track Size:            2080080*2KB
    FABRICATED TOC:
     Track#1  :             14@0
     Track#AA :             14@2080080
     Multi-session Info:    #1@0
    READ CAPACITY:          2080080*2048=4260003840

Vale, ahora metemos el primer DVD que tengamos a mano e intentaremos montarlo:

    ::::Console
    root@patxi:~# mount_cd9660 /dev/cd0 /mnt
    root@patxi:~# ls /mnt

Bueno, la prueba final es tratar de grabar algo en un DVD:

    ::::Console
    root@patxi:~# growisofs -dvd-compat -Z /dev/cd0 -J -R /home/melmak/backup.tar
    Executing '/usr/local/bin/mkisofs -J -R /home/melmak/backup.tar | builtin_dd of=/dev/pass1 obs=32k seek=0'
    /dev/pass1: "Current Write Speed" is 8.2x1385KBps.
      1.13% done, estimate finish Thu Feb  2 23:32:49 2006
      2.27% done, estimate finish Thu Feb  2 23:17:23 2006
      3.40% done, estimate finish Thu Feb  2 23:12:15 2006
      .
      .
      .
      98.48% done, estimate finish Thu Feb  2 23:02:22 2006
      99.62% done, estimate finish Thu Feb  2 23:02:21 2006
    Total translation table size: 0
    Total rockridge attributes bytes: 251
    Total directory bytes: 0
    Path table size(bytes): 10
    Max brk space used bac4
    441712 extents written (862 Mb)
    builtin_dd: 441712*2KB out @ average 6.5x1385KBps
    /dev/pass1: flushing cache
    /dev/pass1: updating RMA
    /dev/pass1: closing disc

Ahora podemos montar el DVD para comprobar que los datos se han grabado correctamente.

En el caso de utilizar un DVD regrabable, antes de quemarlo deberemos formatearlo. Pata ello utilizaremos la herramienta dvd+rw-format:

    ::::Console
    dvd+rw-format -blank /dev/cd0

Esto es todo. Os dejo unas fotos de todo el proceso [aquí](http://nomeriasdeti.no-ip.com/index.php?top_tab=2&section_type=3&num=&task=view&id_album=24).

Más info en el Freebsd Handbook:

[Creating and Using Optical Media (CDs)](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/creating-cds.html)

[Creating and Using Optical Media (DVDs)](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/creating-dvds.html)
