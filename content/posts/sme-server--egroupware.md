Title: SME Server + eGroupWare
Date: 2007-06-28 21:51:34
Category: Spanish
Tags: sme
Author: frommelmak

Como administrador de sistemas, una de las cosas que más me satisface es descubrir cosas de las que -inexplicablemente- no había oído hablar nunca.

Este post habla de dos proyectos libres que no conocía y que me han venido que ni pintados: [SME Server](http://wiki.contribs.org/) y [eGroupWare](http://www.egroupware.org/)

SME Server es el acrónimo de *Small and Medium Enterprise Server*, y eso es exactamente lo que es: una distribución GNU/Linux con los principales servicios que una pequeña o mediana empresa pueda necesitar. Además, todo ello out-of-the-box y con una interfaz web de administración de lo más acertada.

SME Server está basado en [CentOS 4.4](http://www.centos.org/), un rebuild de *Red Hat Enterprise Linux 4 Update 4*, que cabe en un sólo CDROM.

La instalación es asombrosamente sencilla, independientemente de los servicios que necesitemos. Tras unos pocos pasos, tendremos desde un simple servidor de ficheros e impresión, hasta un completo servidor de dominio, un gateway, un servidor servidor de correo y/o un servidor web.

El procedimiento de instalación nos ofrecerá la posibilidad de implementar diferentes niveles de RAID por software. Además, podemos añadir discos una vez instalado el sistema y montar el RAID más adelante si así lo deseamos.

Sin duda alguna, el punto fuerte de SME Server es su interaz web. Grácias a ella, la administración, configuración y actualiación del sistema es un juego de niños. Las altas, bajas y administración de grupos y usuarios, o la creación de *shares* se realizan en unos pocos segundos y sin necesidad de tener conocimientos específicos en administración de sistemas.

Esto último es especialmente importante, ya que no debemos olvidar que no todas las PYMEs pueden permitirse el tener a un administrador de sistemas 24x7 para simplemente crear un share o añadir un usuario.

Otro de los aspectos que más me han gustado ha sido la posibilidad de instalar servicios adicionales a los que vienen en la distribución base. Estos servicios están contribuidos y soportados por la amplia comunidad de usuarios de este estupendo sistema. Este es el caso de [eGroupWare](http://www.egroupware.org/), que pese a no formar parte del conjunto de servicios proporcionados por SME Server, esta disponible como contribución y se integra a las mil maravilla con los usuarios ya definidos en SME Server.

**eGroupWare** esta formado por un conjunto de aplicaciones para el trabajo en grupo necesarias en cualquier oficina: Calendario, libreta de direcciones y contactos, cliente de email web corporativo, notas, listas de tareas, noticias, gestión de recursos (reserva de salas, coches de empresa,...), gestión de proyectos y un montón de aplicaciones más disponibles en forma de módulos.

Esta programada en PHP y ha sido portada a SME Server por lo que su instalación y configuración es muy sencilla.

Actualmente he instalado SME Server como servidor de ficheros con muy buenos resultados, y en breve instalaré eGroupWare en un entorno en producción.

Sinceramente, si quieres montar el servicio y dejar que sea el usuario final el que se soporte la aplicación, SME Server es sin lugar a dudas la herramienta que estabas buscando.
