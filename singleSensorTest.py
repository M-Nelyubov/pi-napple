import time
import board
import adafruit_tcs34725
import busio
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

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

#initializeColorSensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

#Attempt to print sensor object properties:
#for property, value in vars(sensor).items():
#    print(property, ":", value)


# Main loop reading color and printing it every second.
while True:
    # Read the color temperature and lux of the sensor too.
    temp = int(sensor.color_temperature)
    lux = int(sensor.lux)
    colorTuple = sensor.color_rgb_bytes 
    print("Temperature: {0}\tK Lux: {1}\tcolorTuple: {2}".format(temp, lux, colorTuple))
    # Delay for a second and repeat.
    time.sleep(0.25)