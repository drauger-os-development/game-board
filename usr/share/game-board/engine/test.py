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
							#button = "a"
							#SWITCH: Y
							break
						elif button == 1:
							print(button)
							#button = "b"
							#SWITCH: B
							break
						elif button == 2:
							#button = "x"
							#SWITCH: A
							print(button)
							break
						elif button == 3:
							print(button)
							#button = "y"
							#SWITCH: X
							break
						elif button == 4:
							print(button)
							#button = "left_bumper"
							#SWITCH: LEFT BUMPER
							break
						elif button == 5:
							print(button)
							#button = "right_bumper"
							#SWITCH: RIGHT BUMPER
							break
						elif button == 6:
							print(button)
							#button = "back"
							#SWITCH: LEFT TRIGGER
							break
						elif button == 7:
							print(button)
							#button = "start"
							#SWITCH: RIGHT TRIGGER
							break
						elif button == 8:
							print(button)
							#button = "menu"
							#SWITCH: -
							break
						elif button == 9:
							print(button)
							#left analog button
							#SWITCH: +
							break
						elif button == 10:
							#right analog button
							#SWITCH: LEFT ANALOG BUTTON
							print(button)
							break
						elif button == 11:
							print(button)
							#button = None
							#SWITCH: RIGHT ANALOG BUTTON
							break
						elif button == 12:
							#SWITCH: HOME
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
    
