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
#import all necessary modules
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
from os import system
import sys
import subprocess
import psutil

#create process name
def set_procname(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(10) #Note: One larger than the name (man prctl says that)
	buff.value = newname                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.

set_procname("gb-gui")

def check_proc_running(processName):
	#Check if there is any running process that contains the given name processName.
    #Iterate over the all the running process
	for proc in psutil.process_iter():
		try:
			# Check if process name contains the given name string.
			if processName.lower() in proc.name().lower():
				return True
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return False

def check():
	if not check_proc_running("gb-engine"):
		subprocess.Popen(['/home/batcastle/Dropbox/GitHub/game-board/usr/share/game-board/ui/error_enr.py'])
		exit(2)

class main(Gtk.Window):
	def __init__(self):
		#make the window
		Gtk.Window.__init__(self, title="game-board")
		self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)
		
		#get the size of the screen we are working with, so we can scale the images correctly based on that
		resuls = subprocess.Popen(['xrandr'],stdout=subprocess.PIPE).communicate()[0].split("current")[1].split(",")[0]
		width = resuls.split("x")[0].strip()
		height = resuls.split("x")[1].strip()
		width = int(width)
		height = int(height)
		width = width/2
		height = height/2
		
		#load the needed images into RAM and scale them
		null = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/game-board/assets/menu-right-null.png", width, height)
		print("null")
		left = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/game-board/assets/menu-left.png", width, height)
		print("left")
		f_j = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/game-board/assets/menu-right-f_j.png", width, height)
		print("f_j")
		k_o = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/game-board/assets/menu-right-k_o.png", width, height)
		print("k_o")
		p_t = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/game-board/assets/menu-right-p_t.png", width, height)
		print("p_t")
		u_z = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/game-board/assets/menu-right-u_z.png", width, height)
		print("u_z")
		a_e = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/game-board/assets/menu-right-a_e.png", width, height)
		print("a_e")
		#num = GdkPixbuf.Pixbuf.new_from_file("/usr/share/game-board/assets/menu-right-0_9.png")
		#special = GdkPixbuf.Pixbuf.new_from_file("/usr/share/game-board/assets/menu-right-special.png")
		
		image = null
		
		#set the images
		image1 = Gtk.Image()
		image1.set_from_pixbuf(left)
		self.grid.attach(image1, 1, 0, 1, 1)
		
		image2 = Gtk.Image()
		image2.set_from_pixbuf(image)
		self.grid.attach(image2, 2, 0, 1, 1)
	
		#self.change_image(left, a_e, f_j, k_o, p_t, u_z, null)
		#self.change_image(left, a_e, f_j, k_o, p_t, u_z, num, special, null)
		
	def change_image(self, left, a_e, f_j, k_o, p_t, u_z, null):
	#def change_image(self, left, a_e, f_j, k_o, p_t, u_z, num, special, null):
		while True:
			check()
			for str in sys.stdin:
				degree=str
				degree=degree.split()
				degree=degree[0]
				#check if degree is greater 337.5 and less than 22.5
				#F - J
				if degree > 337.5 or degree < 22.5:
					image = f_j
					image2.set_from_pixbuf(image)
				#check if degree is greater than 22.5 and less than 67.5
				#K - O
				elif degree > 22.5 and degree < 67.5:
					image = k_o
					image2.set_from_pixbuf(image)
				#check if degree is greater than 67.5 and less than 112.5
				#P - T
				elif degree > 67.5 and degree < 112.5:
					image = p_t
					image2.set_from_pixbuf(image)
				#check if degree is greater than 112.5 and less than 157.5
				#U - Z
				elif degree > 112.5 and degree < 157.5:
					image = u_z
					image2.set_from_pixbuf(image)
				#check if degree is greater than 157.5 and less than 202.5
				#0 - 9
				elif degree > 157.5 and degree < 202.5:
					image = num
					image2.set_from_pixbuf(image)
				#check if degree is greater than 202.5 and less than 247.5
				#SPECIAL
				elif degree > 202.5 and degree < 247.5:
					image = special
					image2.set_from_pixbuf(image)
				#check if degree is greater than 247.5 and less than 292.5
				#NULL
				elif degree > 247.5 and degree < 292.5:
					#BACKSPACE COMMAND
					image = null
					image2.set_from_pixbuf(image)
				#check if degree is greater than 292.5 and less than 337.5
				#A - E
				elif degree > 292.5 and degree < 337.5:
					image = a_e
					image2.set_from_pixbuf(image)
				#if none of the above match, change to null
				#NULL
				else:
					image = null
					image2.set_from_pixbuf(image)
def show():
	window = main()
	window.set_decorated(True)
	window.set_resizable(True)
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)

check()
show()
