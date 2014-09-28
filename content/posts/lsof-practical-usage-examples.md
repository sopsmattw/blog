Title: lsof practical usage examples 
Date: 2014-06-03 19:53:00
Category: English
Tags: lsof, sysadmin, tools 
Author: frommelmak

As you probably know, `lsof` stands for List of Open Files. Yes, it's seems a simple description for a simple Unix command but, wait! Have you ever heard that everything in Unix is a file? Yes, right? So maybe this tool is more powerful than you think.

Let me show you how powerful it is with a bunch of practical examples (use root):

Lists all open files belonging to all active processes.

    :::bash
    lsof

Shows all files opened by the `www-data` user 

    :::bash
    lsof -u www-data 

Lists just all the PIDs of the processes opened by the `www-data` user

    :::bash
    lsof -t -u www-data

Kills all the activity for a particular user

    :::bash
    killall -9 `lsof -t -u username`

Lists all the files opened by the process with the `PID` 234

    :::bash
    lsof -p 234

Lists processes which are using a specific file.

    :::bash
    lsof -t /var/log/auth.log 

Lists all the log files in use.

    :::bash
    lsof +D /var/log

Lists all the opened files in a NFS folder

    :::bash 
    lsof +D -N /mnt/nfsstorage

Lists of the files opened by the processes whose command begins with the characters of "chrome".

    :::bash
    lsof -c chrome

Until here we were focused on regular files. But, what if we start listing special files like network files ?

Lists all network connections (Yes! Because everything in Unix is a file)

    :::bash
    lsof -i 

Lists all network connections on port 80

    :::bash
    lsof -i:80

Lists of all network connections on privileged ports,

    :::bash
    lsof -i:1-1024

Lists all IPv4 connections on the system

    :::bash
    lsof -i4

See localhost connections.

    :::Bash
    lsof -i 4@127.0.0.1 

Shows all listening TCP/UDP ports

    :::bash
    lsof -Pan -i tcp -i udp

Shows all connections on port 80 using a TCP socket.

    :::bash
    lsof -i TCP:80

Shows al TCP sockets listening on the system.

    :::bash
    lsof -i -sTCP:LISTEN

Shows all listening or established connection TCP ipv4 sockets.

    :::bash
    lsof -s TCP:ESTABLISHED,LISTEN -i4TCP

Check what services are still using old removed libraries and need to be reloaded.

    :::bash
    lsof -n | grep ssl | grep DEL

Find processes that need to be restarted after updating binaries.

    :::bash
    sudo lsof -d txt | grep '(deleted)'

And now let's get stared with the device files.

Find out what processes are using your webcam.

    :::bash
    lsof /dev/video0

Find out what processes are using your sound card.

    :::bash
    sudo lsof +D /dev/snd

The next one is one of my favorites. Displays all deleted files that are still open, and thus still occupy disk space, but are not part of any directory.
For example if you delete a big log file while it still opened by another process.

    :::bash
    lsof +L1

Now the definitive one. See how `lsof` can help you to recover a deleted file!

Imagie you deleted the `syslog` file accidentaly. As we said before, you can see some metadata from the deleted file using `lsof`.
Using the process (`PID`), and the file descriptor (`FD`) identifiers you can recover the file:

    :::bash
    COMMAND    PID       USER   FD   TYPE DEVICE SIZE/OFF NLINK    NODE NAME
    insync    2432 frommelmak   30u   REG    8,1     9252     0 4326104 /var/tmp/etilqs_KFgJC2dGc3A3p9r (deleted)
    soffice.b 3377 frommelmak   23u   REG    8,1     4096     0  789414 /home/frommelmak/.execoooAMcD6a (deleted)
    syslog-ng 1046 root         10w   REG    8,1     278428   0   20198 /var/log/syslog (deleted)

Now you can recover the file as follows:

    :::bash
    cat /proc/1046/fd/10 > /var/log/syslog

If you really want to release the space used by the syslog file without restart the `syslog` process, you can do something like this:

    :::bash
    > /var/log/syslog

Or just:

    :::bash
    echo "" > /var/log/syslog

Finally you can put the `lsof` command in a repeat mode using `-|+r`. The prefix `-` puts the lsof in endless mode. You need to send a control signal to exit.
With the `+` prefix, `lsof` ends when there's no output for the given parameters.

This article just cover the basics about `lsof`. For a complete list of features RTFM!
