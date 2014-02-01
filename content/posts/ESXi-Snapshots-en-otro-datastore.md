Title: ESXi: Snapshots en otro datastore
Date: 2010-11-04 00:22:40
Category: Spanish
Tags: vmware, esxi, virtualization
Author: frommelmak

Si al intentar hacer un snapshot de un guest nos dice que no tenemos espacio, tenemos dos opciones: La primera es añadir otro disco duro y añadirlo al datastore en el que reside la máquina, la segunda es hacer el snapshot en otro datastore.

No obstante, hay escenarios en los que la primera opción puede no ser una solución. Por ejemplo: Si el guest dispone de dos discos duros virtuales, cada uno en un datastore con tamano de bloque diferente, podría ser que pese a tener espacio, el tamaño máximo del fichero permitido en el datastore en el que reside el disco principal no permita realizar el snapshot. En este y otros casos, la solución pasa por forzar el snapshot en otro datastore.

Para ello, existe una variable que controla dónde se hacen los snapshots. Si esta variable no existe, se realizarán el el mismo folder dónde se encuentre el fichero `.vmx` que define la máquina.

Para hacer los snapshots en otro datastore:

  - Paramos el guest.
  - Conectamos por ssh al host y editamos el `.vmx del guest a snapshotear.
  - Creamos un folder para los snapshots el el host
  - Añadimos la variable `workingDir=/vmfs/volumes/id-datastore/vm-snapshots`
  - Desregistramos la máquina: *Remove from invetory*
  - La volvemos a registrar utilizando el fichero `.vmx (ver captura)`.

![vmx register](|filename|/images/old_blog/register_vmachine.png)

Tras esto, veremos que el working dir es ahora otro el folder `vm-snapshots`. Este cambio afecta también al área de *swap* de esta máquina que pasa a estar en el nuevo datastore.
