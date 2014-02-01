Title: Convertir book drupal (UTF-8) a PDF mediante htmldoc
Date: 2009-11-26 09:40:04
Category: Spanish
Tags: pdf, htmldoc, utf8
Author: frommelmak

Descargamos la versión *printer friendly version* del book

    :::console
    wget http://www.youdomain.com/book/export/html/xxx -O web.html

Dado que `htmldoc` no soporta `--charset utf-8` (en las versiones estables  1.9.x), deberemos convertir el `html` a `iso-8859-1` o de lo contrario no veremos bien algunos caracteres.

    :::console
    iconv -f UTF-8 -t ISO-8859-1 web.html  web-iso-8859-1.html

Finalmente utilizamos `htmldoc` para crear el PDF

    :::console
    htmldoc -f web.pdf --webpage web-iso-8859-1.html
