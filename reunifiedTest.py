import time
import board
import adafruit_tcs34725
import adafruit_tca9548a
import busio
import digitalio


#initializeColorSensor
i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_tcs34725.TCS34725(i2c)
tca = adafruit_tca9548a.TCA9548A(i2c)
sensors = [0,0,0,0]
sensorLux = [-1,-1,-1,-1]
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
        str+=("s{0} Lux: {1}\t".format(n,lux))
        n= n+1
    
    print(str)
    
    
    
    
refreshSensorLux()

print("Completed sensor initialization")


print("Initializing motors")


import sys
import RPi.GPIO as GPIO

gpio_channels = [24,26,35,37]       #Channel number will be output pin number


#GPIO.setmode(GPIO.BOARD)            #Sets mode to board numbering
print("setting up GPIO")
GPIO.setup(gpio_channels, GPIO.OUT, initial=GPIO.LOW) # sets up channels (GPIO pins) as an outputs for the motors


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


def turnRight(n):
    GPIO.output(35, GPIO.LOW)
    GPIO.output(37, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)
    time.sleep(n)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    
def turnLeft(n):
    GPIO.output(35, GPIO.HIGH)
    GPIO.output(37, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(n)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    
    

print("Moving forward")
moveForward(0.5)
print("Moving backward")
moveBackward(0.5)