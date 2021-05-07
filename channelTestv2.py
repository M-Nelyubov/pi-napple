import sys
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

gpio_channels = [24,26,35,37]       #Channel number will be output pin number


GPIO.setmode(GPIO.BCM)            #Sets mode to board numbering

GPIO.setup(gpio_channels, GPIO.OUT, initial=GPIO.LOW) # sets up channels (GPIO pins) as an outputs for the motors


#test providing power to each pin one at a time
print("Beginning test of all configured GPIO pins")
for pin in gpio_channels:        #Iterate through the list of pins one pin at a time
    print("high "+ str(pin))     #print currently activated pin for testing
    GPIO.output(pin, GPIO.HIGH)  #turn pin high
    time.sleep(1)                #timeout for 3 seconds to provide time for observation
    print("low " + str(pin))     #print currently activated pin for testing
    GPIO.output(pin, GPIO.LOW)   #turn pin low
    time.sleep(1)                #pause for a quarter second before proceeding to the next pin
print("End of testing all configured GPIO pins")


#print("high 24 and 35")
#GPIO.output(24, GPIO.HIGH)
#GPIO.output(35, GPIO.HIGH)
#time.sleep(5)
#print("high 26 and 37")
#GPIO.output(26, GPIO.HIGH)
#GPIO.output(37, GPIO.HIGH)
#time.sleep(5)
#print("low 24 and 35")
#GPIO.output(24, GPIO.LOW) 
#GPIO.output(35, GPIO.LOW) 
#time.sleep(5)
#print("low 26 and 37")
#GPIO.output(26, GPIO.LOW)
#GPIO.output(37, GPIO.LOW)




def moveForward(n):
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(35, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    time.sleep(n)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)

def moveBackward(n):
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(37, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)
    time.sleep(n)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

def rotateRight(n):
    moveBackward(0.25)

#testchange

GPIO.cleanup()