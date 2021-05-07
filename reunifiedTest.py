print("Initializing motors")

import time
import sys
import RPi.GPIO as GPIO

gpio_channels = [6,13,19,26]       #Channel number will be output pin number

print("setting GPIO mode")
GPIO.setmode(GPIO.BCM)            #Sets mode to board numbering
print("setting up GPIO")
GPIO.setup(gpio_channels, GPIO.OUT, initial=GPIO.LOW) # sets up channels (GPIO pins) as an outputs for the motors


def moveForward(n):
    GPIO.output(gpio_channels[0], GPIO.HIGH)
    GPIO.output(gpio_channels[2], GPIO.HIGH)
    GPIO.output(gpio_channels[1], GPIO.LOW)
    GPIO.output(gpio_channels[3], GPIO.LOW)
    time.sleep(n)
    GPIO.output(gpio_channels[0], GPIO.LOW)
    GPIO.output(gpio_channels[2], GPIO.LOW)

def moveBackward(n):
    GPIO.output(gpio_channels[1], GPIO.HIGH)
    GPIO.output(gpio_channels[3], GPIO.HIGH)
    GPIO.output(gpio_channels[0], GPIO.LOW)
    GPIO.output(gpio_channels[2], GPIO.LOW)
    time.sleep(n)
    GPIO.output(gpio_channels[1], GPIO.LOW)
    GPIO.output(gpio_channels[3], GPIO.LOW)


def fineAdjustRight():
    turnRight(0.05)



def turnRight(n):
    GPIO.output(gpio_channels[2], GPIO.LOW)
    GPIO.output(gpio_channels[3], GPIO.HIGH)
    GPIO.output(gpio_channels[0], GPIO.HIGH)
    GPIO.output(gpio_channels[1], GPIO.LOW)
    time.sleep(n)
    GPIO.output(gpio_channels[0], GPIO.LOW)
    GPIO.output(gpio_channels[1], GPIO.LOW)
    GPIO.output(gpio_channels[2], GPIO.LOW)
    GPIO.output(gpio_channels[3], GPIO.LOW)
    
def fineAdjustLeft():
    turnLeft(0.05)
    
    
def turnLeft(n):
    GPIO.output(gpio_channels[2], GPIO.HIGH)
    GPIO.output(gpio_channels[3], GPIO.LOW)
    GPIO.output(gpio_channels[0], GPIO.LOW)
    GPIO.output(gpio_channels[1], GPIO.HIGH)
    time.sleep(n)
    GPIO.output(gpio_channels[0], GPIO.LOW)
    GPIO.output(gpio_channels[1], GPIO.LOW)
    GPIO.output(gpio_channels[2], GPIO.LOW)
    GPIO.output(gpio_channels[3], GPIO.LOW)
    
    

#print("Moving forward")
#moveForward(0.5)
#print("Moving backward")
#moveBackward(1.5)




import board
import adafruit_tcs34725
import adafruit_tca9548a
import busio

#initializeColorSensor
i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_tcs34725.TCS34725(i2c)
tca = adafruit_tca9548a.TCA9548A(i2c)
sensors = [0,0,0,0]
sensorLux = [False,False,False,False]
sensors[0] = adafruit_tcs34725.TCS34725(tca[0])
sensors[1] = adafruit_tcs34725.TCS34725(tca[1])
sensors[2] = adafruit_tcs34725.TCS34725(tca[2])
sensors[3] = adafruit_tcs34725.TCS34725(tca[3])



# Main loop reading color and printing it every second.
def refreshSensorLux():
    str = ""
    n=0
    for sensor in sensors:
        lux = int(sensor.lux)
        sensorLux[n] = lux > 700
        lux = sensorLux[n]
        str+=("s{0} Lux: {1}\t".format(n,lux))
        n= n+1
    
    print(str)



refreshSensorLux()

#while(sensorLux[0] or sensorLux[1] or sensorLux[2] or sensorLux[3]):
#    refreshSensorLux()
#    if(sensorLux[0] and sensorLux[1]):
#        moveForward(0.075)
#    if(sensorLux[0] and not(sensorLux[1])):
#        fineAdjustLeft()
#    if(sensorLux[1] and not(sensorLux[0])):
#        fineAdjustRight()
#    if(not(sensorLux[0]) and not(sensorLux[1])):
#        turnLeft(0.5)
#turnLeft(1.05)
#time.sleep(5)
#moveBackward(1)
#time.sleep(5)
turnRight(1.05)

print("Completed sensor initialization")



GPIO.cleanup()