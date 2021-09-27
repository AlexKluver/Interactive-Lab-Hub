import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import webcolors
from adafruit_rgb_display.rgb import color565

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
#setting up buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonA.switch_to_input()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

y=top
draw.text((x,y),"Find the right combonation\n to see current the time\n Press buttons to start",font = font, fill = "#FFFFFF")
disp.image(image,rotation)
i=0
h=0
while True:
    # Draw a black filled box to clear the image.
    #draw.rectangle((0, 0, width, height), outline=0, fill=0)
 
    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    
    #unlocking sequence, A, then B, then A, then both
    #check for button push on A
    if buttonB.value and not buttonA.value:
        if i == 0 or i == 2:
            if i == 0:
                #clear screen on first push
                disp.fill(color565(0,0,0))
                draw.rectangle((0,0,width,height),outline = 0, fill = 0)
            #display green squares to show that correct button has been pushed
            draw.text((45,h),"A",font = font2, fill = "#FFFFFF")
            disp.image(image,rotation)
            disp.fill_rectangle(0,100,h + 35,50,color565(0,255,0))
            i += 1
            h += 35
        else:
            #display red rectangle to show wrong button push
            disp.fill_rectangle(h,45,35,50,color565(255,0,0))
    if buttonA.value and not buttonB.value:
        if i == 0:
            #clear screen on first push
            disp.fill(color565(0,0,0))
        if i == 1:
            #display rectangle and corresponding button push
            draw.text((45,h),"B",font = font2, fill = "#FFFFFF")
            disp.image(image,rotation)
            disp.fill_rectangle(0,100,70,50,color565(0,255,0))
            i += 1
            h += 35
        else:
            #display a red square to signify wrong button push
            disp.fill_rectangle(h,45,35,50,color565(255,0,0))
    if not buttonA.value and not buttonB.value and i == 3:
        #display final button sequence and message to see time
        draw.text((0,h),"A + B", font = font2, fill = "#FFFFFF")
        draw.text((160,0), "Push A\n to see\n time", font = font, fill = "#FFFFFF")
        disp.image(image,rotation)
        disp.fill_rectangle(0,100,135,50,color565(0,255,0))
        time.sleep(1)
        #wait for button push
        while buttonA.value:
            time.sleep(0.1)   
        #clear screen then display time using bars
        disp.fill(color565(0,0,0))
        while True:
            #infinite while loop to display clock
            draw.rectangle((0,0,width,height),outline=0,fill=0)
            time_hr = int(strftime("%H"))
            time_min = int(strftime("%M"))
            time_sec = int(strftime("%S"))
            y = 45
            draw.text((time_hr*9 + 1,0), str(time_hr), font=font2, fill="#FFFFFF")
            draw.text((time_min* 3,50),str(time_min),font = font2, fill = "#FFFFFF")
            draw.text((time_sec * 3,100),str(time_sec), font = font2, fill = "#FFFFFF")
            disp.image(image,rotation)
            disp.fill_rectangle(0,240 - time_hr * 9,35,240,color565(255,0,255))
            disp.fill_rectangle(50,240 - time_min * 3,35,240,color565(0,255,255))
            disp.fill_rectangle(100,240-time_sec * 3,35,240, color565(255,255,0))
            time.sleep(0.9)
            if time_sec == 0:
                 disp.fill(color565(0,0,0))
            #reset back to beginning using button push
            if not buttonA.value or not buttonB.value:
                i = 0
                h = 0
                break
    # Display image.
    time.sleep(0.1)
