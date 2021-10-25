import time
import board
import busio
import pyaudio
import numpy as np
import adafruit_mpr121
import qwiic_joystick
import adafruit_ssd1306

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
my_joystick = qwiic_joystick.QwiicJoystick()
my_joystick.begin()

oled = adafruit_ssd1306.SSD1306_I2C(128,32,i2c)
while True:
    oled.fill(0)
    if my_joystick.horizontal > 550:
        x=1.1
    elif my_joystick.horizontal < 450:
        x=0.9
    else:
        x=1
    if mpr121[0].value:
        #play corresponding tone
        oled.text("A",60,15,1)
        oled.show()
        f=261*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[1].value:
        #play corresponding tone
        oled.text("B",60,15,1)
        oled.show()
        f=293*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[2].value:
        #play corresponding tone
        oled.text("C",60,15,1)
        oled.show()
        f=330*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[3].value:
        #play corresponding tone
        oled.text("D",60,15,1)
        oled.show()
        f=349*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[4].value:
        #play corresponding tone
        oled.text("E",60,15,1)
        oled.show()
        f=392*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[5].value:
        #play corresponding tone
        oled.text("F",60,15,1)
        oled.show()
        f=440*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[6].value:
        #play corresponding tone
        oled.text("G",60,15,1)
        oled.show()
        f= 493*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[7].value:
        #play corresponding tone
        oled.text("A",60,15,1)
        oled.show()
        f=523*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[10].value:
        #play corresponding tone
        f=587*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    if mpr121[11].value:
        #play corresponding tone
        f=659*x
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        stream.write(volume*samples)
    
    #stream.write(volume*samples)
    
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
stream.stop_stream()
stream.close()

p.terminate()
