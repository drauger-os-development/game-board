#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  button_in.py
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

set_procname("gb-engine2")

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
							Popen(["python","/usr/share/game-board/engine/conversion/type.py","space"])
							break
						elif button == 1:
							print(button)
							#button = "b"
							try:
								Popen(["/usr/bin/killall","gb-engine1"])
	
							except:
								pass
							
							try:
								Popen(["/usr/bin/killall","gb-gui"])
	
							except:
								pass
							
							try:
								Popen(["/usr/bin/killall","gb-engine2"])
	
							except:
								pass
								
							exit(0)
							break
						elif button == 2:
							#button = "x"
							print(button)
							Popen(["python","/usr/share/game-board/engine/conversion/type.py","enter"])
							break
						elif button == 3:
							print(button)
							#button = "y"
							Popen(["python","/usr/share/game-board/engine/conversion/type.py","tab"])
							break
						elif button == 4:
							print(button)
							#button = "left_bumper"
							Popen(["python","/usr/share/game-board/engine/conversion/type.py","left"])
							break
						elif button == 5:
							print(button)
							#button = "right_bumper"
							Popen(["python","/usr/share/game-board/engine/conversion/type.py","right"])
							''''''
							break
						elif button == 6:
							print(button)
							#button = "back"
							try:
								Popen(["/usr/bin/killall","gb-gui"])
	
							except:
								#restart GUI
								print("GUI not running!")
							break
						elif button == 7:
							print(button)
							#button = "start"
							Popen(["/usr/share/game-board/engine/game-pad/sleep_mode.py"])
							break
						elif button == 8:
							print(button)
							#button = "menu""
							Popen(["python","/usr/share/game-board/ui/config.py"])
							break
						elif button == 9:
							print(button)
							#left analog button
							Popen(["python","/usr/share/game-board/engine/conversion/type.py","backspace"])
							break
						elif button == 10:
							#right analog button
							print(button)
							stdin = sys.stdin
							stdin = stdin.split()
							char = stdin[0]
							printed = 0
							try:
								float(char)
								try:
									int(char)
									printed = 1
								except:
									printed = 0
							except:
								printed = 1
							if printed == 1:
								char = str(char)
								Popen(["python","/usr/share/game-board/engine/conversion/type.py",char])
							break
						else:
							print(button)
							button = None
							break
					else:
						button = button+1
				
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
    
'''
import os
from subprocess import Popen

def set_procname(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(10) #Note: One larger than the name (man prctl says that)
	buff.value = newname                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.

set_procname("gb-engine2")

if os.path.exists('%s/.config/game-board/game-board.conf' % (home)):
	with open('%s/.config/game-board/game-board.conf' % (home)) as r:
		res = r.read()
	res = res.split()
	controller_type = res[8]
	controller_type = str(controller_type)
	controller_type = controller_type.lower()
	if controller_type == "xbox360":
		Popen[("python3","/usr/share/game-board/engine/game-pad/buttons_x360.py")]
	elif controller_type == "xboxone" or controller_type == "xbox1":
		Popen[("python3","/usr/share/game-board/engine/game-pad/buttons_x1.py")]
	elif controller_type == "ps3":
		Popen[("python3","/usr/share/game-board/engine/game-pad/buttons_ps3.py")]
	elif controller_type == "ps4":
		Popen[("python3","/usr/share/game-board/engine/game-pad/buttons_ps4.py")]

'''
