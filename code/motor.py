#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
class motor:


    def newPins(self):
        GPIO.setmode(GPIO.BCM)
        print("test")

        # Define GPIO signals to use
        # GPIO18,GPIO23,GPIO24,GPIO25
        self.StepPins = [18,23,24,25]

        # Set all pins as output
        for pin in self.StepPins:
          print ("Setup pins")
          GPIO.setup(pin,GPIO.OUT)
          GPIO.output(pin, False)

    def newSeq(self):
        # Define advanced sequence
        # as shown in manufacturers datasheet
        Seq = [[1,0,0,1],
               [1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1]]
        self.Seq = Seq

    def newStepCount(self):
        self.StepCount = 8

    def getWaitTime(self) :
        # Read wait time from command line
        if len(sys.argv)>1:
          WaitTime = int(sys.argv[1])/float(1000)
        else:
          WaitTime = 1/float(850)

        return WaitTime

    def newStepCounter(self) :
        # Initialise variables
        self.StepCounter = 0

    def move(self, speed, duration):
        # Start main loops
        self.newPins()
        self.newSeq()
        self.newStepCount()
        self.newStepCounter()

        durTime = 0
        while durTime <= duration/100:
          #print (self.StepCounter)
          #print (self.Seq[self.StepCounter])

          for self.pin in range(0, 4):
            self.xpin = self.StepPins[self.pin]

            if self.Seq[self.StepCounter][self.pin]!=0:
              #print (" Enable GPIO %i" %(self.xpin))
              GPIO.output(self.xpin, True)
            else:
              GPIO.output(self.xpin, False)

          self.StepCounter += speed
          #time +=self.getWaitTime()
          # If we reach the end of the sequence
          # start again
          if (self.StepCounter >= self.StepCount):
            self.StepCounter = 0
          if (self.StepCounter<0):
            self.StepCounter = self.StepCount+speed

          if(self.StepCounter >= duration):
              break;
          durTime = durTime + self.getWaitTime()
          #print (durTime)
          # Wait before moving on
          time.sleep(self.getWaitTime())
