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

### Common colors coordinates (CIE xy and RGB)
##COLOR_TABLE = {"Red":           {"x": 0.64,  "y": 0.33,  "r": 255, "g": 0,   "b": 0},
##                "Green":         {"x": 0.33,   "y": 0.33,   "r": 200,   "g": 255, "b": 200},
##               # "Blue":          {"x": 0.15,  "y": 0.06,  "r": 0,   "g": 0,   "b": 255},
##                "Yellow":        {"x": 0.419, "y": 0.505, "r": 255, "g": 255, "b": 0},
##               # "Magenta":       {"x": 0.321, "y": 0.154, "r": 255, "g": 0,   "b": 255},
##                "Blue":          {"x": 0.225, "y": 0.329, "r": 0,   "g": 255, "b": 255},
##               # "Deep pink":     {"x": 0.466, "y": 0.238, "r": 255, "g": 20,  "b": 147},
##                "Orange":        {"x": 0.5,   "y": 0.441, "r": 255, "g": 165, "b": 0},
##               # "Saddle brown":  {"x": 0.526, "y": 0.399, "r": 139, "g": 69,  "b": 19},
##                "White":  {"x": 0.313, "y": 0.329, "r": 255, "g": 255, "b": 255},
##                "Black":         {"x": 0.5,     "y": 0.33,     "r": 0,   "g": 200,   "b": 200}}

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
                   "White":  {"x": 0.313, "y": 0.329, "r": 255, "g": 255, "b": 255},
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
    x_bar = -0.14282 * red + 1.54924 * green + -0.95641 * blue
    y_bar = -0.32466 * red + 1.57837 * green + -0.73191 * blue
    z_bar = -0.68202 * red + 0.77073 * green + 0.563320 * blue

##    x_bar = (0.49000 * red + 0.31000 * green + 0.20000 * blue)/ div
##    y_bar = (div * red + 0.81240 * green + 0.01063 * blue)/ div
##    z_bar = (0.00000 * red + 0.01000 * green + 0.99000 * blue)/ div
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


