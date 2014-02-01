Title: VPN using SSH
Date: 2011-09-12 19:29:21
Category: English
Tags: ssh, vpn
Author: frommelmak

Las versiones recientes del servidor OpenSSH permiten montar una VPN utilizando una conexinSSH. Esto nos permite, por ejemplo, tener acceso a todos los puertos del servidor incluso en aquellos casos en los que sólo nos dan acceso al puerto de SSH.

Para montar una VPN utilizando el servidorSSHen Debian haremos lo siguiente...        

##SERVER:

Aadimos en `/etc/ssh/sshd_config`
    
    :::console                     
    PermitTunnel point-to-point
    PermitRootLogin yes

Para crear el dispositivo TUN es necesario ejecutar algunos comandos como root, por eso utilizamos la directiva `PermiRootLogin` a yes. Si no queremos dar acceso de login al usuario root, podemos utilizar otras soluciones ms elegantes como: `forzed-commands-only` o  `without-password` que no comprometen tanto la seguridad como `PermitRootLogin yes`. Ver enlaces relaccionados al final del documento.

Finalmente, recuerda que es necesario reiniciar el servidorSSHpara que los cambios tengan efecto.

Editamos: `/etc/network/interfaces`

    :::console
    allow-hotplug tun0
    iface tun0 inet static
          address 10.0.0.1
          netmask 255.255.255.0
          pointopoint 10.0.0.2

Es vital utilizar `allow-hotplug tun0`para que se creen automticamente los dispositivos tun con udev, de lo contrario deberemos utilizar herramientas como `tunctl`para crear los dispositivos, lo cual puede darnos problemas de permisos al intentar abrir/crear los dispositivos.


##CLIENT:

Editamos: `/etc/network/interfaces`
    
    :::console                     
    allow-hotplug tun0
    iface tun0 inet static
          pre-up ssh -vv -i /root/.ssh/id_rsa -S /var/run/ssh-vpn-tunnel-control -M -f -w 0:0 root@ssh_server true
          pre-up sleep 5
          address 10.0.0.2
          pointopoint 10.0.0.1
          netmask 255.255.255.0
          #up route add -net 192.168.1.0 netmask 255.255.255.0 tun0 #creating optional route
          #down route del -net 192.168.1.0 netmask 255.255.255.0 tun0 #creating optional route
          post-down ssh -i/root/.ssh/id_rsa -S /var/run/ssh-vpn-tunnel-control -O exit root@ssh_server

Con esto conseguimos establecer una conexin punto a punto con el servidor ssh remoto, si bien, en ocasiones querremos ir un poco ms all. Por ejemplog. Si queremos llegar a otoros equipos ubicados en la red remota, o al reves, cuando varios equipos de nuestra red han de poder llegar al servidor remoto.
            
Se asume que hemos creado el par de claves privada/publica `id_rsa/id_rsa.pub`y que hemos copiado la publica al servidor SSH remoto para poder autenticar sin necesidad de proporcionar password.

###Arrancar y detener la VPN

Para iniciar la conexin punto a punto utilizaremos los comandos `ifup tun0` e `ifdown tun0` respectivamente.

Ahora ya ponemos alcanzar el servidor remoto en 10.0.0.1.

Tras establecer la conexin punto a punto, y en base a nuestras necesidades, podemos encontrarnos diferentes escenarios. Por ejemplo:

###Acceso a otros equipos de la red remota

Activamos el forwarding en el servidorSSH y ejecutamos:
                         
    :::console
    iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o eth0 -j MASQUERADE

###Acceso al servidor remoto desde varios equipos de nuestra red

Activamos el forwarding en el cliente de ssh y ejecutamos:

    :::console                         
    iptables -t nat -A POSTROUTING -o tun0 -j MASQUERADE

En cada uno de los equipos de red que deseamos que tengan acceso al servidor, deberemos configurar la ruta correspondiente:

Por ejemplo en windows:

    :::console
    route add 10.0.0.0 mask 255.255.255.0 IP_SSH_CLIENT
            
**Nota**: Para activar el forwarding en ambos casos: `sysctl -w net.ipv4.ip_forward=1`


Fuentes: 
            
  * [bodhizazen.net/Tutorials/VPN-Over-SSH]()
  * [www.debian-administration.org/articles/539]()
