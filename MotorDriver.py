#!/usr/bin/env python
#
# GrovePi Library for using the Grove - I2C Motor Driver(http://www.seeedstudio.com/depot/Grove-I2C-Motor-Driver-p-907.html)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this library?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#

# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/GrovePi/blob/master/LICENSE

import time,sys
import RPi.GPIO as GPIO
import smbus

# use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

class motor_driver:

    MotorSpeedSet             = 0x82
    PWMFrequenceSet           = 0x84
    DirectionSet              = 0xaa
    MotorSetA                 = 0xa1
    MotorSetB                 = 0xa5
    Nothing                   = 0x01
    EnableStepper             = 0x1a
    UnenableStepper           = 0x1b
    Stepernu                  = 0x1c
    I2CMotorDriverAdd         = 0x0f  #Set the address of the I2CMotorDriver

    def __init__(self,address=0x0f):
        self.I2CMotorDriverAdd=address

        #Maps speed from 0-100 to 0-255
    def map_vals(self,value, leftMin, leftMax, rightMin, rightMax):
        #http://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return int(rightMin + (valueScaled * rightSpan))

            #Set motor speed
    def MotorSpeedSetAB(self,MotorSpeedA,MotorSpeedB):
        if MotorSpeedA != 0 :
            MotorSpeedA = (MotorSpeedA/100 * 40) + 60
        if MotorSpeedB != 0 :
            MotorSpeedB = (MotorSpeedB/100 * 40) + 60
        MotorSpeedA=self.map_vals(MotorSpeedA,0,100,0,255)
        MotorSpeedB=self.map_vals(MotorSpeedB,0,100,0,255)
        bus.write_i2c_block_data(self.I2CMotorDriverAdd, self.MotorSpeedSet, [MotorSpeedA,MotorSpeedB])
        time.sleep(.02)

    #Set motor direction
    def MotorDirectionSet(self,Direction):
        bus.write_i2c_block_data(self.I2CMotorDriverAdd, self.DirectionSet, [Direction,0])
        time.sleep(.02)


    def move(self, MotorSpeedA, MotorSpeedB, Second=None):
        if(MotorSpeedA < 0) and (MotorSpeedB < 0):
            # print "Backward"
            self.MotorDirectionSet(0b1001)
            MotorSpeedA = int(str(MotorSpeedA).strip('-'))
            MotorSpeedB = int(str(MotorSpeedB).strip('-'))
            self.MotorSpeedSetAB(MotorSpeedA, MotorSpeedB)
        elif(MotorSpeedA >= 0) and (MotorSpeedB >=0):
            # print "Forward"
            self.MotorDirectionSet(0b0110)
            self.MotorSpeedSetAB(MotorSpeedA, MotorSpeedB)
        elif(MotorSpeedA >=0) and (MotorSpeedB < 0):
            # print "turn left"
            MotorSpeedB = int(str(MotorSpeedB).strip('-'))
            self.MotorSpeedSetAB(MotorSpeedA, MotorSpeedB)
            self.MotorDirectionSet(0b1010)
        elif(MotorSpeedA <0) and (MotorSpeedB >= 0):
            # print "turn right")
            MotorSpeedA = int(str(MotorSpeedA).strip('-'))
            self.MotorSpeedSetAB(MotorSpeedA, MotorSpeedB)
            self.MotorDirectionSet(0b0101)

        if Second is not None:
            time.sleep(Second)
            self.MotorSpeedSetAB(0, 0)


                    # m= motor_driver()
                    # m.MotorSpeedSetAB(100,100)
                        # m.MotorDirectionSet(0b1010)
                        # time.sleep(2)
                        # m.MotorSpeedSetAB(100,100)
                        # m.MotorDirectionSet(0b0101)
                        # time.sleep(2)
                        # print "backwards"
                        # m.MotorSpeedSetAB(100,100)
                        # m.MotorDirectionSet(0b1001)
                        # time.sleep(2)
                        # print "forward"
                        # m.MotorSpeedSetAB(100,100)
                        # m.MotorDirectionSet(0b0110)
                        # time.sleep(2)
