#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test.py
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
# ''' 
import pygame
import sys
from subprocess import Popen

def set_procname(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(10) #Note: One larger than the name (man prctl says that)
	buff.value = newname                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.

set_procname("gb-tester")

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                button = 0
                while button <= 12:
					if j.get_button(button):
						if button == 0:
							print(button)
							#Xbox: "a"
							#SWITCH: Y
							#PS3: Triangle
							break
						elif button == 1:
							print(button)
							#Xbox: "b"
							#SWITCH: B
							#PS3: Circle
							break
						elif button == 2:
							#Xbox: "x"
							#SWITCH: A
							#PS3: X
							print(button)
							break
						elif button == 3:
							print(button)
							#Xbox: "y"
							#SWITCH: X
							#PS3: Square
							break
						elif button == 4:
							print(button)
							#Xbox: "left_bumper"
							#SWITCH: LEFT BUMPER
							#PS3: Left Bumper
							break
						elif button == 5:
							print(button)
							#Xbox: "right_bumper"
							#SWITCH: RIGHT BUMPER
							#PS3: Right Bumper
							break
						elif button == 6:
							print(button)
							#Xbox: "back"
							#SWITCH: LEFT TRIGGER
							#PS3: Left Trigger
							break
						elif button == 7:
							print(button)
							#Xbox: "start"
							#SWITCH: RIGHT TRIGGER
							#PS3: Right Trigger
							break
						elif button == 8:
							print(button)
							#Xbox: "menu"
							#SWITCH: -
							#PS3: Select
							break
						elif button == 9:
							print(button)
							#Xbox: left analog button
							#SWITCH: +
							#PS3: Start
							break
						elif button == 10:
							#Xbox: right analog button
							#SWITCH: LEFT ANALOG BUTTON
							#PS3: Left Analog Button
							print(button)
							break
						elif button == 11:
							print(button)
							#Xbox: None
							#SWITCH: RIGHT ANALOG BUTTON
							#PS3: Right Analog Button
							break
						elif button == 12:
							#SWITCH: HOME
							#PS3: None
							#Xbox: None
							print(button)
							break
						elif button == 13:
							print(button)
							break
						else:
							print(button)
							break
					else:
						button = button+1
				
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
    
