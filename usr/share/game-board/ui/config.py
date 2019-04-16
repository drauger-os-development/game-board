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

def set_procname(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(10) #Note: One larger than the name (man prctl says that)
	buff.value = newname                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.

set_procname("gb-config")

class main(Gtk.Window):
	def __init__(self):
		#make the window
		Gtk.Window.__init__(self, title="game-board")
		self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)
		
		main_text = Gtk.Label()
		main_text.set_markup("""	Set game-board configuration. <a href=\"www.github.com\"title=\"By default, we detect your screen resolution\">By default, we detect your screen resolution</a>	""")
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
			
			X = Gtk.Label()
			X.set_markup(""" X """)
			X.set_justify(Gtk.Justification.CENTER)
			self.grid.attach(X, 2, 5, 1, 1)
			
			self.height_dialog = Gtk.Entry()
			self.height_dialog.set_text(str(self.height))
			self.grid.attach(self.height_dialog, 3, 5, 1, 1)
			
		except Exception as e:
			print(e)
			self.checkbox_auto.set_active(True)
			self.height = 0
			self.width = 0
			
		self.checkbox_auto.connect("toggled", self.onautoclicked)
		self.grid.attach(self.checkbox_auto, 1, 3, 1, 1)
		
		button_save = Gtk.Button.new_with_label("Save Config")
		button_save.connect("clicked", self.onsaveclicked)
		self.grid.attach(button_save, 5, 7, 1, 1)
		
		button_cancel = Gtk.Button.new_with_label("Cancel")
		button_cancel.connect("clicked", self.oncancelclicked)
		self.grid.attach(button_cancel, 4, 7, 1, 1)
		
	def oncancelclicked(self, widget):
		exit(1)
		
	def onsaveclicked(self, widget):
		#delete old conf file
		active = self.checkbox_auto.get_active()
		width = self.width_dialog.get_text().decode('utf8')
		height = self.height_dialog.get_text().decode('utf8')
		home = os.environ["HOME"]
		if os.path.exists('%s/.config/game-board/game-board.conf' % (home)):
			os.remove('%s/.config/game-board/game-board.conf' % (home))
		#write variables to new conf file
		if not active:
			if not os.path.exists("%s/.config/game-board" % (home)):
				os.makedirs("%s/.config/game-board" % (home))
			save = open('%s/.config/game-board/game-board.conf' % (home), "a")
			save.write("width = %s\n" % (width))
			save.write("height = %s\n" % (height))
			save.close()
		exit(0)
		
	def onautoclicked(self, widget):
		if widget.get_active():
			print("ON")
		else:
			self.width_dialog = Gtk.Entry()
			self.width_dialog.set_text("Width of Monitor")
			self.grid.attach(self.width_dialog, 1, 5, 1, 1)
			
			X = Gtk.Label()
			X.set_markup(""" X """)
			X.set_justify(Gtk.Justification.CENTER)
			self.grid.attach(X, 2, 5, 1, 1)
			
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
