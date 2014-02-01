Title: SFTP jail en OpenSSH
Date: 2009-12-02 10:33:48
Category: Spanish
Tags: sftp, ssh
Author: frommelmak

Las versiones recientes de OpenSSH facilitan la tarea de enjaular a los usuarios dentro de su home al acceder por SFTP. Para ello podemos utilizar la directivas `Match` y `ChrootDirectory` que permiten sobreescribir las opciones globales de configuración para un grupo, usuario, host o IP determinados.

Ejemplo `sshd_config`:

    :::console
    Subsystem sftp internal-sftp
    Match user pepeuser
     ChrootDirectory /path/to/some_place
     X11Forwarding no
     AllowTcpForwarding no
     ForceCommand internal-sftp

**Nota**: el home de `pepeuser` ha de ser la raiz del sistema `/` ya que esta será relativa al `ChrootDirectory` especificado para ese *user* en `sshd_config`. 

El *shell* para ese user puede ser `/bin/false` para evitar accesos via ssh para ese user.
