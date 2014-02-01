Title: How to use Gmail POP/SMTP services from unsecure clients
Date: 2011-05-23 22:15:55
Category: English
Tags: ssl, pop, smtp, gmail, google
Author: frommelmak

Sometimes you may need to send or retrieve email notifications using SMTP or POP Gmail services, but your client does not support SSL connections. In such cases you can use a SSL proxy tunnel such as stunnel.

stunnel is available as a Debian package, and probably in other modern Linux distributions. It is also available as Win32 binary.
The installation in debian is as simple as type:

    ::::console
    apt-get install stunnel

Since stunnel relies on OpenSSL libraries, the first thing is create a x509 cert.

    :::console
    cd /etc/ssl/certs
    openssl req -new -x509 -days 3650 -nodes -out stunnel.pem -keyout stunnel.pem

Then you need to configure stunnel in order to forward all the traffic in the 110 (POP) and 25 (SMPT) to the Gmail 995 and 465 ports respectively.

    :::console
    /etc/stunnel/stunnel.conf
    [pop3s]
    accept = server_ip_address:110 
    connect = pop.gmail.com:995 
    
    [ssmtp] 
    accept = server_ip_address:25
    connect = smtp.gmail.com:465

The server_ip_address could be the LAN interface IP address or the localhost, depending if the client program is running localy or in some other host in your LAN.

Finaly, just start de service:

    :::console
    /etc/init.d/stunnel4 start

And test the service:

    :::console
    telnet server_ip_address 110
    Trying ...
    Connected to somehost.
    Escape character is '^]'.
    +OK Gpop ready for requests from xx.xx.xx.xx dewf14449283wbe.15
    USER your_user@gmail.com
    +OK send PASS
    PASS your_gmail_pass
    +OK Welcome.
    LIST
    +OK 2 messages (23782 bytes)
    1 3124
    2 2758

If you can connect with telnet, your client can do it too.

[@oriolrius](https://twitter.com/oriolrius), thanks for telling me about this tool.

For more info visit: [www.stunnel.org](http://www.stunnel.org).
