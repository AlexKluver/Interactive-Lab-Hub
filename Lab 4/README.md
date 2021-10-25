# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the 3 example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python light_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***
![image](https://user-images.githubusercontent.com/89855265/137779392-fc9818ec-7f96-4987-b273-06e3f68195c9.png)


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

One of the major questions when sketching out various prototypes that incorporate the sensors was "are the sensors capable of measuring with enough accuracy such that the device will actually be useful?" In order to fully understand the capabilities of the sensors, each one would have to be incorporated into a physical prototype to measure their sensitivity.

Another question that came up when sketching the prototypes was "is my device designed to work in a active or passive manner?" Which is essentially asking if my device requires the user to be aware of how to interact with the device to be able to use it or does the device work without explicit user input. This question does not require physical prototyping to understand, but instead it requires deeper thought into how you intend the end device to work. 

The most important question that I had asked myself when drawing these designs was "how big should my device be?" This is something that can easily be answered by creating a full size physical protoype of the device. This prototype does not require any of the sensors to be implemented yet, but instead just needs to be carried out to determine if the chosen size of the device makes sense.

**\*\*\*Pick one of these designs to prototype.\*\*\***

The design that I have chosen to move forward with for the remainder of the lab is the Twizzler piano as seen in number 2 of the design sketches.

### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***
![image](https://user-images.githubusercontent.com/89855265/137779458-987441dd-a2d8-4567-a6df-60b92ffa3141.png)
![image](https://user-images.githubusercontent.com/89855265/137779518-e9a2d0b6-7da7-4328-9516-ffd0a6c9c84a.png)


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

As the device I have chosen to create does not use the distance or proximity sensor, the size and overall shape of the device is arbitrary as long as each sensor can still be connected to the pi, however, one major question that arrose when creating the prototype designs for this lab was "where should I place the sensors on my device so that the user can interact with each of them without interference from another sensor. By drawing 3 dimensional renderings of the prototypes, these places can be intuitively chosen based on how you expect the user to interact with the device. In order to fully answer this question, I would need to physically prototype the interface of the design and test it out to see if my assumptions of sensor placement were true.

Another question that I had thought of when sketching the prototypes was "should my design incorporate similarities to common design templates that already exist?" Another way to think of this question in relation to my chosen device design is "should I design it to look like a piano or change the look to something new?" I decided that it would be better to incorporate established designs into my prototype so that a new user of the device can intuitively understand how to use the device without explanation. Again, to better understand this question, I would need to prototype the physical interface of the device and have other use the device to see if they understand what it is without the need for an explanation.




**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***
The display design that I have chosen to integrate into my prototype is design 4 as shown above, which includes a joystick/rotary encoder (tbd on which one will be used), the OLED display for showing the notes of the piano, the capacitive sensor for detecting key touches, and the alligator clips to connect the capacitive sensor to the keys.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)
 The reasoning behind choosing this design is because it is a classical piano style design where the "keys" are positioned vertically across the face of the device. This design provides initial intuition on how to interact with the device as it is something that people will have seen before and know how to use. In addition to this design, I plan on adding the rotary encoder to either control the volume or the pitch of the piano.
 
 The size of the design was chosen to be large because I wanted to give the user of the device sufficient spacing between the keys of the piano so that they do not accidentily touch a key they had not intended to. The position of the OLED display was chosen to be centered at the bottom of the box because this is where it would be the most visible while not being in the way of the rest of the parts in the design. The speaker was placed next to the OLED for symmetry purposes, and a cutout will be made so that the sound can be properly heard. The joystick was placed in the bottom left-hand corner of the face of the device so that it can be controlled with the left hand of the user while they interact with the keys. I chose the left side for this because most people are right handed and will use their right hand to control the active parts of the device (i.e. the keys) and their left hand to adjust the pitch.
 
Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

Outside of prototype design:
![image0 (2)](https://user-images.githubusercontent.com/89855265/137804193-a1e67d27-2cbf-4d2e-b927-f654b6887caa.jpeg)
Conductive tape was used instead of twizzlers because I did not have any twizzlers. Otherwise the prototype is exactly as seen in the sketch

Inside of the prototype:
![image1 (1)](https://user-images.githubusercontent.com/89855265/137804207-9b20fad1-12b9-4abd-810f-ae91ac605466.jpeg)

LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which we will be distributing the battery packs in the class. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/245605956_303690921194525_3309212261588023460_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=FvFLlClTKuUAX9nJ3LR&_nc_ht=scontent-lga3-1.xx&oh=b7ec1abc8d458b6c1b7a00a6f11398ac&oe=618D7D96" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:

* "Looks like": shows how the device should look, feel, sit, weigh, etc.
Here is the final sketch of the exterior of the device. The goal is to get the device to look as close to this as possible given the equipment that is available. As seen in the sketch, I plan to include the capacitive sensor to detect the key-press, the speaker/webcam to play to tone, and the joystick to alter the pitch of the note. In addition to these sensors, a OLED display will be included at the bottom of the face of the device to display the note that is being played. The end goal is for this device to function similarly to a electric piano with a pitch changer.
  ![image](https://user-images.githubusercontent.com/89855265/138771854-c79ed421-43eb-4439-b6eb-b0cb741224b5.png)

Below, I have provided several pictures of iterations made to the device throughout the creation process. most notably the inclusion of labels for the device sensors. Without labels, the device was slightly confusing to use since the user was not aware of what each sensor was being used for.

Inside of first iteration:
![image2 (1)](https://user-images.githubusercontent.com/89855265/138772637-e86f5525-453e-4d56-b250-cf6d302299a2.jpeg)

Outside of first iteration:
![image3 (1)](https://user-images.githubusercontent.com/89855265/138772715-49549ae1-24df-40e9-beb2-d98e05370941.jpeg)

Outside of Final Iteration:
![image4 (1)](https://user-images.githubusercontent.com/89855265/138772792-f98d11a1-708b-4ef7-9f49-2b0ba0587e14.jpeg)

Side angle of final iteration:
![image0 (3)](https://user-images.githubusercontent.com/89855265/138772837-458de317-4b68-4294-b269-14c5a26957b1.jpeg)


* "Works like": shows what the device can do
Below I have made a few videos displaying how each sensor works in the device as well as a complete overview of the device. The device worked great and eexactly as I had intended it to. The only thing that I think could have been better is if I had a box that was better suited for this device, but I did not have one available.

Here is a video showing how the notes of each of the keys are displayed on the OLED display.

https://user-images.githubusercontent.com/89855265/138773320-1b6d5a94-5c54-4882-b0c4-d126f9f05811.mov

Here is a video walkthrough of how the device works overall:



https://user-images.githubusercontent.com/89855265/138775329-57c64bb4-c9c7-443d-a981-bcfaa76526ef.mov



* "Acts like": shows how a person would interact with the device
Shown below are two different videos showing how someone would interact with the device. The code used to control the piano can be found in piano.py

Here is an interaction with the device of a user playing a song without using the joystick:
https://user-images.githubusercontent.com/89855265/138774402-ed6e0b5c-f2f8-4cf4-951d-bf0b454cb5e1.mov

Here is another interaction with the device where the user plays the same song as before, but using the joystick instead to produce similar notes:

https://user-images.githubusercontent.com/89855265/138774573-f15ade0c-14ba-406f-a02c-dedc30d15cb7.mov


The overall interactions with the device went well. Since the device was made to look and work like a classical electric piano, it was relatively simple to interact with since most people have at one point in their lifetime attempted to play a piano. The addition of the labels on the device was definitely necessary, however, since not all users were aware of what the additional sensors (the ones other than the capacitive touch which was for the keypress) were doing. After these labels were added, all user interactions went flawlessly.
