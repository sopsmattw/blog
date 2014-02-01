Title: Freecom DVB-T USB Stick en SuSE 10.0
Date: 2006-01-03 01:27:25
Category: Spanish
Tags: Freecom, dvb, suse
Author: frommelmak

Hoy tocaba sesión de compras para reyes, y he aprovechado para autoregalarme un pequeńo gadget. Se trata de una llave USB 2.0 para ver los canales de la [Television Digital Terrestre (TDT)](http://www.tdt.es/).

La verdad es que no he mirado muchos modelos antes de decidirme por este. Sólo un par de ellos, una [Hauppauge WinTV HRV 900](http://www.hauppauge.co.uk/pages/products/data_hvr900.html) (compatible con la TV analogica) de tipo pendrive que se iba a los 120€, y una [AVerMedia AVerTV USB 2.0](http://www.avermedia.com/cgi-bin/products_tvtuner_avertvusb2.asp?show=2) un poco aparatosa ya que era un módulo externo.

Finalmente, el modelo por el que me he decidido ha sido el que tenia en mente. Una [Freecom DVB-T USB Stick](http://www.freecom.com/ecProduct_detail.asp?ID=2234&nr=25451&prodn=DVB%2DT+USB+Stick), que me ha salido por 62,90€ (sin buscar demasiado)

Bueno, pues a continuación os explico mis experiencias al pinchar el receptor en una SuSE 10.0.

Al pinchar el receptor, simplemente no pasa nada. Se cargan unos cuantos modulos en el kernel pero el dispositivo parece estar muerto, ya que el led del que dispone ni se enciende.

Si optas por la via fácil y lo intentas via YaST, tampoco esperes mucho más, ya que la Freecom no aparece entre los dispositivos TV Card soportados.

Bueno, que no cunda el pánico. Tras googlear durante unos 2 minutos, llegarás a la web de referencia para este tipo de dispositivos que es esta:
 
[www.linuxtv.org](www.linuxtv.org)

Dentro de esta web encontrarás el enlace al wiki que concentra todo el desarrollo de dispositivos **Digital Video Broadcasting - Terrestrial (DVB-T)** como el que acabo de adquirir.

En dicho wiki, encontraremos una sección reservada a los dispositivos USB:

[DVB/ATSC USB boxes sorted by driver](http://www.linuxtv.org/wiki/index.php/DVB_USB)

Y allí, en la sección  WideView/Yakumo/Hama/Typhoon/Yuan Boxes and Pens encontramos la primera referencia al receptor de Freecom.
Nos informan que nuestro dispositivo tan sólo necesita de estos módulos para funcionar:

    ::::Console   
    dvb-usb.ko
    dvb-usb-dtt200u.ko
   
Y lo más importate, se nos informa del firmware que es capaz de controlar nuestro dispositivo. Es este fichero:

`dvb-usb-wt220u-01.fw`

Disponible [aquí](http://www.linuxtv.org/downloads/firmware/) y que deberemos copiar a `/lib/firmware`

Bueno, tras esto, si volvemos a pinchar el receptor USB, veremos que la lucecita del mismo ya muestra actividad, y si damos un vistazo a los módulos que carga el sistema veremos algo como esto:

    ::::Console
    melmak@super8:~> lsmod |grep dvb
    dvb_usb_dtt200u         8580  0
    dvb_usb                17928  1 dvb_usb_dtt200u
    dvb_core               77480  1 dvb_usb
    dvb_pll                 9348  1 dvb_usb
    i2c_core               20368  2 dvb_usb,i2c_i801
    firmware_class          9856  3 dvb_usb,pcmcia,ipw2200
    usbcore               112512  6 dvb_usb_dtt200u,dvb_usb,usbhid,ehci_hcd,uhci_hcd


Genial, ahora ya estamos en condiciones de utilizar algun software que nos permita ver las emisiones DVB-T.

Bueno, mis primeras pruebas han sido con Kaffeine. Al principio he tenido algunos problemas, ya que he tenido que instalar algunos paquetes adicionales de Xine via YaST, pero despues de esto, todo ha funcionado perfectamente salvo un pequeńo detalle: con la antena que se suministra no soy capaz de pillar absolutamente nada!!!. Con la antena comunitaria, los resultados han sido bastante mejores, ya que veo los 4 canales de TV3 (TV3, 33, 3/24 y 300) que se ven increiblemente nitidos.

Tras consultar mi zona en la web [www.tdt.es](http://www.tdt.es/) veo que en principio debería poder ver todos los canales desde el centro de emision de collserola: 21 Nacionales y 4 Autonomicos, pero solo soy capaz de ver los Autonomicos.

Bueno, por hoy esto es todo. Os dejo [aquí](http://nomeriasdeti.no-ip.com/index.php?top_tab=2&section_type=3&num=&task=view&id_album=22) unas fotos de todo el proceso.
