## Part 1.
### Text to Speech 

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

This file has been saved to lab3 repo under the name flite_demo.sh

### Speech to Text

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

This part of the lab has been saved to vosk_demo_mic.sh in the Lab 3 repo. I asked the user to state how many fingers they had.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

![IMG_20211003_113012](https://user-images.githubusercontent.com/89855265/135761054-ca55654e-b0f5-4f6f-8c1f-0352c7580482.jpg)

\*\***Please describe and document your process.**\*\*

When creating the storyboard, we were trying to think of a few things that a personal assistant would be capable of doing while considering our techinical limitations of what we have available to use for creating the prototype device. Since the device is dependent on voice interaction, we decided that our best and easiet option would be for use to have the personal assistant greet people and wave when spoken to. While we were in the process of creating the story board, we added additional voice activated and supported ideas to our personal assistant such as having the assistant tell the user if their outfit matches and have the assistant wake up the user is the morning.

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

https://user-images.githubusercontent.com/89855265/135762391-7dd904cc-0e60-4713-ab91-c35b89ade3d8.mp4

The dialog was slightly different than what we had thought it was going to be. I think this was because it is hard to predict human interactions and language. In our script, we had a more outlined interaction of asking questions and having the device user answer them, but when we acted it out, it ended up being that the device user answered several of the future questions without being asked. For example, our script had a back and forth about asking if the user wanted an alarm, them asking what time to set the alarm for, but instead the user said that he wanted an alarm and immediately said for what time without being asked. When programming such a sophisticated interactove device, it is important to consider the variations in natural language and conversation.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
One thing that was a major factor in the usability of our initial device design was the wording of how the device interacted with the user. While our device was scripted to ask simple questions and receive one word answers such as "Yes", "No", or a time of day, we found that the user who was not aware of the script assumed that the device would be able to understand longer phrases and be able to keep track of answers to questions that it had not yet asked. One major example of this was when the device asked the user if he would like to set an alarm, and the user responded yes and said a time that he wanted the alarm for without being asked for it. If this had been a real device, it may not have been able to understand that the user already gave it a time and asked "what time would you like to set the alarm for?" even though the user had already stated that.

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
An easy interaction that would help the user to interact with the device would possibly be the addition of visuals such as a red or green light if the device did or did not understand the request of the user. (i.e. the speech was recognized incorrectly.) This way the user would be able to tell what has gone wrong with the interaction or understand that the device was not able to understand their speech. Another way to implement the same feature could be to have two different tones to play if the device was or wasn't able to understand what the user was saying.

Another way to improve the interaction of our device would be to have a visual display of a person as the device is acting as a personal assistant. Adding a dynamic visual like this could allow the user to easily adapt the problems they are experiencing in the device by being guided by the virtual person.

3. Make a new storyboard, diagram and/or script based on these reflections.
 
## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*


### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

