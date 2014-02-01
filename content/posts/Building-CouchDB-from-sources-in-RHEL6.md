Title: Building CouchDB from sources in RHEL6
Date: 2011-04-18 19:00:48
Category: English
Tags: couchdb, rhel, erlang
Author: frommelmak

Install Erlang from sources:

Prerequisites: `unixODBC-devel-2.2.14-11.el6.i686.rpm`

    :::console 
    wget http://www.erlang.org/download/otp_src_R14B02.tar.gz
    tar zxvf otp_src_R14B02.tar.gz
    cd otp_src_R14B02 LANG=C; export LANG
    ./configure --prefix=/opt/erlang
    make
    make install

Install Mozilla SpiderMonkey from sources:

Prerequisties: `libicu-devel-4.2.1-9.el6.i686.rpm`, `libicu-4.2.1-7.el6.i686.rpm`

    :::console 
    wget http://ftp.mozilla.org/pub/mozilla.org/js/js-1.7.0.tar.gz
    tar zxvf js-1.7.0.tar.gz
    cd js/srcmkdir /opt/js-devel
    make BUILD_OPT=1 JS_DIST=/opt/js-devel -f Makefile.ref export

And finally install Couchdb from sources:
 
    :::console
    ERL='/opt/erlang/bin/erl' ;
    export ERLERLC='/opt/erlang/bin/erlc' ;
    export ERLCwget http://apache.rediris.es//couchdb/1.0.2/apache-couchdb-1.0.2.tar.gz
    tar zxvf apache-couchdb-1.0.2.tar.gzcd apache-couchdb-1.0.2./configure --prefix=/opt/couchdb \
    --with-erlang=/opt/erlang/lib/erlang/usr/include/ \
    --with-js-include=/opt/js-devel/include/js \
    --with-js-lib=/opt/js-devel/lib
    make
    make install
