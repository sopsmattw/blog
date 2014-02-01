Title: Crear discos virtuales de más de 256GB en VMware ESXi
Date: 2009-08-11 14:53:41
Category: Spanish
Tags: hdd, esx, vmware
Author: frommelmak

Por defecto, al instalar ESXi en una máquina con un sólo disco configurado en el sistema, el datastore que se crea utiliza todo el espacio disponible en dicho dispositivo. Además configura el `block_size` del filesystem `vmfs3` del datastore a 1MB. Esto limita el tamaño máximo de los discos virtuales que podremos crear en dicho datastore a 256GB.

Para poder crear discos de mayor tamao es necesario definir un `block_size` de mayor tamaño (2MB para 510GB y 4MB para 1TB). El problema es que una vez creado el datastore no es posible modificar el `block_size`. La solución pasa por eliminar el datastore nada más instalar ESXi y volver a crearlo. En ese momento sí que es posible seleccionar el tamaño del `block_size`.

No lo he probado, preo otra opción seria crear un datastore para las máquinas virtuales con un `block_size` de 1MB y otro para el disco o discos virtuales con un tamao de `block_size` de 2MB o 4MB.
