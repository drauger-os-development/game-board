#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  circle.py
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
"""game-board2 menu library"""
from __future__ import print_function
import sys
import math
import pygame
import copy
from time import sleep
import common


def __eprint__(*args, **kwargs):
    """Make it easier for us to print to stderr"""
    print(*args, file=sys.stderr, **kwargs)


if sys.version_info[0] == 2:
    __eprint__("Please run with Python 3 as Python 2 is End-of-Life.")
    exit(2)

# get length of argv
ARGC = len(sys.argv)


class Circle:
    """Define our Radial Menus"""
    def __init__(self, radius, settings, offset, background, surface):
        """Init system"""
        # define our class attributes
        self.radius = int(radius)
        self.slices = settings["slices"]
        self.slice_size = 360 / self.slices
        self.offset_coords = tuple(offset)
        self.color = tuple(settings["de_color"])
        self.selected_color = tuple(settings["color"])
        self.background = tuple(background)
        #  self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.image = surface
        #  self.image.fill(self.background)
        self.rect = self.image.get_rect()
        self.rect.x = self.offset_coords[0]
        self.rect.y = self.offset_coords[1]
        #  print(f"Offset: {offset}")
        self.rim = self.calculate_rim()
        #  print(f"Rim, pre-offset: {self.rim}")
        self.apply_offset()
        #  print(f"Rim, post-offset: {self.rim}")

    def draw(self, window, selected_slice=None) -> None:
        """Draw points on screen with Pygame"""
        if selected_slice == None:
            for each in self.rim:
                pygame.draw.line(window, self.color, self.rim[each][0],
                                 self.rim[each][1], width=10)
                pygame.draw.line(window, self.color, self.offset_coords,
                                 self.rim[each][0], width=10)
                #  sleep(1)
        else:
            for each in self.rim:
                if selected_slice not in self.rim[each]:
                    pygame.draw.line(window, self.color,
                                     self.rim[each][0], self.rim[each][1],
                                     width=10)
                    pygame.draw.line(window, self.color,
                                     self.offset_coords, self.rim[each][0],
                                     width=10)
                else:
                    if selected_slice == self.rim[each][0]:
                        pygame.draw.line(window, self.color,
                                        self.rim[each][0], self.rim[each][1],
                                        width=10)
                        pygame.draw.line(window, self.selected_color,
                                        self.offset_coords, self.rim[each][0],
                                        width=10)
                    else:
                        pygame.draw.line(window, self.selected_color, self.rim[each][0],
                                        self.rim[each][1], width=10)
                        pygame.draw.line(window, self.selected_color, self.offset_coords,
                                        self.rim[each][0], width=10)


    def update(self, js_coords, window):
        """Update points on screen"""
        selected_slice = None
        quardent = None
        skipper = False
        check_points = []
        # calculate quadrant we are working in
        # During this section, we are working on the joystick coordinate plane
        # this follows traditional Euclidean geometry, except the Y-axis is inverted
        if js_coords[0] > 0:
            if js_coords[1] > 0:
                quadrent = 4
            else:
                quadrent = 1
        else:
            if js_coords[1] > 0:
                quadrent = 3
            else:
                quadrent = 2
        # this section follows traditional Euclidean geometry with an offset
        # origin
        for each in self.rim:
            if quadrent == 1:
                if self.rim[each][0][0] > self.offset_coords[0]:
                    if self.rim[each][0][1] > self.offset_coords[1]:
                        check_points.append(self.rim[each][0])
            elif quadrent == 2:
                if self.rim[each][0][0] < self.offset_coords[0]:
                    if self.rim[each][0][1] > self.offset_coords[1]:
                        check_points.append(self.rim[each][0])
            elif quadrent == 3:
                if self.rim[each][0][0] < self.offset_coords[0]:
                    if self.rim[each][0][1] < self.offset_coords[1]:
                        check_points.append(self.rim[each][0])
            elif quadrent == 4:
                if self.rim[each][0][0] > self.offset_coords[0]:
                    if self.rim[each][0][1] < self.offset_coords[1]:
                        check_points.append(self.rim[each][0])
        # apply offset to Joystick coordinates
        #  js_coords[0]+=self.offset_coords[0]
        #  js_coords[1]+=self.offset_coords[1]
        # actually do the math to check placement
        # calculate slope of joystick coordinates
        # we need to make sure this jives with the coordinate system of the
        # rest of the GUI, so we need to invert the sign of the Y-axis
        try:
            js_slope = (js_coords[1] * -1) / js_coords[0]
        except ZeroDivisionError:
            self.draw(window)
            skipper = True
        direction = None
        if not skipper:
            slope_1 = check_points[0][1] / check_points[0][0]
            try:
                slope_2 = check_points[1][1] / check_points[1][0]
            except IndexError:
                # this happens if there is only one radial line in the quadrant.
                # this is not only a recoverable error, we can take advantage of this
                # to get better performance
                if js_slope > slope_1:
                    selected_slice = check_points[0]
                else:
                    for each in self.rim:
                        if self.rim[each][0] == check_points[0]:
                            selected_slice = self.rim[each][1]
                            break
                skipper = True
        if not skipper:
            if (slope_1 > slope_2):
                direction = True
            elif (slope_1 < slope_2):
                direction = False
            del slope_1, slope_2, js_coords, each
            for each in check_points:
                # calculate slope of points in quadrant
                slope = each[1] / each[0]
                # check where the slope of joystick coordinates lies in relation
                # to slope of points
                # select applicable slice
                if direction:
                    if slope >= js_slope:
                        selected_slice = each
                    elif slope < js_slope:
                        break
                else:
                    if slope <= js_slope:
                        selected_slice = each
                    elif slope > js_slope:
                        break
        if selected_slice is not None:
            self.draw(window, selected_slice=selected_slice)

    def calculate_rim(self) -> None:
        """Calculate the points along our rim"""
        rim = {}
        for slices in range(self.slices):
            rim[slices] = []
        angle = self.slice_size
        for slices in range(self.slices):
            point = common.rect(self.radius, angle)
            if len(rim[slices]) < 2:
                rim[slices].append(copy.copy(point))
            try:
                if len(rim[slices-1]) < 2:
                    rim[slices-1].append(copy.copy(point))
            except KeyError:
                pass
            angle+=self.slice_size
        rim[self.slices - 1].append(copy.copy(rim[0][0]))
        return rim

    def apply_offset(self) -> None:
        """Apply offset so the menu draws fully on-screen"""
        for each in self.rim:
            for each1 in enumerate(self.rim[each]):
                self.rim[each][each1[0]][0]+=self.offset_coords[0]
                self.rim[each][each1[0]][1]+=self.offset_coords[1]

