Title: Establecer una conexion OpenVPN desde una tarea de cron
Date: 2008-12-31 00:21:36
Category: Spanish
Tags: cron, openvpn
Author: frommelmak

Es muy típico que un script que funciona perfectamente desde una sesión de usuario normal falle al correr como un trabajo ejecutado por el cron.

Generalmente esto es debido a que las variables de entorno bajo las que se ejecuta el script en uno y otro caso no son las mismas.

En el caso de lanzar OpenVPN como demonio desde una tarea de cron es importante tener esto en cuenta, ya que OpenVPN tras la autenticación llamará al comando `ifconfig` para crear el dispositivo de red virtual.

Llegado este momento, si `/sbin` no forma parte de la variable de entorno `PATH`, nuestro script fallará.

Invocar a `/etc/init.d/openvpn start | stop` para establecer y parar la conexión requiere utilizar los ficheros de configuración ubicados en `/etc/openvpn` y jugar con `/etc/default/openvpn` para que el script de inicialización haga lo que queremos. Así, una opción más fácil puede ser llamar a openvpn con un script similar a este, evitando parar accidentalmente sesiones de vpn no deseadas.

    :::bash
    #!/bin/bash
    PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
    /usr/sbin/openvpn --daemon --writepid /var/run/myvpn --cd /root/vpn --config /root/vpn/client.conf
    /bin/sleep 16
    ... (lo que sea que hagamos por la VPN... acceso seguro a svn por ejemplo)...
    /bin/kill $(cat /var/run/myvpn)  rm /var/run/mypid

  * Con `PATH` aseguramos que OpenVPN, al correr como hijo del cron encuentra el comando `ifconfig`.
  * Con `--daemon`, OpenVPN corre como demonio. De lo contrario, el script nunca pasaria de esta lnea.
  * Con `--writepid /var/run/myvpn` escribimos el PID del proceso OpenVPN en el fichero `/var/run/myvpn`. Esto nos permite matar sólo esa sessión de vpn con `killall` más adelante.
  * `sleep` es sálo para asegurar que el dispositovo TAP y las rutas existan antes de utilizarlas.
    
Finalmente matamos sólo la conexión vpn establecida por este script.
    
Por otro lado, si además de los certificados y claves necesitamos de una autenticación mediante user y password, deberemos especificar el fichero que los contiene tras la opción `auth-user-pass /root/vpn/up`. Esta opción suele estar en en fichero `client.conf` y es la responsable de que se te pregunte que introduzcas un usuairo y password en aquellas conexines que asi lo requieren. De hecho, todas las opciones que hemos pasado a openvpn por linea de comandos mediante `--opcion`, pueden ir en dicho fichero de configuración si as lo deseamos.
