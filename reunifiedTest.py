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