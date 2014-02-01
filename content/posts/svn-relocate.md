Title: SVN relocate
Date: 2009-11-16 11:22:17
Category: Spanish
Tags: svn, subversion
Author: frommelmak

**Nota rápida**: Si el host o la IP del servidor de svn cambia, un upgrade de tu copia local fallará. Esto es porque tu copia local hace referencia a la IP o nombre viejo. Para que no tengas que hacer un chekcout entero del repositorio, es posible cambiar la copia local para que haga referencia a la nueva IP. Para ello utilizaremos el comando `switch` de `svn`:

    :::console
    cd /working_copy
    svn switch --relocate svn://HOST/REPO_PATH svn://host/REPO_PATH .
