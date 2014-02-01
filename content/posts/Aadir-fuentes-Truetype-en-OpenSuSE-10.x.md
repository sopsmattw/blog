Title: Añadir fuentes Truetype en OpenSuSE 10.x
Date: 2006-11-17 22:06:34
Category: Spanish
Tags: fonts, truetype
Author: frommelmak

Rara vez añado fuentes al sistema por lo que siempre que he de hacerlo he de googlear un rato para recordar cómo diablos se hacía. La teoria es la misma para todas las distros, pero algunas de ellas incorporan scripts para facilitarnos la vida. Sirva esta noticia como recordatorio de como se hace en OpenSuSE 10.x (al menos yo lo he hecho así).

Copiar las fuentes en al directorio de fuentes del sistema:

    :::console
    cp fuente.ttf /usr/X11R6/lib/X11/fonts/truetype 

Actualizar los ficheros `fonts.dir` y `fonts`.

    :::console
    scalefonts-config -f 
