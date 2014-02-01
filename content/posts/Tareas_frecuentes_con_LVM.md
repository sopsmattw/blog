Title: Tareas frecuentes con LVM
Date: 2011-02-15 17:25:01
Category: Spanish
Tags: lvm
Author: frommelmak

Un par de apuntes rápidos sobre LVM:

Juntar varios discos o particiones en un único volumen lógico:

    :::Console
    pvcreate /dev/sdb /dev/sdc
    vgcreate -s 16M data /dev/sdb /dev/sdc
    vgdisplay
    lvcreate -l 25600 -n storage data
    mkfs.ext3 /dev/data/storage

Expandir en 100GB un LV y el filesystem que contiene.

    :::console
    lvextend -L+100G /dev/mapper/loquesea
     umount /del/putno/de/montaje
     e2fsck -f /dev/mapper/loquesea
     resize2fs /dev/mapper/loquesea
     mount -a
