##
#     Project: BlueWho
# Description: Information and notification of new discovered bluetooth devices.
#      Author: Fabio Castelli (Muflone) <webreg@vbsimple.net>
#   Copyright: 2009-2013 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import sys
import os.path
from xdg import BaseDirectory

# Application constants
APP_NAME = 'BlueWho'
APP_VERSION = '0.2'
APP_DESCRIPTION = 'Information and notification of new discovered bluetooth devices'
APP_ID = 'bluewho.muflone.com'
APP_URL = 'http://bluewho.muflone.com/'
APP_AUTHOR = 'Fabio Castelli'
APP_AUTHOR_EMAIL = 'webreg@vbsimple.net'
APP_COPYRIGHT = 'Copyright 2009-2013 %s' % APP_AUTHOR
# Other constants
DOMAIN_NAME = 'bluewho'
VERBOSE_LEVEL_QUIET = 0
VERBOSE_LEVEL_NORMAL = 1
VERBOSE_LEVEL_MAX = 2

# Paths constants
# If there's a file data/bluewho.png then the shared data are searched
# in relative paths, else the standard paths are used
if os.path.isfile(os.path.join('data', 'bluewho.png')):
  DIR_PREFIX = '.'
  DIR_LOCALE = os.path.join(DIR_PREFIX, 'locale')
  DIR_DOCS = os.path.join(DIR_PREFIX, 'doc')
else:
  DIR_PREFIX = os.path.join(sys.prefix, 'share', 'bluewho')
  DIR_LOCALE = os.path.join(sys.prefix, 'share', 'locale')
  DIR_DOCS = os.path.join(sys.prefix, 'share', 'doc', 'bluewho')
# Set the paths for the folders
DIR_DATA = os.path.join(DIR_PREFIX, 'data')
DIR_UI = os.path.join(DIR_PREFIX, 'ui')
DIR_SETTINGS = BaseDirectory.save_config_path(DOMAIN_NAME)
DIR_BT_ICONS = os.path.join(DIR_DATA, 'icons')
# Set the paths for the UI files
FILE_UI_MAIN = os.path.join(DIR_UI, 'main.glade')
FILE_UI_ABOUT = os.path.join(DIR_UI, 'about.glade')
FILE_UI_SERVICES = os.path.join(DIR_UI, 'services.glade')
FILE_UI_PREFERENCES = os.path.join(DIR_UI, 'preferences.glade')
FILE_UI_APPMENU = os.path.join(DIR_UI, 'appmenu.ui')
# Set the paths for the data files
FILE_ICON = os.path.join(DIR_DATA, 'bluewho.png')
FILE_TRANSLATORS = os.path.join(DIR_DOCS, 'translators')
FILE_LICENSE = os.path.join(DIR_DOCS, 'license')
FILE_RESOURCES = os.path.join(DIR_DOCS, 'resources')
FILE_BT_CLASSES = os.path.join(DIR_DATA, 'classes.txt')
# Set the paths for configuration files
FILE_SETTINGS_NEW = os.path.join(DIR_SETTINGS, 'settings.conf')
FILE_SETTINGS_DEVICES = os.path.join(DIR_SETTINGS, 'devices')
# Set bluetooth types
BT_DEVICETYPE_UNKNOWN = 0
BT_DEVICETYPE_COMPUTER = 1
BT_DEVICETYPE_PHONE = 2
BT_DEVICETYPE_NETWORK = 3
BT_DEVICETYPE_AUDIOVIDEO = 4
BT_DEVICETYPE_PERIPHERAL = 5
BT_DEVICETYPE_IMAGING = 6
BT_DEVICETYPE_MISCELLANEOUS = 7
BT_DEVICETYPE_TOY = 8
BT_DEVICETYPE_HEALTH = 9
# Preferences sections
PREFS_SECTION_MAIN = 'main window'
PREFS_SECTION_STARTUP = 'startup'
PREFS_SECTION_SCAN = 'scan'
PREFS_SECTION_NOTIFY = 'notify'
# Preferences options
PREFS_OPTION_RESTORE_SIZE = 'restore size'
PREFS_OPTION_WINLEFT = 'left'
PREFS_OPTION_WINTOP = 'top'
PREFS_OPTION_WINWIDTH = 'width'
PREFS_OPTION_WINHEIGHT = 'height'
PREFS_OPTION_STARTUPSCAN = 'startup scan'
PREFS_OPTION_RETRIEVE_NAMES = 'retrieve names'
PREFS_OPTION_RESOLVE_NAMES = 'resolve names'
PREFS_OPTION_SHOW_LOCAL = 'show local'
PREFS_OPTION_NOTIFICATION = 'show notification'
PREFS_OPTION_PLAY_SOUND = 'play sound'
