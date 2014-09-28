#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marcos Mart\xednez'
SITENAME = u'frommelmak'
SITEURL = ''
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'es'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_DIR = 'posts'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

##############################
# CUSTOM SETTINGS (frommelmak)
##############################

DISPLAY_CATEGORIES_ON_MENU = False 

# Don't forget to install "pip install mdx_video"
MD_EXTENSIONS = ['codehilite', 'extra', 'video']
TYPOGRIFY = True

THEME = "themes/plumage"
STATIC_PATHS = [
    'images',
]
IMAGE_PATH = "images"
#THUMBNAIL_SIZES = {
#    'thumbnail': '462x?',
#}
#DEFAULT_TEMPLATE = """<a href="{url}" class="zoomable" title="{filename}"><img src="{thumbnail}" alt="{filename}"></a>"""
SITE_THUMBNAIL = "images/avatar.png"
SITE_THUMBNAIL_TEXT = "Alien Life Form"
SITESUBTITLE = "Yet another Melmacian interested in technology..."

#PAGE_DIR = 'pages'

PLUGIN_PATH = "pelican-plugins"
PLUGINS = ["neighbors","related_posts"]

RELATED_POSTS_MAX = 3

MENUITEMS = (
    ('Home', '/'),
    ('Wiki', 'http://wiki.frommelmak.com'),
    ('Old Blog', 'http://old.frommelmak.com'),
)
TWITTER_USERNAME = "frommelmak"
GITHUB_URL = "https://github.com/frommelmak"

SOCIAL_TITLE = "Contact"
SOCIAL = (
    ('@frommelmak', 'http://twitter.com/frommelmak'),
)

LINKS_TITLE = "Profiles"
LINKS = (
#    ('PDF resume', 'http://docs.google.com/document/export?format=pdf&amp;id=1XaJgwRAhxHDuBSD-JqE--8WKGx0uTasa6IOU4IFBeKg'),
    ('LinkedIn', 'http://linkedin.com/in/marcosmartinezjimenez'),
    ('GitHub', 'http://github.com/frommelmak'),
    ('Youtube', 'http://www.youtube.com/user/melmak'),
)

#CATEGORY_URL = 'category/{slug}/'
#CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

ARTICLE_EDIT_LINK = 'https://github.com/frommelmak/blog/edit/master/content/posts/%(slug)s.md'
GOOGLE_SEARCH = 'partner-pub-2082790787711438:7148578903'
#LEFT_SIDEBAR=""" """
DISQUS_SITENAME = "frommelmak"
