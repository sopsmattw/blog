Title: Unificar el contenido de varios wikis en uno solo
Date: 2007-07-12 22:34:00
Category: Spanish
Tags: mediawiki
Author: frommelmak

El objetivo de esta entrada en el blog es describir el método que he seguido para fusionar varios Wikis en uno sólo. La poca documentación que he encontrado al respecto, me ha animado a explicar mis experiencias al respecto en este mini-howto.

El escenario inicial es el siguiente: Disponemos de varios wikis basados en diferentes versiones de MediaWiki. Uno utiliza *MediaWiki 1.3.9* (wiki2 en este ejemplo), y el resto *MediaWiki 1.5.8* (wiki1 en este ejemplo). El contenido de todos los wikies será migrado a un nuevo wiki basado en *MediaWiki 1.6.10*.

Empezamos!

##Descripción general del proceso.

A grandes rasgos, el proceso consiste en volcar por un lado el contenido de los wikis (páginas) a un fichero XML, y por el otro las images y demás ficheros adjuntos. Para lo primero utilizaremos las herramientas facilitadas por MediaWiki y para lo segundo bastará con copiar el contenido del directorio images y extraer unas tablas de la base de datos.

Antes de importar los XML de cada wiki, procesaremos los ficheros XML para incluir una etiqueta de categoria a cada página. Si bien esto es opcional, el proposito es no perder la pista del origen de cada una de las páginas. De esta manera, cada una de las páginas de los wikis que importemos estarán agrupadas bajo una categoria en el wiki de destino.

##Exportar el contenido de los wikis:

Tanto en la versión 1.3.9 como 1.5.8 de MediaWiki es posible exportar el contenido completo del wiki a un fichero de texto XML. La idea es que luego este fichero pueda ser importado en el wiki de destino.

Si bien es posible exportar e importar el contenido del wiki via web, es recomendable hacerlo mediante el script PHP que viene con MediaWiki siempre que sea posible.  Por qué ? Bueno, el motivo principal es porque si el contenido del wiki es muy extenso, probablemente los settings del fichero `php.ini` no sean suficiente generoros como para realizar el *import* con éxito. Esto es especialmente cierto cuando además el XML generado incluye las diferentes revisiones de cada página, ya que entos casos el tamao del XML puede ser considerable.

### En MediaWiki 1.5.8

En esta versión no hay ningun secreto, tan sólo será necesario ejecutar el script `dumpBackup.php` que se encuentra en la carpeta maintenance.

Antes de ejecutar los scripts de la carpeta maintenance deberemos editar el fichero `AdminSettings.php` con el un usuario y password con permisos sobre la base de datos MySQL del wiki.

    :::console
    cd /your_wiki_path/maintenance
    cp AdminSettings.sample AdminSettings.php
    vi AdminSettings.php
    php dumpBackup.php --full  wiki-backup.xml

Para importar las imágenes, necesitaremos además extraer el contenido de las tablas: image, imagelinks y oldimage.

    :::console
    mysqldump -u root -p wikidatabase image  wiki1-image.sql
    mysqldump -u root -p wikidatabase imagelinks  wiki1-imagelinks.sql
    mysqldump -u root -p wikidatabase oldimage  wiki1-oldimage.sql

Deberemos repetir estos pasos para cada uno de los wikis con versión 1.5.8.

###En MediaWiki 1.3.9

En esta versión de MediaWiki no existe el script `dumpBackup.php`, por lo que nos veremos obligados a extraer el XML via web, lo cual es un poco ms engorroso.

En primer lugar necesitamos la lista de páginas que queremos exportar, ya que deberemos introducirla a lo largo del proceso.

Si nuestro wiki tiene unas pocas páginas, lo mas rápido es ir a: *Special pages -> All pages* y hacer un cut &  paste. En cambio, si nuestro wiki dispone de muchas páginas, estas aparecern ordenadas en columnas y la tarea de copiar y pegar se tornará muy tediosa.

La solucin más rapida y segura que he encontrado es esta:

Vamos a:  *Special pages -> All pages*

Utilizaremos entonces la opción *view-source* (de nuestro navegador), seleccionareos todo el código de la página y lo copiaremos a un fichero llamado `all_pages.txt`.

Luego ejecutamos sobre ese fichero este comando y listos:

    :::console
    sed -n '/-- start content --/,/-- end content --/p' all_pages.txt |sed 's/\/td/\n/g'| sed -e 's#[^]*##g'| sed '/^$/d' |less

