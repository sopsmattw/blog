Title: Configurar fail2ban para notificaciones por email 
Date: 2011-02-04 09:54:45
Category: Spanish
Tags: fail2ban
Author: frommelmak

Por defecto fail2ban no notifica los baneos al servicio ssh por email. En las ultimas versiones (0.8.4) la config ha cambiado sustancialmente. Para habilitar el envio de emails hemos de crear el fichero `jail.local` en `/etc/fail2ban` con este contenido.

    :::console
    [ssh]action = %(action_mw)s
