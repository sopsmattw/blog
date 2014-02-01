Title: MidpSSH cliente Java de SSH para el movil
Date: 2006-12-01 23:47:01
Category: Spanish
Tags: ssh, terminal, phone
Author: frommelmak

No sé muy bien cómo, ayer fui a parar a la web de [MidpSSH](http://www.xk72.com/midpssh), un cliente de SSH y Telnet para teléfonos móviles compatibles con Java MIDP 1.0 / 2.0 (J2ME) licenciado bajo GPL.

Lo he probado en mi [Sony Ericson k610i](http://www.sonyericsson.com/spg.jsp?cc=es&lc=es&ver=4000&template=pip1&zone=pp&pid=10389) y una tarifa estándar (Amena/Orange) y la verdad es que funciona a las mil maravillas. La instalación no tiene ningún misterio, sólo hay que descargar el fichero [`midpssh-full.jar`](http://www.xk72.com/midpssh/release/midpssh-full.jar) (o alguna de las [versiones](http://www.xk72.com/midpssh/download.php) reducidas) y copiarlo al teléfono utilizando el cable suministrado con el terminal u otro medio (bluetooth, web...).

Una vez allí, al seleccionar el fichero nos dar la opción de instalarlo en el teléfono. Lo siguiente es crear una *session* al mas puro estilo *PuTTY* (host + protocolo + user y password). 
A mi me ha dado algunos problemas al principio, ya que no tenía correctamente configurado el Java para que accediera correctamente a Internet, lo que provocaba un mensaje de error poco clarificador `write:`.

Tras trastear un rato he dado con la solución, que no es otra que configurar correctamente los ajustes Java para que las aplicaciones puedan conectar a Internet.

Ajustes -> Conectividad -> Ajustes de Internet -> Ajustes de Java 

Y cambiamos 'Amena' por 'Amena Internet'.

Bueno ahora sólo quedaria el tipico screenshot, pero no tengo por aqui más que la cámara del  propio movil, asi que lo dejo para otro dia.
