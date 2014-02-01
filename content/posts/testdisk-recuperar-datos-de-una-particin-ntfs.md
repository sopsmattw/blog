Title: TestDisk: Recuperar datos de una partición NTFS
Date: 2008-01-03 11:40:01
Category: Spanish
Tags: ntfs, testdisk, filesystems
Author: frommelmak

Imagina que tu PC se muere, imagina que te compras uno nuevo, llegas a casa lo conectas todo y lo enciendes. Imagina ahora que por alguna extraña razón decides instalar Windows en tu nuevo ordenador y en el momento de reparticionar el disco vas a saco. Pese a que te extraña ver dos discos piensas que los de la tienda han hecho algo raro y no le das más importancia. Te cargas **TODAS** las particiones que ves para empezar de cero y dejarlo todo como a ti te gusta. 

Justo en ese fatídico momento te das cuenta de que la BIOS de tu flamante nuevo equipo es capaz de arrancar desde dispositivos USB por lo que windows ha sido capaz de detectar el disco duro externo en el momento del particionado. Así que te lo has cargado todo todo y todo!!!

Antes de pensar en el suicidio como una posible solución al problema, quizás te interese seguir leyendo. Bueno, que no cunda el pánico!!! La teoría dice que sólo te has cargado la partición, por lo que el filesystem debería seguir ahí, intacto. Mas chulo que un ocho arrancas de nuevo el ordenador con un sistema operativo de verdad. Metes tu CD de Knoppix y tiras de `fdisk` para volver a crear la partición. Pero horror!!! Tras rehacerla, sigues sin poder montar el disco duro externo! Esto quiere decir que no sólo has eliminado la partición, sino que ademas dañado el filesystem que contiene.

