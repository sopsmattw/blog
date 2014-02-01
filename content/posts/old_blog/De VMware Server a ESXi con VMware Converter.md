Title: De VMware Server a ESXi con VMware Converter
Date: 2008-10-07 17:16:37
Category: Spanish
Tags: vmware, esxi, virtualization
Author: frommelmak

Chuleta rápida para convertir una máquina *VMware Server* (`.vmx`) a formato *appliance* para *VMware ESXi* (`.ova`/`.ovf`).

  * Inicio -> Todos los programas  -> VMware -> VMware Converter
  * Convert Machine -> Siguiente -> Siguiente
  * Select the type of source you want to use: Other (Siguiente)
  * Source VM or Image: `loquesea.vm`x (Siguiente)

Esperamos un rato e ignoramos el warning que da (Siguiente)

  * Siguiente, Siguiente
  * Select destination type: Virtual Appliance (Siguiente)
  * Virtual Appliance Name: lo que sea
  * Location: dónde sea que tengamos espacio suficiente
  * Siguiente

Rellenamos los detalles del appliance: Product URL, Version, Vendor, Vendor URL, Annotation...

  * Siguiente, Siguiente

Ahora seleccionamos el formato del fichero de salida (distribution format), teniendo especial cuidado de utilizar el formato ova. (Si especificamos ova, obtendremos tanto el formato ova como el ovf. OVF es que que vamos a poder importar desde ESXi)

  * Siguiente, Siguiente, Finalizar

Dependiendo del tamao del a imagen, el proceso puede tardar un buen rato, asi que paciencia.