# #!/usr/bin/env python
# #
# # Library for Grove - I2C Color Sensor V2(https://www.seeedstudio.com/Grove-I2C-Color-Sensor-V2-p-2890.html)
# #
# # This is the library for Grove Base Hat which used to connect grove sensors for raspberry pi.
# #
#
# '''
# ## License
#
# The MIT License (MIT)
#
# Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
# Copyright (C) 2018  Seeed Technology Co.,Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# '''
# import time
# import math
# from grove.i2c import Bus
#
#
# _CMD      = 0x80
# _AUTO     = 0x20
#
# _ENABLE   = 0x00
# _ATIME    = 0x01
# _WTIME    = 0x03
# _AILT     = 0x04
# _AIHT     = 0x06
# _PERS     = 0x0C
# _CONFIG   = 0x0D
# _CONTROL  = 0x0F
# _ID       = 0x12
# _STATUS   = 0x13
# _CDATA    = 0x14
# _RDATA    = 0x16
# _GDATA    = 0x18
# _BDATA    = 0x1A
#
# _AIEN       = 0x10
# _WEN        = 0x08
# _AEN        = 0x02
# _PON        = 0x01
#
# _GAINS  = (1, 4, 16, 60)
#
#
#
# """Driver for Grove I2C Color Sensor (TCS34725)"""
#
# def __init__(self, bus=None, address=0x29):
#     self.address = address
#     self.bus = Bus(bus)
#
#     self.awake = False
#
#     if self.id not in (0x44, 0x4D):
#         raise ValueError('Not find a Grove I2C Color Sensor V2')
#
#     self.set_integration_time(24)
#     self.set_gain(1)
#
# def wakeup(self):
#     enable = self._read_byte(_ENABLE)
#     self._write_byte(_ENABLE, enable | _PON | _AEN)
#     time.sleep(0.0024)
#
#     self.awake = True
#
# def sleep(self):
#     enable = self._read_byte(_ENABLE)
#     self._write_byte(_ENABLE, enable & ~_PON)
#
#     self.awake = False
#
# def is_awake(self):
#     return self._read_byte(_ENABLE) & _PON
#
# def set_wait_time(self, t):
#     pass
#
# @property
# def id(self):
#     return self._read_byte(_ID)
#
# @property
# def integration_time(self):
#     steps = 256 - self._read_byte(_ATIME)
#     return steps * 2.4
#
# def set_integration_time(self, t):
#     """Set the integration time of the sensor"""
#     if t < 2.4:
#         t = 2.4
#     elif t > 614.4:
#         t = 614.4
#
#     steps = int(t / 2.4)
#     self._integration_time = steps * 2.4
#     self._write_byte(_ATIME, 256 - steps)
#
# @property
# def gain(self):
#     """The gain control. Should be 1, 4, 16, or 60.
#     """
#     return _GAINS[self._read_byte(_CONTROL)]
#
# def set_gain(self, gain):
#     if gain in _GAINS:
#         self._write_byte(_CONTROL, _GAINS.index(gain))
#
# @property
# def raw(self):
#     """Read RGBC registers
#     return 16 bits red, green, blue and clear data
#     """
#
#     if not self.awake:
#         self.wakeup()
#
#     while not self._valid():
#         time.sleep(0.0024)
#
#     data = tuple(self._read_word(reg) for reg in (_RDATA, _GDATA, _BDATA, _CDATA))
#     return data
#
# @property
# def rgb(self):
#     """Read the RGB color detected by the sensor.  Returns a 3-tuple of
#     red, green, blue component values as bytes (0-255).
#     """
#     r, g, b, clear = self.raw
#     if clear:
#         r = int(255 * r / clear)
#         g = int(255 * g / clear)
#         b = int(255 * b / clear)
#     else:
#         r, g, b = 0, 0, 0
#     return r, g, b, clear
#
# @property
# def getClear(self):
#     """Read the RGB color detected by the sensor.  Returns a 3-tuple of
#     red, green, blue component values as bytes (0-255).
#     """
#     r, g, b, clear = self.raw
#     if clear:
#         r = int(255 * r / clear)
#         g = int(255 * g / clear)
#         b = int(255 * b / clear)
#     else:
#         r, g, b = 0, 0, 0
#     return clear
#
# def _valid(self):
#     """Check if RGBC is valid"""
#     return self._read_byte(_STATUS) & 0x01
#
# def _read_byte(self, address):
#     command = _CMD | address
#     return self.bus.read_byte_data(self.address, command)
#
# def _read_word(self, address):
#     command = _CMD | _AUTO | address
#     return self.bus.read_word_data(self.address, command)
#
# def _write_byte(self, address, data):
#     command = _CMD | address
#     self.bus.write_byte_data(self.address, command, data)
#
# def _write_word(self, address, data):
#     command = _CMD | _AUTO | address
#     data = [(data >> 8) & 0xFF, data & 0xFF]
#     self.bus.write_i2c_block_data(self.address, command, data)
#
#
# def getColor(self):
#     """ Reads the measured color and maps it to the nearest color present in COLOR_TABLE.
#
#     Warning: current implementation does not work well with white / grey / black or dark colors.
#
#     :return: The color name used as a key in COLOR_TABLE.
#     """
# ##        xy = self.read_xy()
# ##        r, g, b, clear = self.raw
# ##        closest_color = None
# ##        closest_distance = math.sqrt(2)
# ##        for current_color in self.COLOR_TABLE:
# ##            current_coordinates = self.COLOR_TABLE[current_color]
# ##            current_dist = math.sqrt(
# ##                    (current_coordinates["r"]/255 - r/clear)**2 + (current_coordinates["g"]/255 - g/clear)**2 + (current_coordinates["b"]/255 - b/clear)**2)
# ##            if current_dist < closest_distance:
# ##                closest_color = current_color
# ##                closest_distance = current_dist
# ##
# ##        return closest_color
#
#     r, g, b, clear= self.rgb
#     color_read = None
#
#     if (r > 100):
#         if (b < 70):
#             if (g > 90):
#                 color_read = 'Yellow'
#             elif ( g < 70):
#                 color_read = 'Red'
#             else:
#                 color_read = 'Orange'
#     elif (g > 100):
#         color_read = 'Green'
#     elif(b > 100):
#         if (r > 75):
#             color_read = 'Purple'
#         else:
#             color_read = 'Blue'
#     elif(g,b < 100):
#         if (r > 90):
#             color_read = 'Pink'
#         elif(g >= b):
#             color_read = 'Black'
#         else:
#             color_read = 'White'
#
#     return color_read
#
#
# # def main():
# #
# # ##    print('Raw data of red-filtered, green-filtered, blue-filtered and unfiltered photodiodes')
# #     while True:
# #         colorSensor = colorSensor
# #         colorSensor.set_gain(1)
# #         r, g, b, clear= sensor.rgb
# # ##        r, g, b, clear = sensor.raw
# #         color = colorSensor.getColor()
# #         print((r,g,b,clear))
# # ##        print((r, g, b, sszzzzzclear))
# #         print(color)
# #         time.sleep(1.0)
# #
# # if __name__ == '__main__':
# #     main()
