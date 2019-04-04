import time
import grovepi

class buzzer:

    def port(self):
        return self.port

    def on(self):
        grovepi.analogWrite(self.port,250)

    def off(self):
        grovepi.analogWrite(self.port,0)

    def beep(self, duration):
        self.on()
        time.sleep(duration)
        self.off()
        time.sleep(duration)

    def playTone(self,volume, duration):
        print("Play Tone " + str(volume) )
        grovepi.analogWrite(self.port,volume)
        time.sleep(duration)
        grovepi.analogWrite(self.port,0)

    def playTone(self,volume):
        print("Play Tone " + str(volume) )
        grovepi.analogWrite(self.port,volume)