Ahora ya podemos ir a: *Special pages -> Export pages*

Introducimos la lista de páginas a exportar (obtenida anteriormente) teniendo cuidado de desmarcar además la casilla:

*Include only the current revision, not de full history*

Finalmente le damos a: *Submit query*  y obtendreos en el browser el cdigo XML con todo el contenido de nuestro wiki.

Ya sólo hemos de copiar el código y pegarlo en un fichero de texto: `wiki2-backup.xml`, por ejemplo.

De igual modo que para la versión 1.5.8, de cara a exportar las imgenes necesitaremos también el contenido de las tabas: image, imagelinks y oldimage.

    :::console
    mysqldump -u root -p wikidatabase image  wiki2-image.sql
    mysqldump -u root -p wikidatabase imagelinks  wiki2-imagelinks.sql
    mysqldump -u root -p wikidatabase oldimage  wiki2-oldimage.sql

##Importar el contenido de los wikies:

Como este manual no pretende ser una guia de instalacin y configuracin de MediaWiki, voy a asumir que ya tenemos instalado y configurado el wiki de destino (recordemos, MediaWiki 1.6.10).

Llegados a este punto, lo que haremos ser ir importando el contenido (`ficheros.xml`) y las imagenes y/o archivos adjuntos que tubieran nuestros wikis de origen (ficheros + tablas de imagenes).

En primer lugar importaremos el contenido del wiki con la versin ms vieja (MediaWiki 1.3.9), más adelante veremos por qué.

###Importar el XML generado por MediaWiki 1.3.9

Dado que necesitaremos ejecutar varios de los scripts de la carpeta maintenance de nuestro wiki de destino, antes de nada, deberemos editar el `ficheroAdminSettings.php` para que estos scripts puedan acceder a la base de datos.

    ::::console
    cp AdminSettings.sample AdminSettings.php
    vi AdminSettings.php

Edit the file `AdminSettings.php` with the mysql user/password)

Ahora ya podriamos importar el contenido del wiki con el script `importDump.php`, si bien antes de hacerlo podrá interesaros, como en mi caso, añadir una etiqueta de categoria a cada una de las páginas del wiki. Esto nos permitir poder separar la informacin de cada uno de los wikis en función de su procedencia. Así todas las páginas de la categoria wiki2 s que vienen del wiki2.

Para hacer esto, podeis utilizar un script como el siguiente:

    :::console
    #!/bin/bash
    
    IFILE=$1
    OFILE=P_$1
    CATEGORY_STRING=$2
    
    echo Output file is: $OFILE
    > $OFILE
    
    UPC=FALSE
    PAGES=0
    
    while read LINE
    do
    echo $LINE | grep title.*/title | grep -qv -e MediaWiki:.* -e MediaWiki talk:.* -e Image:.* -e Image talk:.* -e Talk:.* -e User:.* -e User talk:.* -e Category:.* -e Category talk:.* -e Template:.* -e Template talk:.*  UCP='TRUE'  let PAGES=$PAGES+1
    echo $LINE | grep -q '/text'
    TEXT_TAG=$?
    if [[ $UCP = TRUE  $TEXT_TAG -eq 0 ]]
    then
    echo -n .
    echo $LINE | sed s/\/text/$CATEGORY_STRING\/text/g  $OFILE
    else echo $LINE  $OFILE  echo $LINE | grep -q '/page'  UCP=FALSE
    fi
    done  $IFILE
    echo 
    
    echo Processed pages: $PAGES
    
    
    echo Done!


Para procesar el XML, llamaremos al script con algo parecido a esto:

    :::console
    ./xwp.sh wiki2-backup.xml [[Category:wiki2]]

Y finalmente importaremos el contenido del fichero resultante (P_wiki2-backup.xml) a nuestro nuevo wiki:

    :::console
    php maintenance/importDump.php P_wiki2-backup.xml

Una vez importado el fichero XML al nuevo wiki tendremos a nuestra disposicin todas y cada una de las pginas que contenia el viejo wiki.

Podemos listarlas todas si vamos a:

*Special pages->All pages*

Del mismo modo, si nuestro viejo wiki disponía de categorias, estas aparecerán bajo: *Special pages->Categories*, después de ejecutar este script.

    :::console
    php maintenance/refreshLinks.php

