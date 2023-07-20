#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  buttons.py
#
#  Copyright 2023 Thomas Castleman <batcastle@draugeros.org>
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
"""Explain what this program does here!!!"""
from __future__ import print_function
import sys
import pygame


def __eprint__(*args, **kwargs):
    """Make it easier for us to print to stderr"""
    print(*args, file=sys.stderr, **kwargs)


if sys.version_info[0] == 2:
    __eprint__("Please run with Python 3 as Python 2 is End-of-Life.")
    exit(2)


class Button_Interface():
    """Button Interface and Abstraction Layer"""
    signals = [
        "upper", # Equivalent to "Y" on XBox
        "lower", # Equivalent to "A" on XBox
        "left", # Equivalent to "X" on XBox
        "right", # Equivalent to "B" on XBox
        "left_bumper",
        "right_bumper",
        "left_joy_button",
        "right_joy_button",
        "menu", # Equivalent to "Back" on XBox
        "select" # Equivalent to "Start" on XBox
    ]

    def get_button_raw(self, event):
        """Get Raw Button press from event"""
        try:
            return self.BUTTONS[event.button]
        except IndexError:
            raise ValueError("`button_id' is outside acceptable range for controller.")
