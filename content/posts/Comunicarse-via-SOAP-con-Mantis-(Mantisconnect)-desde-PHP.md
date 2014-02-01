Title: Comunicarse via SOAP con Mantis (Mantisconnect) desde PHP
Date: 2008-11-26 22:15:54
Category: Spanish
Tags: soap, mantis, php
Author: frommelmak

No he encontrado muchos ejemplos (por no decir ninguno) de como llamar a los mtodos SOAP de Mantis desde PHP, así que aquí dejo unos ejemplitos.

Lo primero de todo es saber que tras la instalación de Mantis, podemos obtener el WSDL bajo esta URL: `http://logquesea/api/soap/mantisconnect.php?wsdl`

Adems del WSDL, es interesante saber que hay una ayuda para humanos acerca de los métodos disponibles. Se puede obtener omitiendo `?wsdl` en la llamada anterior.

A continuación os dejo los ejemplos sobre como llamar a algunos de estos métodos desde PHP.

Obtener la versin de Mantis:

    :::php
    <?php
    
    $client = new SoapClient(http://mantis/api/soap/mantisconnect.php?wsdl);print($client-mc_version());
    ?>

Obtener array con diferentes estadisticas de Mantis


    :::php
    <?php
    
    $client = new SoapClient(http://mantis/api/soap/mantisconnect.php?wsdl);$username=usuario;$password=contrasea;print_r($client-mc_enum_status($username, $password));

    ?>

Aadir una nueva issue a Mantis

    :::php
    <?php
    
    $client = new SoapClient(http://mantis/api/soap/mantisconnect.php?wsdl);
    
    $username=usuario;
    $password=constrasea;
    
    $issue=array (project = array (id = , name = SOAP Test),
                  category = General,
                  priority = array (id = , name = ),
                  severity = array (id = , name = ),
                  status = array (id = , name = ),
                  reproducibility = array (id = , name = ),
                  resolution = array (id = , name = ),
                  projection = array (id = , name = ),
                  eta = array (id = , name = ),
                  view_state = array (id = , name = ),
                  summary  = Test SOAP,
                  description = This is just a new issue added using SOAP);$client-mc_issue_add($username, $password, $issue);
    ?>


**Nota**: Aquí lo importante es saber que los tipos de datos complejos del array (priority, severity, status, ) han de estar definidos pese a ser opcionales. De lo contrario el servidor soap da un error y no procesa la llamada.

