#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  switch.py
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
"""Button layout config for Switch controllers"""
import game_pad.buttons as buttons


class Switch(buttons.Button_Interface):
    BUTTONS = {
        0: "A",
        1: "B",
        2: "X",
        3: "Y",
        4: "-",
        5: "home",
        6: "+",
        7: "left_joy_button",
        8: "right_joy_button",
        9: "left_bumper",
        10: "right_bumper",
        11: "dpad_up",
        12: "dpad_down",
        13: "dpad_left",
        14: "dpad_right",
        15: "screenshot"
    }

    joystick = {
                "left": {
                            "horizontal": {
                                            "id": 0,
                                            "location": 0
                                        },
                            "vertical": {
                                            "id": 1,
                                            "location": 0
                                        }
                        },
                "right": {
                            "horizontal": {
                                            "id": 2,
                                            "location": 0
                                        },
                            "vertical": {
                                            "id": 3,
                                            "location": 0
                                        }
                        }
            }

    def translation_layer(self, event):
        """Translate a button ID to an internal button type"""
        button = self.get_button_raw(event)
        if button == "X":
            return self.signals[0]
        if button == "B":
            return self.signals[1]
        if button == "Y":
            return self.signals[2]
        if button == "A":
            return self.signals[3]
        if button in ("left_bumper", "right_bumper", "left_joy_button", "right_joy_button"):
            return button
        if button == "screenshot":
            return self.signals[8]
        if button == "home":
            return self.signals[9]
        # Explicitly return None in case of a change in Python later
        return None

