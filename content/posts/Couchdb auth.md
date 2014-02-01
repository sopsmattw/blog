Title: Couchdb auth
Date: 2010-11-09 18:21:58
Category: Spanish
Tags: couchdb
Author: frommelmak

Ojito con la autenticacin en Couchdb 0.11.0. Si la queremos deshabilitar, haremos esto:

    :::console
    #[admins]

NO ESTO!!!

    :::console
    #[admins]
    #user = -hashedlalkasdlfk....

Lo segundo hace que al arrancar couchdb de un error que hace que couchdb muera. Al rato se reinicia automaticamente (esto lo hace couchdb de saque) *respawn*. Por lo visto tras intentarlo mil veces lo deja estar. El error sólo se ve si llamamos al script de arranque en `bin` de couchdb directamente (no al de `/etc/inet.d`).

    :::console
    exec: 20: -hashed-df8ebe0300961b4230c639a427257c0dfe061fd6,157784fea6862263081b88f43ff8b0cf: not found

El sintoma es que un `tail -f` del log da mensajes de error sin parar

    :::console
    [Tue, 09 Nov 2010 16:45:03 GMT] [error] [0.91.0] OS Process died with status: 2
    
    [Tue, 09 Nov 2010 16:45:03 GMT] [error] [0.91.0] ** Generic server 0.91.0 terminating 
    ** Last message in was {#Port0.1831,{exit_status,2}}
    ** When Server state == {os_proc,-hashed-ad8d52d1277370343929dd7214b6a5106abe9e09,bc93fecc05e101f891d1afb58be1b8a7,
     #Port0.1831,
     #Funcouch_os_process.0.132953560,
     #Funcouch_os_process.1.15901032,5000}
    ** Reason for termination == 
    ** {exit_status,2}
