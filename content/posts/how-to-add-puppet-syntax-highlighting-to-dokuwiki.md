Title: How to add Puppet syntax highlighting to Dokuwiki
Date: 2013-07-05 12:50:40
Category: English
Tags: puppet, dokuwiki
Author: frommelmak

As you probably know, Dokuwiki relies on [GeSHI](http://qbnz.com/highlighter/) for syntax highlighting. Unfortunately, the current version of GeSHI does not support Puppet language. Nevertheless GeSHI allows you to add new languages easily by creating new language files, so to add Puppet support you just need to get a languaje file for Puppet and copy it into the inc/geshi folder.

I've found this [Puppet GeSHI file](https://github.com/jasonhancock/geshi-language-files/blob/master/puppet.php) that works fine in Dokuwiki.
