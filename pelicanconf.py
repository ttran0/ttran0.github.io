#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Truong Tran'
SITENAME = u"Truong's Website"
SITEURL = 'https://ttran0.github.io/'
SITESUBTITLE = "Mathematician & Data Science Practitioner"
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
# LINKS = ((),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/truong-tran'),
            ('github', 'https://github.com/ttran0'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Data Science Projects', '/category/projects.html'),
             ('Teaching','/category/teaching.html')
             ,)

STATIC_PATHS = ['pdfs']
# INDEX_SAVE_AS = 'about.html'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
SITELOGO = 'https://media.licdn.com/dms/image/C5103AQE-KW5gH0banw/profile-displayphoto-shrink_200_200/0?e=1529121600&v=beta&t=t7WWD9umuS0wPmwZbYJQBMajMvCBZHHWEbQuy67A_1M'
# SITELOGO = 'sitelogo.png'
MARKUP = ('md', 'ipynb')
THEME = './Flex'
JINJA_ENVIRONMENT = {}
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
