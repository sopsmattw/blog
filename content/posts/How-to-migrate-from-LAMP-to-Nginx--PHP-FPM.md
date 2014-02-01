Title: How to migrate from LAMP to Nginx + PHP-FPM
Date: 2011-11-03 14:26:49
Category: English
Tags: nginx, php
Author: frommelmak

This blog has been migrated from Apache2 + mod_php to Nginx + PHP-FPM. In this entry I'm going to explain the whole process (just for fun).

The easiest way is just install the precompiled packages from [www.dotdeb.org]() as explained [here](http://www.codernotes.com/2011/7/install-nginx-and-php-fpm-on-debian-6-squeeze-2/).
Unfortunatelly my blog isn't compatible with the latest PHP versions provided by dotdeb, so I've had to compile my own version of PHP-FPM.

Firts of all, we need to install Nginx:

    :::console
    apt-get install nginx

Then I downloaded the source code of PHP 5.4.3 from [http://www.php.net/releases/]()

    :::console
    cd /var/tmp 
    wget http://museum.php.net/php5/php-5.3.4.tar.gz
    tar zxvf php-5.3.4.tar.gz
    cd php-5.3.4
    ./configure --prefix=/opt/php-5.3.4 --enable-fpm --with-mcrypt --with-zlib --enable-mbstring --disable-pdo --with-mysql --with-curl --disable-debug --disable-rpath --enable-inline-optimization --with-bz2 --with-zlib --enable-sockets --enable-sysvsem --enable-sysvshm --enable-pcntl --enable-mbregex --with-mhash --enable-zip --with-pcre-regex
    make all
    make install

Now, the required PHP version, including the PHP-FPM service are installed here: `/opt/php5-3.4`

The easiest way to get the PHP-FPM service running is by using the init script and the config files contained in the php5-fpm dotdeb package.

    :::console
    wget http://packages.dotdeb.org/dists/squeeze/php5/binary-i386/php5-fpm_5.3.8-1~dotdeb.2_i386.deb
    dpkg-deb -x php5-fpm_5.3.8-1~dotdeb.2_i386.deb /tmp/php5-fpm
    cp /tmp/php5-fpm/etc/init.d/php5-fpm /etc/init.d/php5-fpm
    cp -R /tmp/php5-fpm/etc/fpm /etc/php5/
    ln -s /opt/php-5.3.4/sbin/php-fpm /usr/sbin/php5-fpm

Now you should copy your previous php.ini file into the correct place: Use `phpinfo ()` to know the correct path for the php.ini file: 

    :::console
    /opt/php-5.3.4/bin/php -i|grep php.ini
 
In this case, the PHP-FPM will look for php.ini here `/opt/php-5.3.4/lib`, so just drop your previous file here.
 
    :::console
    cp /etc/php5/apache2/php.ini /opt/php-5.3.4/lib
