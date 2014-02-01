Title: Error de autenticación en Samba (RHEL4.6 AS x86_64)
Date: 2008-02-25 10:37:57
Category: Spanish
Tags: samba, pam
Author: frommelmak
 
Tras perder la tarde del viernes configurando un simple share en samba, por fin he dado con el problema.

El error se producía al intentar mapear el share desde Windows. Tras poner usuario y password obtenia este mensaje:

    :::console
    A device attached to the system is not functioning.

El problema es que el fichero del módulo de autenticación PAM, hacía referencia a las librerias de 32bits en lugar de llamar a las de 64bits. Para solucionarlo, tan solo has de referenciar a la libreria en cuestión, sin poner el path absoluto. De esta manera es el sistema el que selecciona las librerias que considera necesario.

`/etc/pam.d/samba` **Incorrecto**.

    :::console
    /etc/pam.d/samba [Incorrecto]
    auth required /lib/security/pam_stack.so service=system-auth
    account required /lib/security/pam_stack.so service=system-auth

`/etc/pam.d/samba` **Correcto**:

    :::console
    /etc/pam.d/samba [Correcto]
    auth required pam_stack.so service=system-auth
    account required pam_stack.so service=system-auth

Desconozco si es un error reportado, pero en la web de Red Hat no he encontrado ninguna referencia.

Más [info](http://www.linuxquestions.org/questions/linux-server-73/swat-root-cant-log-in-604135/)

