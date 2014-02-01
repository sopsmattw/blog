Title: Utilizar el lector de huellas del Dell m1330 en GNU/Linux
Date: 2008-07-08 23:45:08
Category: Spanish
Tags: m1330, dell
Author: frommelmak

Bueno, este va a ser una entrada breve. Casi tanto como rápido y fácil ha sido configurar esto en Opensuse 11. Y es que Linux ya no es lo que era. Ahora casi todo se puede hacer a golpe de ratn (snif snfi!).

Bueno, ahi va la receta:

  * Desde la sección *Hardware* de *Yast*, habilitamos el lector de huellas (Fingerprint Reader).
  * Vamos a la sección *Security and Users* de Yast y seleccionamos *User and Group Management*. En la pestaa Users, seleccionamos los usuarios que queremos puedan validar su sesion mediante el lector de huellas y editamos sus propiedades. Vamos a la ventana de plugins, seleccionamos el plugin *Sets the User Fingerprint* y le damos a *Launch*. Nos pedirá que pasemos el dedo tres veces por el lector y listos.

Ahora, si abrimos un terminal y nos convertimos en `su - usuario`, nos pedirá que introduzcamos el *password* o pasemos el dedo. Mola!

Bueno, pero como funciona realmente todo esto ?

Por un lado, lo que hemos hecho es configurar la autenticación *pam* para llamar a los modulitos que permiten la entrada desde el lector de huellas. Dicho de otro modo, metemos en `/etc/pam.d/common-auth-pc` esta linea:

    :::console
    auth sufficient pam_thinkfinger.so

Luego, via Yast hemos llamado a la herramienta *Think Finger* para que lea y verifique nuestra huella y la meta en `/etc/pam_thinkfinger` en formato `usuario.bir`.

Así pues, para que también podamos pasar a root con un sólo dedo, hemos de ejecutar el siguiente comando (pasando olimpicamente de Yast). Aunque sólo sea para que parezca que sabemos lo que estamos haciendo.

    :console
    tf-tool --add-user root

Si queremos pasar al 100% de Yast y hacerlo todo desde la línea de comandos, hemos de asegurarnos de cargar el modulo `uinput` y que tenemos un dispositivo tipo `/dev/input/uinput` o similar.

Para más informacin: `man pam_thinkfinger`, `man tf-tool` y [thinkfinger.sourceforge.net]()

Por cierto, por si no lo habeis adivinado aun sí, ahora tengo un *Dell m1330* full featured ! Con gadgets así, los cambios de trabajo se hacen menos duros jeje.
