Title: Convertir videos al formato utilizado por el movil con ffmpeg
Date: 2006-12-18 17:24:49
Category: Spanish
Tags: video, encoder, ffmpeg
Author: frommelmak

La mayoría de teléfonos móviles de última generación del mercado son capaces de manejar ficheros multimedia.
Para hacerlo algunos utilizan ficheros [3GP](http://en.wikipedia.org/wiki/3GP) que no es un formato de vídeo en si mismo, sino un formato de contenedor que permite albergar pistas de audio ([AMR-NB](http://en.wikipedia.org/wiki/Adaptive_Multi-Rate)/[AAC-LC](http://en.wikipedia.org/wiki/Advanced_Audio_Coding)) y vídeo ([MPEG-4](http://en.wikipedia.org/wiki/MPEG-4_Part_2) , [H.263](http://en.wikipedia.org/wiki/H.263) ó [H.264](http://en.wikipedia.org/wiki/H.264)).

Hoy he estado experimentando con ffmpeg y he conseguido crear ficheros 3GP que he podido reproducir sin problemas con mi [Sony Ericsson k610i](http://www.sonyericsson.com/spg.jsp?cc=es&lc=es&ver=4000&template=pip1&zone=pp&pid=10389). La calidad, tanto del vídeo como del sonido son más que aceptables, y no es descabellado pasar un capitulo de tu serie favorita al teléfono para disfrutarlo durante un viaje o mientras esperas en la consulta del médico por ejemplo.

Bueno, dejo aquí el comando por si me veo en la necesidad de volver a utilizarlo algún día:

    :::bash
    ffmpeg -i prodigy90_med.mpg -s qcif -acodec aac -vcodec mpeg4 ADG3.3gp

Dónde: `-i` (Fichero de entrada), `-s` (size qcif 176x144), `-acodec` (audio codec AAC), `-vcodec` (video codec MP4), `ADG3.3gp` (Fichero de salida)
