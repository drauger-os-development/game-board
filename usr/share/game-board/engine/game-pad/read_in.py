#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  read_in.py
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
from inputs import get_gamepad
from math import atan, degrees
from time import sleep
from subprocess import Popen

def set_procname(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(10) #Note: One larger than the name (man prctl says that)
	buff.value = newname                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.

set_procname("game-board-engine")

while True:
	sleep(.1)
	x=None
	y=None
	rx=None
	ry=None
	z=0
	while z < 2:
		events=get_gamepad()
		for event in events:
			if event.code == "SYN_REPORT":
				continue
			elif event.code == "ABS_X":
				x=event.state
			elif event.code == "ABS_RX":
				rx=event.state
			elif event.code == "ABS_Y":
				y=event.state
			elif event.code == "ABS_RY":
				ry=event.state
			else:
				continue
			z=z+1
	#for the left analog stick
	if x != None:
		x=float(x)
	else:
		x=0
	if y != None:
		y=float(y)
	else:
		y=0
	if x == 0 and y == 0:
		angle="null"
	elif x == 0 and y != 0:
		if y > 0:
			angle=0
		elif y < 0:
			angle=180
	elif x != 0 and y == 0:
		if x > 0:
			angle=90
		elif x < 0:
			angle=270
	else:
		tan=y/x
		angle=atan(tan)
		angle=degrees(angle)
		if x > 0 and y > 0:
			angle=90-angle
		elif x > 0 and y < 0:
			angle=angle+90
		elif x < 0 and y < 0:
			angle=angle+180
		elif x < 0 and y > 0:
			angle=angle+270
	#for the right analog stick
	if rx != None:
		rx=float(rx)
	else:
		rx=0
	if ry != None:
		ry=float(ry)
	else:
		ry=0
	if rx == 0 and ry == 0:
		rangle="null"
	elif rx == 0 and ry != 0:
		if ry > 0:
			rangle=0
		elif ry < 0:
			rangle=180
	elif rx != 0 and ry == 0:
		if rx > 0:
			rangle=90
		elif rx < 0:
			rangle=270
	else:
		tan=ry/rx
		rangle=atan(tan)
		rangle=degrees(rangle)
		if rx > 0 and ry > 0:
			rangle=90-rangle
		elif rx > 0 and ry < 0:
			rangle=rangle+90
		elif rx < 0 and ry < 0:
			rangle=rangle+180
		elif rx < 0 and ry > 0:
			rangle=rangle+270
	#check if degree is greater 337.5 and less than 22.5
	if angle > 337.5 or angle < 22.5:
		if rangle > 330 or rangle < 30:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","h"])
		#check if degree is greater than 22.5 and less than 67.5
		elif rangle > 30 and rangle < 90:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","i"])
		#check if degree is greater than 67.5 and less than 112.5
		elif rangle > 90 and rangle < 150:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","j"])
		#check if degree is greater than 112.5 and less than 157.5
		elif rangle > 150 and rangle < 210:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","shift"])
		#check if degree is greater than 157.5 and less than 202.5
		elif rangle > 210 and rangle < 270:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","f"])
		#check if degree is greater than 202.5 and less than 247.5
		elif rangle > 270 and rangle < 330:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","g"])
	#check if degree is greater than 22.5 and less than 67.5
	elif angle > 22.5 and angle < 67.5:
		if rangle > 330 or rangle < 30:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","m"])
		#check if degree is greater than 22.5 and less than 67.5
		elif rangle > 30 and rangle < 90:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","n"])
		#check if degree is greater than 67.5 and less than 112.5
		elif rangle > 90 and rangle < 150:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","o"])
		#check if degree is greater than 112.5 and less than 157.5
		elif rangle > 150 and rangle < 210:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","shift"])
		#check if degree is greater than 157.5 and less than 202.5
		elif rangle > 210 and rangle < 270:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","k"])
		#check if degree is greater than 202.5 and less than 247.5
		elif rangle > 270 and rangle < 330:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","l"])
	#check if degree is greater than 67.5 and less than 112.5
	elif angle > 67.5 and angle < 112.5:
		if rangle > 330 or rangle < 30:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","r"])
		#check if degree is greater than 22.5 and less than 67.5
		elif rangle > 30 and rangle < 90:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","s"])
		#check if degree is greater than 67.5 and less than 112.5
		elif rangle > 90 and rangle < 150:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","t"])
		#check if degree is greater than 112.5 and less than 157.5
		elif rangle > 150 and rangle < 210:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","shift"])
		#check if degree is greater than 157.5 and less than 202.5
		elif rangle > 210 and rangle < 270:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","p"])
		#check if degree is greater than 202.5 and less than 247.5
		elif rangle > 270 and rangle < 330:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","q"])
	#check if degree is greater than 112.5 and less than 157.5
	elif angle > 112.5 and angle < 157.5:
		#U-Z
		if rangle > 0 or rangle < 51.428571429:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","u"])
		elif rangle > 51.428571429 and rangle < 102.857142857:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","v"])
		elif rangle > 102.857142857 and rangle < 154.285714286:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","w"])
		elif rangle > 154.285714286 and rangle < 205.714285714:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","shift"])
		elif rangle > 205.714285714 and rangle < 257.142857143:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","x"])
		elif rangle > 257.142857143 and rangle < 308.571428571:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","y"])
		elif rangle > 308.571428571 and rangle < 360:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","z"])
	#check if degree is greater than 157.5 and less than 202.5
	elif angle > 157.5 and angle < 202.5:
		#NUMBERS
		print()
	#check if degree is greater than 202.5 and less than 247.5
	elif angle > 202.5 and angle < 247.5:
		#SPECIAL CHARACTERS
		print()
	#check if degree is greater than 247.5 and less than 292.5
	elif angle > 247.5 and angle < 292.5:
		#BACKSPACE COMMAND
		Popen(["python","/usr/share/game-board/engine/conversion/type.py","backspace"])
	#check if degree is greater than 292.5 and less than 337.5
	elif angle > 292.5 and angle < 337.5:
		if rangle > 330 or rangle < 30:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","c"])
		#check if degree is greater than 22.5 and less than 67.5
		elif rangle > 30 and rangle < 90:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","d"])
		#check if degree is greater than 67.5 and less than 112.5
		elif rangle > 90 and rangle < 150:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","e"])
		#check if degree is greater than 112.5 and less than 157.5
		elif rangle > 150 and rangle < 210:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","shift"])
		#check if degree is greater than 157.5 and less than 202.5
		elif rangle > 210 and rangle < 270:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","a"])
		#check if degree is greater than 202.5 and less than 247.5
		elif rangle > 270 and rangle < 330:
			Popen(["python","/usr/share/game-board/engine/conversion/type.py","b"])
	Popen(["python3","/usr/share/game-board/engine/game-pad/translate-left.py",str(angle)])
	Popen(["python3","/usr/share/game-board/engine/game-pad/translate-right.py",str(rangle)])

