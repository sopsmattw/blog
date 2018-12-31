Title: Increase volume size using Elastic Volumes 
Date: 2018-12-31 06:15:00
Category: English
Tags: ext4, lvm, ebs, aws, filesystem, maintenance
Author: frommelmak

On February 2017, AWS [announced](https://aws.amazon.com/blogs/aws/amazon-ebs-update-new-elastic-volumes-change-everything/) the availability of a new EBS feature called Elastic Volumes. The new feature allow you to increase the size, performance and type and of your EBS volumes while in use. In order to take adantage of this great featrue some requisites needs to be done.

  - The volume needs to be attached to a compatible instane: C1, C3, CC2, CR1, G2, I2, M1, M3 y R3 and later. 
  - The volume was attached to the instance after the November 1 of 2016.

To modify the volumen size just modify the volumen size using the Modify Volume action on the AWS Console.

![EBS volume resize](/images/ebs-resize.png)

Note: depending on the new size the action can take several hours.

Once the action completes, log into the instance and expand de filesystem. In my case since I'm using LVM I need to expand the physical and logical volumes.

    ::::bash
    pvdisplay
    pvscan
    pvresize /dev/xvdg
    pvdisplay
    lvdisplay
    lvextend -l +100%FREE /dev/vgroup2/volume

And finally the ext4 filesystem:

    ::::bash
    resize2fs /dev/vgroup2/volume
