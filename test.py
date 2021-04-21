import sys
import time
import RPi.GPIO as GPIO

#motor & sensor I/O channels
channel = 26 #todo, int         Channel number will be output pin number
channels = [26, 25]							   #Any other channels that we may need
pwmpin = 28

#configuration from:
#	https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
#	https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
GPIO.setmode(GPIO.BOARD)     #Sets mode to board numbering
p = GPIO.PWM(pwmpin, frequency)	#Create an instance of PWM


GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)				# sets up channel (pin) as an output



#test turning on a motor
dutyCycle = 10.0
p.start(dutyCycle)
time.sleep(0.5)
p.stop()
##Once basic on/off behavior is established, test varying duty cycle behavior min to max
#        for dc in range(0, 101, 5):
#            p.ChangeDutyCycle(dc)
#            time.sleep(0.1)
#				 for dc in range(100, -1, -5):
#            p.ChangeDutyCycle(dc)
#            time.sleep(0.1)


state = GPIO.HIGH						#Truthy -> GPIO.HIGH, Falsy -> GPIO.LOW
GPIO.output(channel, state)
time.sleep(0.5)
GPIO.output(channel, GPIO.LOW) 










GPIO.cleanup()