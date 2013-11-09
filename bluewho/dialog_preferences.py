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

from gi.repository import Gtk
from bluewho.constants import *
from bluewho.functions import *

class DialogPreferences(object):
  def __init__(self, settings, winParent, show = False):
    self.settings = settings
    # Load the user interface
    builder = Gtk.Builder()
    builder.add_from_file(FILE_UI_PREFERENCES)
    # Obtain widget references
    self.dialog = builder.get_object("dialogPreferences")
    # Set various properties
    self.dialog.set_title(_('Preferences'))
    self.dialog.set_icon_from_file(FILE_ICON)
    self.dialog.set_transient_for(winParent)
    self.dialog.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)
    self.dialog.set_default_response(Gtk.ResponseType.OK)
    # Optionally show the dialog
    if show:
      self.show()

  def show(self):
    "Show the Preferences dialog"
    self.dialog.run()
    self.dialog.hide()

  def destroy(self):
    "Destroy the Preferences dialog"
    self.dialog.destroy()
    self.dialog = None
