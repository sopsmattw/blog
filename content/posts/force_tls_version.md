Title: Force an old version of TLS 
Date: 2020-01-20 16:06:00
Category: English 
Tags: apache, ssl, tls 
Author: frommelmak

If you -for whatever reason- need to force the old TLS-1.0, you can put the folllowing line en  the Apache's `/etc/apache2/mods-enabled/ssl.conf` file.

    :::bash
    SSLProtocol All -TLSv1.1 -TLSv1.2

*Note*: TLS-1.0 is broken and is considered insecure. This version of the protocol will be rejected by the major browsers at some point during the current year.
So, use this trick at your own risk. Tested on Ubuntu 12.04.

