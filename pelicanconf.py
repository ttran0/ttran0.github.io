#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Truong Tran'
SITENAME = u"Truong's Website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('LinkedIn', 'https://www.linkedin.com/in/truong-tran'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
SITELOGO = 'https://media.licdn.com/mpr/mpr/shrinknp_400_400/AAEAAQAAAAAAAAlNAAAAJDUwZmRlZmQ1LWRkYmMtNDA0OC1hMzVkLTQ0NmEzN2E4MjI4MA.jpg'
MARKUP = ('md', 'ipynb')
THEME = './Flex'
PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
