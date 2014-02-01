Title: Vodafone MC950D en Opensuse 11.1
Date: 2009-10-13 20:55:48
Category: Spanish
Tags: vodafone, opensus, modem, adsl
Author: frommelmak

Notas para instalar Modem **USB MC950D de Vodafone** en Opensuse 11.1

  * Disponer del dispositovo USB Ovation MC950D de Vodafone
  * Instalar [Vodafone Mobile Connect Card driver for Linux](https://forge.betavine.net/projects/vodafonemobilec) ([INSTALL_OPENSUSE111.TXT](https://forge.betavine.net/frs/download.php/537/INSTALL_OPENSUSE111.TXT)) para Opensuse.

Llegados a este punto, si al lanzar `vodafone-mobile-connect-card-driver-for-linux` no te detecta ningun dispositivo, probablemente sea porque te está detectando la llave USB como dispositivo de almacenamiento. En este caso, un `lsusb` te retorna esto:

    :::console
    Bus 004 Device 005: ID 1410:5010 Novatel Wireless

Para conmutar dicho dispositivo a modo Modem has de ejecutar este comando:

    :::console
    vmc-usb_modeswitch-eject.sh 1410 5010

Tras lo cual un `lsusb` mostrará:

    :::console
    Bus 004 Device 006: ID 1410:4400 Novatel Wireless

Para que udev se encargue de hacer este switch automáticamente, es necesario modificar la regla udev para el dispositivo Novatel (`/etc/udev/rules.d/45-vmc-novatel.rules`)

Cambiamos:

    :::console
    ACTION==add, \
     ATTRS{idVendor}==1410, ATTRS{idProduct}==5010, \
     RUN:=/bin/eject %k

Por esto otro:

    :::console
    ACTION==add, \
     ATTRS{idVendor}==1410, ATTRS{idProduct}==5010, \
     RUN:=/usr/sbin/vmc-usb_modeswitch-eject.sh 1410 5010

Ahora al arrancar aparecerá el dispositivo, la ventana para introducir el PIN, etc.