Lamentablemente, si importamos desde un wiki basado en MediaWiki 1.3.9, las pginas que describen las categorias, asi como los templates no se importan correctamente y hay que importarlos via cut & paste.

## Importar las imagenes y documentos adjuntos desde MediaWiki 1.3.9

La sincronización de las imágenes y los ficheros adjuntos se compone de 3 pasos.

  * Copia de los ficheros
  * Importar las tablas image de la base de datos (implica borrar las actuales)
  * Actualizar las tablas de imagenes a las de la version 1.6.10

Llevamos a la consola, quedaría asi:

    :::console
    cd /your_wiki_path/images
    rsync -avz wiki2host:/path/to/old/wiki2/images/ .
    chown -R apache:apache *
    cd /path/to/your/database_files
    mysql -u root -p new_wikidatabase  wiki2-image.sql
    mysql -u root -p new_wikidatabase  wiki2-imagelinks.sql
    mysql -u root -p new_wikidatabase  wiki2-oldimage.sql

Dado que no hemos modificado los ficheros SQL obtenidos mediante el volcado con `mysqldump`, las tablas actuales han sido substituidas por las viejas. Estas tablas no son exactamente igual en la version 1.3.9 y la 1.6.10 por lo que deberemos añadir los nuevos campos que se introducen a partir de la versin 1.5.8.

Afortunadamente, disponemos de un script que actualiza esta tabla sin eliminar su contenido.

    :::console
    php maintenance/update.php
    php rebuildImages.php

Y este es básicamente el motivo por el cual hemos elegido el wiki movido por MediaWiki 1.3.9 en primer lugar.

##Importar el XML generado por MediaWiki 1.5.8

En este punto, apenas hay diferencias con la versin 1.3.9 y el proceso es prácticamente idéntico. Es decir: procesamos el XML antes de importarlo y luego importamos las imágenes y documentos adjuntos.

La única diferencia en este punto es que si importamos el contenido de un XML generado con la versin 1.5.8 de MediaWiki, es que las pginas de descripción de las categorias y los templates en esta ocasión, se crean correctamente.

    :::console
    cd /your_wiki_path
    ./xwp.sh wiki1-backup.xml [[Category:wiki1]]
    cd /your_wiki_path/maintenance 
    php importDump.php P_wiki1-backup.xml


##Importar las imagenes y documentos adjuntos desde MediaWiki 1.5.8

De nuevo en esencia la idea es la misma, por un lado copiaremos los ficheros de imagenes y documentos adjuntos para posteriormente reflejar estos en la base de datos. Si bien en esta ocasión, los campos de las tablas son idénticos para ambas versiones de MediaWiki, deberemos editar los ficheros SQL antes de importarlos.

Lo que haremos es borrar la sentencias `CREATE TABLE` que crean las tablas image, imagelinks y oldimage. Si no lo hacemos, perderemos que habiamos importado del anterior wiki.

    :::console
    cd /your_wiki_path/images
    rsync -avz wiki1host:/path/to/old/wiki1/images/ .
    chown -R apache:apache *

Ahora, deberemos editar los ficheros SQL borrando las sentencias `CREATE TABLE` que preceden a los `INSERT` de cada tabla. En otras palabras, borraremos las lineas que preceden a cada:

    :::console
    --
    -- Dumping data for table
    --

**Nota**: En mi caso también he tenido que eliminar la siguiente línea de cada archivo. Sino, el `import` me daba un warning.

    :::console
    /*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

    :::console
    vi wiki1-image.sql
    vi wiki1-imagelinks.sql
    vi wiki1-oldimage.sql
    mysql -u root -p new_wikidatabase  wiki1-image.sql
    mysql -u root -p new_wikidatabase  wiki1-imagelinks.sql
    mysql -u root -p new_wikidatabase  wiki1-oldimage.sql
    cd /your_wiki_path/maintenance
    php refreshLinks.php

###Retoques finales:

Una vez hayamos repetido esto para cada uno de los wikis a fusionar, nos queda ejecutar estos scritps:

    :::console
    php maintenance/initStats.php
    php maintenance/updateSearchIndex.php
    php maintenance/rebuildtextindex.php

El primero de ellos pondrá al día la página de estadisticas *Special pages->Stats*, mientras que los dos últimos rehacen los indices que permiten hacer búsquedas en nuestro nuevo, enorme y flamante wiki.
