Title: udev network device en Ubuntu Hardy sobre VMWare
Date: 2010-03-22 15:47:00
Category: Spanish
Tags: udev, ubuntu, vmware
Author: frommelmak

Cuando clonamos una máquina *Ubuntu Hardy* para correr otra instancia en VMWare, `udev` detecta una nueva MAC y crea otra interfaz de red.

Esto provoca que cada vez que restauramos una máquina basada en *Ubuntu Hardy*, el interfaz de red se incremente: eth0, eth1,... etc.

*Debian 5.0* (*lenny*) soluciona esto añadiendo esta línea en el fichero `/etc/udev/rules.d/75-persistent-net-generator.rules` (linea 34):

    :::console
    ENV{MATCHADDR}==00:0c:29:*|00:50:56:*, ENV{MATCHADDR}=

Este cambio es aplicable también en *Ubunty Hardy* y es la manera más sencilla de eliminar esta problematica.
