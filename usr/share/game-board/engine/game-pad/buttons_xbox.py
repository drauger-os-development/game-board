#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  buttons_xbox.py
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
#  This script is for Xbox One and Xbox 360 controllers, specificly the buttons on it.
#  The analog sticks are handled for all controllers in analog_in.py
#
import pygame
import sys
from subprocess import Popen
from conversion import type_out
from setproctitle import setproctitle

setproctitle("gb-engine2")

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
							type_out("space")
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
							type_out("enter")
							break
						elif button == 3:
							print(button)
							#button = "y"
							type_out("tab")
							break
						elif button == 4:
							print(button)
							#button = "left_bumper"
							type_out("left")
							break
						elif button == 5:
							print(button)
							#button = "right_bumper"
							type_out("right")
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
							Popen(["/usr/bin/python3","/usr/share/game-board/engine/game-pad/sleep_mode.py"])
							break
						elif button == 8:
							print(button)
							#button = "menu""
							Popen(["/usr/bin/python3","/usr/share/game-board/ui/config.py"])
							break
						elif button == 9:
							print(button)
							#left analog button
							type_out("backspace")
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
								type_out(char)
							break
						else:
							print(button)
							break
					else:
						button = button+1
				
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
