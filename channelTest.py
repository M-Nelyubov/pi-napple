import sys
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

channel = 24 #todo, int         Channel number will be output pin number


GPIO.setmode(GPIO.BOARD)     #Sets mode to board numbering

GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)				# sets up channel (pin) as an output

GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)				# sets up channel (pin) as an output


GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)				# sets up channel (pin) as an output

GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)				# sets up channel (pin) as an output


print("high 24 and 35")
GPIO.output(24, GPIO.HIGH)
GPIO.output(35, GPIO.HIGH)
time.sleep(5)
print("high 26 and 37")
GPIO.output(26, GPIO.HIGH)
GPIO.output(37, GPIO.HIGH)
time.sleep(5)
print("low 24 and 35")
GPIO.output(24, GPIO.LOW) 
GPIO.output(35, GPIO.LOW) 
time.sleep(5)
print("low 26 and 37")
GPIO.output(26, GPIO.LOW) 
GPIO.output(37, GPIO.LOW) 


GPIO.cleanup()



