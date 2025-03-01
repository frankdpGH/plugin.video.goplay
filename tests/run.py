#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Run any Kodi plugin:// URL on the commandline """

import os
import sys

# Add current working directory to import paths
cwd = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(os.path.realpath(__file__))), os.pardir))
sys.path.insert(0, cwd)
from resources.lib import addon  # noqa: E402  pylint: disable=wrong-import-position

if len(sys.argv) <= 1:
    print("%s: URI argument missing\nTry '%s plugin://plugin.video.goplay/' to test." % (sys.argv[0], sys.argv[0]))
    sys.exit(1)

# Also support bare paths like /recent/2
if not sys.argv[1].startswith('plugin://'):
    sys.argv[1] = 'plugin://plugin.video.goplay' + sys.argv[1]

# Split path and args
try:
    path, args = sys.argv[1].split('?', 1)
except ValueError:
    path, args = sys.argv[1], ''

print('** Running URI %s with args %s' % (path, args))
plugin = addon.routing
plugin.run([path, 0, args])
