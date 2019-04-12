#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
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
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from multiprocessing import Process,Queue,Pipe
from /usr/share/game-board/engine/translate-left.py import convert_left
from /usr/share/game-board/engine/translate-right.py import convert_right
from os import system

def set_procname(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(10) #Note: One larger than the name (man prctl says that)
	buff.value = newname                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.

set_procname("game-board-gui")

class main(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="game-board")
		self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)
		
		image="/usr/share/game-board/assets/menu-right-null.png"
			
		image1 = Gtk.Image()
		image1.set_from_file("/usr/share/game-board/assets/menu-left.png")
		self.grid.attach(image1, 1, 0, 1, 1)
		
		image2 = Gtk.Image()
		image2.set_from_file(image)
		self.grid.attach(image2, 2, 0, 1, 1)
	
		self.change_image()
		
	def change_image(self):
		while True:
			parent_conn,child_conn = Pipe()
			receive = Process(target=convert_left, args=(child_conn,))
			receive.start()
			degree=parent_conn.recv()
			#check if degree is greater 337.5 and less than 22.5
			if degree > 337.5 or degree < 22.5:
				image="/usr/share/game-board/assets/menu-right-f_j.png"
				image2.set_from_file(image)
			#check if degree is greater than 22.5 and less than 67.5
			elif degree > 22.5 and degree < 67.5:
				image="/usr/share/game-board/assets/menu-right-k_o.png"
				image2.set_from_file(image)
			#check if degree is greater than 67.5 and less than 112.5
			elif degree > 67.5 and degree < 112.5:
				image="/usr/share/game-board/assets/menu-right-p_t.png"
				image2.set_from_file(image)
			#check if degree is greater than 112.5 and less than 157.5
			elif degree > 112.5 and degree < 157.5:
				image="/usr/share/game-board/assets/menu-right-u_z.png"
				image2.set_from_file(image)
			#check if degree is greater than 157.5 and less than 202.5
			elif degree > 157.5 and degree < 202.5:
				image="/usr/share/game-board/assets/menu-right-0_9.png"
				image2.set_from_file(image)
			#check if degree is greater than 202.5 and less than 247.5
			elif degree > 202.5 and degree < 247.5:
				image="/usr/share/game-board/assets/menu-right-special.png"
				image2.set_from_file(image)
			#check if degree is greater than 247.5 and less than 292.5
			elif degree > 247.5 and degree < 292.5:
				#BACKSPACE COMMAND
				image="/usr/share/game-board/assets/menu-right-null.png"
				image2.set_from_file(image)
			#check if degree is greater than 292.5 and less than 337.5
			elif degree > 292.5 and degree < 337.5:
				image="/usr/share/game-board/assets/menu-right-a_e.png"
				image2.set_from_file(image)
			#if none of the above match, change to null
			else:
				image="/usr/share/game-board/assets/menu-right-null.png"
				image2.set_from_file(image)
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
