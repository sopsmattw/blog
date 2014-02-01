Title: Utilidad para modificar ficheros SWF en Linux/Windows
Date: 2009-12-01 00:11:32
Category: Spanish
Tags: swf
Author: frommelmak

Para poder modificar un fichero SWF es necesario desensamblar el binario SWF, editar el fichero de texto resultante y volver a ensamblar. Mediante la utilidad [Flasm](http://www.nowrap.de/flasm.html) es posible realizar esto de forma sencilla. Ejemplo:

    :::console
    ./flame -d fichero.swf  fichero.flm

Editamos el fichero `.flm` mediante un editor de textos y volvemos a generar el fichero swf.

    :::console
    ./flame -a fichero.flm

De esta manera es posible actualizar por ejemplo los enlaces del típico menú en flash.
