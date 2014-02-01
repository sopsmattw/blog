Title: rabbitmqctl: Error unable to connect to node
Date: 2013-01-17 15:22:47
Category: English
Tags: rabbitmq
Author: frommelmak

If you are running `rabbitmqctl` with a different user than the one used by server, you will get an error like this:

    :::bash
    rabbitmqctl status Status of node rabbit@foo
    Error: unable to connect to node rabbit@foo: nodedown
    - home dir: /root
    - cookie hash: 0fWPcZtM431dRX003r6OAg==

This is because the cookie stored in your home directory `.erlang.cookie` differs from the cookie used by the server instance.

The cookie file used by the server is inside the home dir used by the server. You can see the location of the home dir in the stdout of the rabbitmq server during the startup. Something like:

    :::console
    home dir : /opt/rabbitmq/var/lib/rabbitmq
    cookie hash : NNYm39bSA1i7yB+fQjTdiOJK

To solve the problem, just copy the `.erlang.cookie` in the home dir of the user you are using to execute the rabbitmqclt command line.


