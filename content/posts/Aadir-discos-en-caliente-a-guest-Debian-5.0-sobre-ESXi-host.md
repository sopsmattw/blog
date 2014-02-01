Title: Añadir discos en caliente a guest Debian 5.0 sobre ESXi host
Date: 2010-04-21 13:36:51
Category: Spanish 
Tags: esx, vmware
Author: frommelmak

En primer lugar añadimos un nuevo disco al guest desde el host mediante vSphere.

El disco aun no se ve en el guest:

    ::::Console
    guest666@root:# cat /proc/scsi/scsi 
    Attached devices: 
    Host: scsi0 Channel: 00 Id: 01 Lun: 00 
     Vendor: VMware Model: Virtual disk Rev: 1.0 
     Type: Direct-Access ANSI SCSI revision: 02

Por lo que un `sfdisk -l` no lo lista tampoco:

    ::::Console
    guest666@root:# sfdisk -l
    
    Disk /dev/sda: 1305 cylinders, 255 heads, 63 sectors/track
    Units = cylinders of 8225280 bytes, blocks of 1024 bytes, counting from 0
    
     Device Boot Start End #cyls #blocks Id System
    /dev/sda1 * 0+ 1178 1179- 9470286 83 Linux 
    /dev/sda2 1179 1304 126 1012095 5 Extended
    /dev/sda3 0 - 0 0 0 Empty 
    /dev/sda4 0 - 0 0 0 Empty 
    /dev/sda5 1179+ 1304 126- 1012063+ 82 Linux swap / Solaris

Lo que hay que hacer es forzar un re-scan de los dispositivos scsi. Para esto lo normal sería reiniciar, sin embargo podemos utilizar `scsiadd` en su lugar (`apt-get install scsiadd` si no lo tenemos).

    ::::Console
    guest666@root:~# scsiadd -s
    Attached devices:
    Host: scsi0 Channel: 00 Id: 01 Lun: 00
     Vendor: VMware Model: Virtual disk Rev: 1.0
     Type: Direct-Access ANSI SCSI revision: 02
    Host: scsi0 Channel: 00 Id: 00 Lun: 00
     Vendor: VMware Model: Virtual disk Rev: 1.0
     Type: Direct-Access ANSI SCSI revision: 02

Tras esto, el disco ya aparece en `/proc/scsi/scsi` y mediante `sfdisk -l`. Ahora ya sólo queda particionar y formatear.

*IMPORTANTE!!!* Tras trastear con `scsiadd`, es recomendable prestar especial atención al pórximo reeboot del sistema. En mi caso, no encontraba el disco de arranque **operative system not found**. Al parecer, tras reiniciar el identificador SCSI, del último disco añadido era el 0 en lugar del 2. Para solventarlo, hay que cambiar los ID SCSI desde vmware y habilitar la opción de entrar en la BIOS para conseguir arrancar el sistema.
