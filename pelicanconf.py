#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Carlos Molina'
SITENAME = 'Carlos Molina'
SITEURL = 'https://cmolinaord.github.io'
SIDEBAR_DIGEST = 'Physicist and Aerospace Engineering Student'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'English'

THEME = 'themes/pelican-blue'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Other links
LINKS = (('SUGUS ETSII', 'https://sugus.eii.us.es'),
		('My Wikipedia userpage (es)', 'https://es.wikipedia.org/wiki/Usuario:Kamelox'),)

# Social widget
SOCIAL = 	(('GitHub', 'https://github.com/cmolinaord'),
			('Twitter', 'https://twitter.com/cmolina_ord'),
			('Flickr', 'https://www.flickr.com/photos/cmolina_remo'),
			('Linkedin', 'https://www.linkedin.com/in/cmolinaord'),
			('Instagram', 'https://www.instagram.com/contandolafisica/'),)

TWITTER_USERNAME = 'cmolina_ord'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['pdf', 'extra/favicon.ico', 'images']
EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'}
}

DISQUS_SITENAME = "https-cmolinaord-github-io"
