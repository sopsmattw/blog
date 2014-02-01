Title: Instalar subversion 1.6.5 en en Ubuntu dapper
Date: 2009-10-28 20:32:51
Category: Spanish
Tags: svn, subversion, ubuntu
Author: frommelmak

La última versión del paquete subversion en *Ubuntu Dapper* es de la rama 1.3.x. Si queremos actualizar el servidor deberemos compilar subversion desde las fuentes con la opción `--without-serf` para as poder satisfacer las dependencias.

En resumen:

    :::console
    mkdir svntemp
    cd svntemp
    wget http://subversion.tigris.org/downloads/subversion-1.6.5.tar.gz
    wget http://subversion.tigris.org/downloads/subversion-deps-1.6.5.tar.gz
    tar zxvf subversion-1.6.5.tar.gz
    tar zxvf subversion-deps-1.6.5.tar.gz
    cd subversion-1.6.5
    ./configure --without-serf --prefix=/opt/subversion-1.6.5
    make
    make install

Tras esto exportamos el repositorio actual (dump) y lo cargamos en la nueva versin de subversion:

    :::console
    cd /path/al/repositoriosvnadmin dump /path/al/repositorio  /path/al/dumpfile-$(date +%F)

creamos repositorio nuevo:

    :::console
    /opt/subversion-1.6.5/bin/svnadmin create nuevo_repositorio

cargamos fichero dump con la nueva versin de svnadmin:

    :::console
    /opt/subversion-1.6.5/bin/svnadmin load repository-name  repository.dumpfile

Si utilizamos `websvn`, este seguir funcionando sobre el nuevo repositorio si bien deberemos configurarlo para que utilice el svn instalado en opt en vez del instalado como paquete, que podemos borrar (manteniendo websvn).
