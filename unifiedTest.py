import time
import board
import adafruit_tcs34725
import adafruit_tca9548a
import busio
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
import sys
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

gpio_channels = [24,26,35,37]       #Channel number will be output pin number


GPIO.setmode(GPIO.BOARD)            #Sets mode to board numbering

GPIO.setup(gpio_channels, GPIO.OUT, initial=GPIO.LOW) # sets up channels (GPIO pins) as an outputs for the motors


#intializeLCD
lcd_columns = 16
lcd_rows =2

lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D21)
lcd_d6 = digitalio.DigitalInOut(board.D5)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d4 = digitalio.DigitalInOut(board.D13)

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,lcd_d7, lcd_columns, lcd_rows)

#initialize i2c 
i2c = busio.I2C(board.SCL, board.SDA)
#initialize multiplexor
tca = adafruit_tca9548a.TCA9548A(i2c)
#create sensor array
sensors = [0,0,0,0]
sensorsLux = [-1,-1,-1,-1]
sensors[0] = adafruit_tcs34725.TCS34725(tca[0])
sensors[1] = adafruit_tcs34725.TCS34725(tca[1])
sensors[2] = adafruit_tcs34725.TCS34725(tca[2])
sensors[3] = adafruit_tcs34725.TCS34725(tca[3])








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
