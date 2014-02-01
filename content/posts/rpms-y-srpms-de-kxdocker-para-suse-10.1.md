Title: RPMS y SRPMS de KXDocker para SuSE 10.1
Date: 2006-08-19 00:13:03
Category: Spanish
Tags: RPM, SRPM, kxdocker, dock, suse
Author: frommelmak

Bueno, por fin he podido dedicar algo de tiempo ha crear los paquetes RPM y source RPM para [SuSE 10.1](http://www.opensuse.org/) de [KXDocker](http://www.xiaprojects.com/www/prodotti/kxdocker/main.php). No he sido capaz de encontrar los RPM completos de la última versión (1.1.4a) por ninguna parte, ni siquiera en [rpm.pbone.net](http://rpm.pbone.net). Por otro lado, en la web oficial del proyecto sólo están los paquetes precompilados para [Gentoo](http://packages.gentoo.org/packages/?category=kde-misc;name=kxdocker) y [Slackware](http://packages.gentoo.org/packages/?category=kde-misc;name=kxdocker). Así que finalmente he decidido crear mis propios RPM. De esta manera, la próxima vez que por cualquier motivo tenga que reinstalar todo el sistema operativo, tendré mi Dock Bar favorita en marcha en un momento.

**Actualización**: Los paquetes `taskmanager` y `gaclock` han sido actualizados a la release 2 porque había un error en el `.spec`. Con los nuevos paquetes, estos plugins ya deberian funcionar sin problemas.

| RPMS SuSE 10.1                           | SRPM SuSE 10.1                          |
| ---------------------------------------- | --------------------------------------- |
| [kxdocker-1.1.4a-1.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-1.1.4a-1.i586.rpm)                             | [kxdocker-1.1.4a-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-1.1.4a-1.src.rpm)                              |
| [kxdocker-configurator-1.0.2-1.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-configurator-1.0.2-1.i586.rpm)     | [kxdocker-configurator-1.0.2-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-configurator-1.0.2-1.src.rpm)      |
| [kxdocker-trayiconlogger-1.0.0-1.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-trayiconlogger-1.0.0-1.i586.rpm) | [kxdocker-trayiconlogger-1.0.0-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-trayiconlogger-1.0.0-1.src.rpm)  |
| [kxdocker-dcop-1.0.0-1.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-dcop-1.0.0-1.i586.rpm)                     | [kxdocker-dcop-1.0.0-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-dcop-1.0.0-1.src.rpm)                      |
| [kxdocker-i18n-1.0.2-1.i586.rpm ](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-i18n-1.0.2-1.i586.rpm)                    | [kxdocker-i18n-1.0.2-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-i18n-1.0.2-1.src.rpm)                      |
| [kxdocker-resources-1.1.0-1.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-resources-1.1.0-1.i586.rpm)           | [kxdocker-resources-1.1.0-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-resources-1.1.0-1.src.rpm)            |
| [kxdocker-taskmanager-1.0.2-2.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-taskmanager-1.0.2-2.i586.rpm)       | [kxdocker-taskmanager-1.0.2-2.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-taskmanager-1.0.2-2.src.rpm)        |
| [kxdocker-gaclock-1.0.1-2.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-gaclock-1.0.1-2.i586.rpm)               | [kxdocker-gaclock-1.0.1-2.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-gaclock-1.0.1-2.src.rpm)                |
| [kxdocker-gdate-1.0.0-1.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-gdate-1.0.0-1.i586.rpm)                   | [kxdocker-gdate-1.0.0-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-gdate-1.0.0-1.src.rpm)                    |
| [kxdocker-gtrash-1.0.0-1.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-gtrash-1.0.0-1.i586.rpm)                 | [kxdocker-gtrash-1.0.0-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-gtrash-1.0.0-1.src.rpm)                  |
| [kxdocker-gbattery-1.0.0-1.i586.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-gbattery-1.0.0-1.i586.rpm)             | [kxdocker-gbattery-1.0.0-1.src.rpm](http://nomeriasdeti.no-ip.com/files/suse/10.1/RPMS/kxdocker-gbattery-1.0.0-1.src.rpm)              |
