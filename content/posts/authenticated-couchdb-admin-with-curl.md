Title: Authenticated Couchdb admin with Curl
Date: 2011-01-25 23:35:01
Category: Spanish
Tags: couchdb, curl
Author: frommelmak

Los principales parámetros de configuración de Couchdb se puede consultar y administrar mediante la interfaz web de Couchdb. No obstante hay algunas opciones interesantes que no están disponibles en dicha interfaz. Para cambiarlas es necesario modificar los valores directamente mediante un PUT HTTP. Para ello utilizaremos `curl`:

Por ejemplo, cambiar el nmero de revisiones que guardaremos de un documento sería:

    :::console
    curl -X PUT -d 500 http://localhost:5984/document_db/_revs_limit 

Vale, pero cmo lo hacemos si hemos protegido el acceso a couchdb con un usuario y un password ?

    :::console
    curl -X PUT -d 500 http://user:passwd@localhost:5984/document_db/_revs_limit

Sencillo no ?
