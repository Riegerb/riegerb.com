#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brian Charles Rieger'
SITENAME = 'Brian Charles Rieger'
SITEURL = 'http://riegerb.com'
DESCRIPTION = 'Website for Brian Charles Rieger'

PATH = 'content'

DIRECT_TEMPLATES = ['index']

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['js']

THEME = 'themes/pelican-alchemy/alchemy'

# Blogroll
LINKS = ()

ICONS = (('github', 'https://github.com/Riegerb'),)

DEFAULT_PAGINATION = 10

HIDE_AUTHORS = True

DELETE_OUTPUT_DIRECTORY = True

LOAD_CONTENT_CACHE = False
