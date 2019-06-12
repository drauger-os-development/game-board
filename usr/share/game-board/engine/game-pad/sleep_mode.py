#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  sleep_mode.py
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
from subprocess import Popen
from pynput.mouse import Listener
from setproctitle import setproctitle

setproctitle("gb-sleeper")

def on_click(x, y, button, pressed):
	if pressed and str(button) == "Button.left":
		try:
			Popen(["/usr/bin/game-board","-I"])
			Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","NOTICE", "game-board re-started from sleep", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
			
		except:
			Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","ERROR", "/usr/bin/game-board not present", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
		# Stop listener
		return False
        
try:
	Popen(["/usr/bin/killall","gb-engine1"])
	Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","NOTICE", "gb-engine1 killed", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
	
except:
	Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","ERROR", "gb-engine1 not running", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
	pass

try:
	Popen(["/usr/bin/killall","gb-engine2"])
	Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","NOTICE", "gb-engine2 killed", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
	
except:
	Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","ERROR", "gb-engine2 not running", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
	pass

try:
	Popen(["/usr/bin/killall","gb-gui"])
	Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","NOTICE", "gb-gui killed", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
	
except:
	Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","ERROR", "gb-gui not running", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
	pass
	
Popen(["/usr/bin/python3","/usr/share/game-board/engine/log.py","NOTICE", "Starting listener . . .", "/usr/share/game-board/engine/game-pad/sleep_mode.py"])
while True:
	with Listener(on_click=on_click) as listener:
		listener.join()
