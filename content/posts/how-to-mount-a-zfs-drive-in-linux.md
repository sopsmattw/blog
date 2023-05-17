Title: How to mount a ZFS drive in Linux
Date: 2012-02-08 14:39:12
Category: English
Tags: zfs, mount
Author: frommelmak

First: Plug the HDD into a SATA to USB adapter (obvious).
Then find the device:

    :::console
    sfdisk -l

In my case the device was `/dev/sdb1`

Install zfs-fuse for your distro:

**Debian**:

    :::console
    apt-get install zfs-fuse

**OpenSUSE**:

    :::console
    zypper install zfs-fuse

Start the zfs fuse daemon:

    :::bash
    /etc/init.d/zfs-fuse start
    super8:~ # zpool import
     pool: mypool
     id: 16911161038176216381
    state: ONLINE
    status: The pool was last accessed by another system.
    action: The pool can be imported using its name or numeric identifier and
        the '-f' flag.
       see: http://www.sun.com/msg/ZFS-8000-EY
    config:
        mypool  ONLINE
          disk/by-id/ata-ST3500418AS_5VM4KPXB-part2 ONLINE

Force the command using the -f flag and the pool identifier

    :::bash
    super8:~ # zpool import -f 16911161038176216381

Verify that everithing look normal:

    :::bash
    super8:~ # zpool list
    NAME SIZE ALLOC FREE CAP DEDUP HEALTH ALTROOT
    mypool  460G 2.97G 457G 0% 1.00x ONLINE -
 
And mount the filesystem in your desired mountpoint.

    :::bash
    zfs set mountpoint=/mnt/zfs mypool

Thats all, you are done! Your disk is available at `/mnt/zfs` mountpoint
Do whatever you need to do and finaly umount the device with this command:

    :::bash
    zfs umount mypool
