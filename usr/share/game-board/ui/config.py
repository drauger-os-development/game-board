#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  config.py
#  
#  Copyright 2019 Thomas Castleman <contact@draugeros.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
#import all necessary modules
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import os
from subprocess import Popen
from setproctitle import setproctitle

Popen(["/usr/share/game-board/engine/log.py","NOTICE", "Configuration Editor Called", "/usr/share/game-board/ui/config.py"])

setproctitle("gb-config")

class main(Gtk.Window):
	def __init__(self):
		#make the window
		Gtk.Window.__init__(self, title="game-board")
		self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)
		
		main_text = Gtk.Label()
		main_text.set_markup("""	Set game-board configuration. <a href=\"file:///usr/share/game-board/assets/index.html\"title=\"Help and Info\">By default, we detect your screen resolution</a>	""")
		main_text.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(main_text, 1, 1, 4, 1)
		
		spacer = Gtk.Label()
		spacer.set_markup(""" """)
		spacer.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(spacer, 1, 2, 4, 1)
		
		self.checkbox_auto = Gtk.CheckButton()
		self.checkbox_auto = self.checkbox_auto.new_with_label("Auto-detect screen resolution")
		#set the default to selected if ~/.config/game-board/game-board.conf doesn't exist
		try:
			home = os.environ["HOME"]
			with open('%s/.config/game-board/game-board.conf' % (home)) as r:
				res = r.read()
			res = res.split()
			count = 0
			for each in res:
				self.width = [int(s) for s in res if s.isdigit()]
			self.height = self.width[1]
			self.width = self.width[0]
			
			self.width_dialog = Gtk.Entry()
			self.width_dialog.set_text(str(self.width))
			self.grid.attach(self.width_dialog, 1, 5, 1, 1)
			
			self.X = Gtk.Label()
			self.X.set_markup(""" X """)
			self.X.set_justify(Gtk.Justification.CENTER)
			self.grid.attach(self.X, 2, 5, 1, 1)
			
			self.height_dialog = Gtk.Entry()
			self.height_dialog.set_text(str(self.height))
			self.grid.attach(self.height_dialog, 3, 5, 1, 1)
			
		except:
			self.checkbox_auto.set_active(True)
			self.height = 0
			self.width = 0
			
		self.checkbox_auto.connect("toggled", self.onautoclicked)
		self.grid.attach(self.checkbox_auto, 1, 3, 1, 1)
		
		button_save = Gtk.Button.new_with_label("Save Config")
		button_save.connect("clicked", self.onsaveclicked)
		self.grid.attach(button_save, 5, 9, 1, 1)
		
		button_cancel = Gtk.Button.new_with_label("Cancel")
		button_cancel.connect("clicked", self.oncancelclicked)
		self.grid.attach(button_cancel, 4, 9, 1, 1)
		
		labeldropdown = Gtk.Label()
		labeldropdown.set_markup("\nDesignate what type of controller will be used (Default is Xbox):")
		labeldropdown.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(labeldropdown, 1, 7, 3, 1)
		
		self.dropdown = Gtk.ComboBoxText()
		self.dropdown.insert_text(0, "Switch/PlayStation 4")
		self.dropdown.insert_text(-1, "PlayStation 3")
		self.dropdown.insert_text(-1, "Xbox 360/One")
		self.grid.attach(self.dropdown, 1, 8, 3, 1)
	
	def oncancelclicked(self, widget):
		exit(1)
		
	def onsaveclicked(self, widget):
		#delete old conf file
		home = os.environ["HOME"]
		if os.path.exists('%s/.config/game-board/game-board.conf' % (home)):
			os.remove('%s/.config/game-board/game-board.conf' % (home))
		try:
			active = self.checkbox_auto.get_active()
			width = self.width_dialog.get_text().decode('utf8')
			height = self.height_dialog.get_text().decode('utf8')
			if not os.path.exists("%s/.config/game-board" % (home)):
				os.makedirs("%s/.config/game-board" % (home))
			save = open('%s/.config/game-board/game-board.conf' % (home), "a")
			save.write("width = %s\n" % (width))
			save.write("height = %s\n" % (height))
			save.close()
		#write variables to new conf file
		except:
			pass
		contents = self.dropdown.get_active_text()
		dest = "%s/.config/game-board/controller-buttons.py" % (home)
		if contents == "Switch/PlayStation 4":
			os.symlink("/usr/share/game-board/engine/game-pad/buttons_switch_ps4.py", dest)
		elif contents == "PlayStation 3":
			os.symlink("/usr/share/game-board/engine/game-pad/buttons_ps3.py", dest)
		elif contents == "Xbox 360/One":
			os.symlink("/usr/share/game-board/engine/game-pad/buttons_xbox.py", dest)
		else:
			os.symlink("/usr/share/game-board/engine/game-pad/buttons_xbox.py", dest)
		exit(0)
		
	def onautoclicked(self, widget):
		if widget.get_active():
			self.grid.remove(self.width_dialog)
			self.grid.remove(self.height_dialog)
			self.grid.remove(self.X)
		else:
			self.width_dialog = Gtk.Entry()
			self.width_dialog.set_text("Width of Monitor")
			self.grid.attach(self.width_dialog, 1, 5, 1, 1)
			
			self.X = Gtk.Label()
			self.X.set_markup(""" X """)
			self.X.set_justify(Gtk.Justification.CENTER)
			self.grid.attach(self.X, 2, 5, 1, 1)
			
			self.height_dialog = Gtk.Entry()
			self.height_dialog.set_text("Height of Monitor")
			self.grid.attach(self.height_dialog, 3, 5, 1, 1)
			
			self.show_all()
		
def show():
	window = main()
	window.set_decorated(True)
	window.set_resizable(True)
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)
	
show()
