#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  overrides.py
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
"""Set specific controllers as a specific controller type"""
# device names MUST be lower-case
# if you over ride a device because it's not recognized, please open an issue
# at https://github.com/drauger-os-development/game-board with the device name
# and type
CONTROLLERS = {
    "my-power co.,ltd. usb gamepad": "ps3",
    "szmy-power co.,ltd. pc gamepad": "ps4"
}