Bien, es hora de asumir que quizás no sabes tanto como creías sobre particiones y filesystems y dejar paso a un experto en la materia: [TestDisk](http://www.cgsecurity.org/wiki/TestDisk).

Esta tool a la que debiste haber recurrido desde un buen principio es 100% GPL y te permite ,entre otras cosas, escanear el disco duro y detectar problemas con las particiones y/o los filesystem. Dado que existen versiones para Windows, Linux (el propio Knoppix la trae en sus últimas versiones) y Mac podrás utilizar la tool desde cualquier ordenador.

Pese a que la tool está ampliamente documentada en el wiki del proyecto, voy a tratar de explicar paso a paso como utilizarla para este caso en concreto, ya que en el momento de la recuperación, quizás estemos algo alterados como para tener que leer la documentación.

Lo primero de todo es instalar la aplicación en nuestro sistema. Si estamos utilizando un sistema GNU/Linux probablemente la tool ya este instalada. En caso contrario, la [descargaremos desde la web](http://www.cgsecurity.org/wiki/TestDisk_Download) y la instalaremos (descomprimir el fichero en el caso de windows) en el sistema.

Para ejecutarla en Linux basta con ejecutar testdisk como root. En windows en cambio, deberemos ejecutar el siguiente binario una vez descomprimido el software:

`testdisk\win\testdisk_win.exe`

##Guia Rápida.

Para recuperar una partición borrada, la secuencia de opciones a seleccionar sera esta:

No Log -> Seleccionamos partición a restaurar + Proceed -> Intel -> Analyse -> Proceed -> Buscar Vista ? N Seleccionamos la Partición a Restaurar + Enter -> Write ? Y -> Ok -> Quit  ->Quit ...

Si sólo hemos borrado la partición, ya deberíamos haber solucionado el problema.

Para comprobarlo salimos de la aplicación, (desmontamos: quitar hardware con seguridad) y desconectamos el disco USB. Volvemos a conectar y si el filesystem no tiene daños, deberá montarse sin más.

Si no es así, es porque probablemente hemos dañado el sector de arranque. Los pasos para intentar restaurar el sistema de ficheros serán estos:

No Log -> Seleccionamos partición a restaurar + Proceed -> Intel -> Advance -> Boot -> Rebuild BS (esperamos cruzando los dedos) -> Quit -> Quit ...

Al igual que antes, quitamos el hardware y lo volvemos a conectar para ver si ya es accesible.

Bueno, hasta aquí la guia rápida. Dejo unas capturas a continuación para ilustrar con más detalle los dos procesos descritos anteriormente.

##Recuperación de una partición con Test Disk paso a paso (con capturas):

    
    :::console        
    TestDisk 6.7, Data Recovery Utility, June 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    
    TestDisk is a data recovery designed to help recover lost partitions
    and/or make non-booting disks bootable again when these symptoms
    are caused by faulty software, certain types of viruses or human error.
    It can also be used to repair some filesystem errors.
    
    Information gathered during TestDisk use can be recorded for later
    review. If you choose to create the text file, testdisk.log , it
    will contain TestDisk options, technical information and various
    outputs; including any folder/file names TestDisk was used to find and
    list onscreen.
    
    Use arrow keys to select, then press Enter key:
    [ Create ] Create a new log file
    [ Append ] Append information to log file
    [ No Log ] Don't record anything


Donde seleccionaremos **`[ No Log ]`** si no deseamos guardar lo que vamos haciendo. Guardar un log podría ser útil en caso de problemas para por ejemplo poder enviar el log al creador de la tool o a algún foro especializado en busca de ayuda.

La siguiente pantalla que veríamos sería esta:

    
    :::Console
    TestDisk 6.7, Data Recovery Utility, June 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    TestDisk is free software, and
    comes with ABSOLUTELY NO WARRANTY.
    
    Select a media (use Arrow keys, then press Enter):
    Disk /dev/sda - 80 GB / 74 GiB
    Disk /dev/sdb - 2023 MB / 1929 MiB
    
    
    
    
    
    
    
    
    [Proceed ] [ Quit ]
           
    Note: Disk capacity must be correctly detected for a successful recovery.
    If a disk listed above has incorrect size, check HD jumper settings, BIOS
    detection, and install the latest OS patches and disk drivers.
    
    

Seleccionamos el dispositivo danado -`/dev/sdb` en este caso- y le damos a [Proceed].

    
    :::Console
    TestDisk 6.7, Data Recovery Utility, June 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    
    Disk /dev/sdb - 2023 MB / 1929 MiB
    
    Please select the partition table type, press Enter when done.
    [Intel ] Intel/PC partition
    [Mac ] Apple partition map
    [None ] Non partitioned media
    [Sun ] Sun Solaris partition
    [XBox ] XBox partition
    [Return ] Return to disk selection
    
    
    
    
    
    
    Note: Do NOT select 'None' for media with only a single partition. It's very
    rare for a drive to be 'Non-partitioned'.
        
    

Aquí seleccionamos Intel ya que la partición del ejemplo es NTFS (PC).

    
    :::Console
    TestDisk 6.7, Data Recovery Utility, June 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
            
            
    Disk /dev/sdb - 2023 MB / 1929 MiB - CHS 246 255 63
           
    [ Analyse ] Analyse current partition structure and search for lost partitions
    [ Advanced ] Filesystem Utils
    [ Geometry ] Change disk geometry
    [ Options ] Modify options
    [ MBR Code ] Write TestDisk MBR code to first sector
    [ Delete ] Delete all data in the partition table
    [ Quit ] Return to disk selection
    
    
    
    
    
    
    Note: Correct disk geometry is required for a successful recovery. 'Analyse'
    process may give some warnings if it thinks the logical geometry is mismatched.
        
    

En primer lugar recuperaremos la tabla de particiones que hemos perdido utilizando la opción [ Analyse ].

    
    :::Console
    TestDisk 6.7, Data Recovery Utility, June 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    Disk /dev/sdb - 2023 MB / 1929 MiB - CHS 246 255 63
    Current partition structure:
    PartitionStart EndSize in sectors
    
    1 * HPFS - NTFS0   1  1  245 254 63  156296322
    
    
    
    
    
    
    
    
    
    
    
    
    
    *=Primary bootable P=Primary L=Logical E=Extended D=Deleted
    [Proceed ]
     Try to locate partition


Seleccionamos [Proceed].

    
    :::Console
    TestDisk 6.8, Data Recovery Utility, August 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    Should TestDisk search for partition created under Vista ? [Y/N] (answer Yes if unsure)
        
    

Si el disco no fue formateado bajo Vista responderemos Y, en caso contrario N.

    
    :::Console
    TestDisk 6.8, Data Recovery Utility, August 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    Disk /dev/sdb - 2023 MB / 1929 MiB - CHS 246 255 63
    Partition               Start        End    Size in sectors
    * HPFS - NTFS              0   1  1   244 254 63    3935862
            
            
            
            
            
            
            
            
            
            
            
            
    Structure: Ok.  Use Up/Down Arrow keys to select partition.
    Use Left/Right Arrow keys to CHANGE partition characteristics:
    *=Primary bootable  P=Primary  L=Logical  E=Extended  D=Deleted
    Keys A: add partition, L: load backup, T: change type, P: list files,
    Enter: to continue
    NTFS, 2015 MB / 1921 MiB
            
       
Le damos a Enter.

    
    :::Console 
    TestDisk 6.8, Data Recovery Utility, August 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    Disk /dev/sdb - 2023 MB / 1929 MiB - CHS 246 255 63
    
    Partition                  Start        End    Size in sectors
    
    1 * HPFS - NTFS              0   1  1   244 254 63    3935862
    
    
    
    
    
    
    
    [  Quit  ]  [Search! ]  [ Write  ]
    Search deeper, try to find more partitions
            
        
Guardamos la propuesta [Write].

    
    ::::Console
    TestDisk 6.8, Data Recovery Utility, August 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    Write partition table, confirm ? (Y/N)
            
        

Si sólo has dañado la partición, ya hemos terminado. Desconecta el disco y vuelve a conectarlo. Si sigues sin poder acceder a la unidad, es probable que también este dañado el sistema de ficheros, pero no te preocupes. Con un poco de suerte aun podrás reconstruirlo si no has perdido el backup del que dispone es propio sistema de ficheros NTFS. El procedimiento paso a paso seria este:

##Recuperación de un filesystem NTFS con Test Disk paso a paso (con capturas):

Las primeras cinco capturas serían análogas al procedimiento descrito para recuperar la información, sólo que en esta ocasión, en lugar de la opción [Analyse], seleccionaremos la opción [Advance].


    :::console
    TestDisk 6.8, Data Recovery Utility, August 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    Disk /dev/sdb - 2023 MB / 1929 MiB - CHS 246 255 63
    Partition                  Start        End    Size in sectors
    1 * HPFS - NTFS              0   1  1   244 254 63    3935862
    
    Boot sector
    Status: Bad
    
    Backup boot sector
    Satus: OK
    
    Sectors are not identical.
    
    A valid NTFS Boot sector must be present in order to access
    any data; even if the partition is not bootable.
    
    
    
    [  Quit  ]  [  List  ]  [Backup BS] [Rebuild BS][  Dump  ]
    Return to Advanced menu


Vemos que el sector de arranque parece estar dañado, no obstante y dado que el sector de boot de backup es correcto, podemos restaurar utilizando dicho backup. Para ello seleccionamos la opción [Backup BS].

    
    :::Console
    TestDisk 6.8, Data Recovery Utility, August 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    Copy backup NTFS boot sector over boot sector, confirm ? (Y/N)
    
    

Confirmamos con Y y hemos terminado.

    
    :::Console        
    TestDisk 6.8, Data Recovery Utility, August 2007
    Christophe GRENIER grenier@cgsecurity.org
    http://www.cgsecurity.org
    
    Disk /dev/sdb - 2023 MB / 1929 MiB - CHS 246 255 63
    Partition                  Start        End    Size in sectors
    1 * HPFS - NTFS              0   1  1   244 254 63    3935862
    
    Boot sector
    Status: OK
    
    Backup boot sector
    Status: OK
    
    Sectors are identical.
    
    A valid NTFS Boot sector must be present in order to access
    any data; even if the partition is not bootable.
    
    
   
    [  Quit  ]  [  List  ]  [Rebuild BS][Repair MFT][  Dump  ]
    Return to Advanced menu          
    

Salimos...quit, quit, quit...etc. Y volvemos a conectar el disco. Si todo ha ido bien y con un poco de suerte, deberías ver todos tus datos intactos.

**Nota**: El ejemplo descrito aquí es para el caso concreto descrito al inicio. Quizás tengas que jugar un poquito más con la tool para recuperar tus datos, o puede que el daño sea tan serio que esta tool no te pueda ayudar. Si es as, las opciones pasan por tools propietarias o servicios de pago o empezar a asumir que lo has perdido todo.
