#!/usr/bin/env python
#
# https://www.dexterindustries.com
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/DI_Sensors/blob/master/LICENSE.md
#
# Python example program for the Dexter Industries Light Color Sensor

from __future__ import print_function
from __future__ import division

import math
from time import sleep
from di_sensors.easy_light_color_sensor import EasyLightColorSensor

my_lcs = EasyLightColorSensor(led_state = True)

# Common colors coordinates (CIE xy and RGB)
COLOR_TABLE = {"Red":           {"x": 0.64,  "y": 0.33,  "r": 255, "g": 0,   "b": 0},
                "Green":         {"x": 0.3,   "y": 0.6,   "r": 0,   "g": 255, "b": 0},
                "Blue":          {"x": 0.15,  "y": 0.06,  "r": 0,   "g": 0,   "b": 255},
                "Yellow":        {"x": 0.419, "y": 0.505, "r": 255, "g": 255, "b": 0},
                "Magenta":       {"x": 0.321, "y": 0.154, "r": 255, "g": 0,   "b": 255},
                "Cyan":          {"x": 0.225, "y": 0.329, "r": 0,   "g": 255, "b": 255},
                "Deep pink":     {"x": 0.466, "y": 0.238, "r": 255, "g": 20,  "b": 147},
                "Orange":        {"x": 0.5,   "y": 0.441, "r": 255, "g": 165, "b": 0},
                "Saddle brown":  {"x": 0.526, "y": 0.399, "r": 139, "g": 69,  "b": 19},
                "Grey / White":  {"x": 0.313, "y": 0.329, "r": 255, "g": 255, "b": 255},
                "Black":         {"x": 0,     "y": 0,     "r": 0,   "g": 0,   "b": 0}}




def getColor():
    # Read the R, G, B, C color values
    red, green, blue, clear = my_lcs.safe_raw_colors()

    # Print the values
    #print("Red: {:5.3f} Green: {:5.3f} Blue: {:5.3f} Clear: {:5.3f}".format(red, green, blue, clear))
    """ Reads the measured color and converts it as CIE x,y coordinates.

    See http://www.techmind.org/colour/ and https://en.wikipedia.org/wiki/CIE_1931_color_space for more information.

    :return: a (x, y) tuple
    """
    div = 0.17697
##    x_bar = -0.14282 * red + 1.54924 * green + -0.95641 * blue
##    y_bar = -0.32466 * red + 1.57837 * green + -0.73191 * blue
##    z_bar = -0.68202 * red + 0.77073 * green + 0.563320 * blue

    x_bar = (0.49000 * red + 0.31000 * green + 0.20000 * blue)/ div
    y_bar = (div * red + 0.81240 * green + 0.01063 * blue)/ div
    z_bar = (0.00000 * red + 0.01000 * green + 0.99000 * blue)/ div
    x = x_bar / (x_bar + y_bar + z_bar + 0.00001)
    y = y_bar / (x_bar + y_bar + z_bar + 0.00001)

    closest_color = None
    closest_distance = 1
    for current_color in COLOR_TABLE:
        current_coordinates = COLOR_TABLE[current_color]
        current_dist = math.sqrt(
                (current_coordinates["y"] - y)**2 + (current_coordinates["x"] - x)**2)
        if current_dist < closest_distance:
            closest_color = current_color
            closest_distance = current_dist

    return closest_color
