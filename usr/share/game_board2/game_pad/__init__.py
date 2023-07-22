#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __init__.py
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
"""Init File for Game-Pad"""
#  import game_pad.analog as analog
import game_pad.ps3 as ps3
import game_pad.switch as switch
import game_pad.ps4 as ps4
import game_pad.xbox as xbox
import game_pad.overrides as overrides
import common


def GamePad(js):
    """Initialize the gamepad as needed"""
    name = js.get_name().lower()
    js_type = None
    if "xbox" in name:
        js_type = xbox.Xbox
    elif ("ps3" in name) or ("playstation 3" in name):
        js_type = ps3.PlayStation3
    elif ("ps4" in name) or ("playstation 4" in name):
        js_type = ps4.PlayStation4
    elif "switch" in name:
        js_type = switch.Switch
    else:
        if name in game_pad.overrides.CONTROLLERS.keys():
            if game_pad.overrides.CONTROLLERS[name] == "xbox":
                js_type = xbox.Xbox
            elif game_pad.overrides.CONTROLLERS[name] == "ps3":
                js_type = ps3.PlayStation3
            elif game_pad.overrides.CONTROLLERS[name] == "ps4":
                js_type = ps4.PlayStation4
            elif game_pad.overrides.CONTROLLERS[name] == "switch":
                js_type = switch.Switch
            else:
                NotImplementedError(f"Device `{name}' overridden incorrectly")
        else:
            NotImplementedError(f"Device '{ name }' not recognized as joystick type. No override provided either. Cannot use.")

    class GamePad_class(js_type):
        """GamePad interaction abstraction class"""
        def __init__(self, js):
            """Initialize Class"""
            self.gamepad = js

        def get_button(self, event):
            """Get internal button type for event"""
            return self.translation_layer(event)

        def update_joystick(self, event):
            """Update Joystick location"""
            for each in self.joystick:
                if event.axis == self.joystick[each]["horizontal"]["id"]:
                    self.joystick[each]["horizontal"]["location"] = event.value
                elif event.axis == self.joystick[each]["vertical"]["id"]:
                    self.joystick[each]["vertical"]["location"] = event.value

        def get_joystick_location(self, js: str, formatting: bool) -> tuple:
            """Output current joystick location based off internal data
            as well as formatting settings.

            If `formatting' is True, return polar coordinates,
            if False, return rectangular."""
            if js not in self.joystick.keys():
                raise ValueError(f"{js} not a joystick. Please use either 'left' or 'right'")
            location = (self.joystick[js]["horizontal"]["location"],
                        self.joystick[js]["vertical"]["location"])
            if not formatting:
                return location
            return common.polar(location[0], location[1])


    return GamePad_class(js)



