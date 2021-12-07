import time
import board
import busio
import pyaudio
import numpy as np
import adafruit_mpr121
import qwiic_joystick
import adafruit_ssd1306
import time
from adafruit_servokit import ServoKit
from adafruit_apds9960.apds9960 import APDS9960

kit = ServoKit(channels=16)
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128,32,i2c)

oled.fill(0)
apds = APDS9960(i2c)


apds.enable_proximity = True

servo1 = kit.servo[0]
#servo2 = kit.servo[1]
servo3 = kit.servo[2]
#servo4 = kit.servo[3]


servo1.set_pulse_width_range(500, 2500)
#servo2.set_pulse_width_range(500, 2500)
servo3.set_pulse_width_range(500, 2500)
#servo4.set_pulse_width_range(500, 2500)

mpr121 = adafruit_mpr121.MPR121(i2c)
#oled = adafruit_ssd1306.SSD1306_I2C(128,32,i2c)
score = 0
while True:
    oled.fill(0)
    oled.text(str(score),60,15,1)
    oled.show()
    if mpr121[0].value:
        #servo1
        #print("servo1")
        servo1.angle = 90
    else:
        servo1.angle = 180
    #if mpr121[1].value:
        #servo2
        #print("servo2")
       #servo2.angle = 180
    #else:
        #servo2.angle = 0
    if mpr121[2].value:
        #servo3
        #print("servo3")
        servo3.angle = 86
    else:
        servo3.angle = 3
    #if mpr121[3].value:
        #servo4
        #print("servo4")
   #     servo4.angle = 180
    #else:
    #    servo4.angle = 0
    if(apds.proximity > 5):
        score += 1
        print(score)
        time.sleep(2)
