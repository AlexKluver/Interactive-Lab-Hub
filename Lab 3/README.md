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

Another way to improve the interaction of our device would be to have a visual display of a person as the device is acting as a personal assistant. Adding a dynamic visual like this could allow the user to easily adapt the problems they are experiencing in the device by being guided by the virtual person. We originally had thought of using some type of servo powered doll to achieve this, but we had decided that the use of a virtual person may be better as it would then not be limited by the movements of the servos

3. Make a new storyboard, diagram and/or script based on these reflections.

Here is an updated story board that implements the use of a digital person instead of a physical one so that the device can be more dynamic based on user input.

![IMG_20211007_103853](https://user-images.githubusercontent.com/89855265/136857611-602cee13-4050-4bc3-8945-f7a2ec02a94b.jpg)

 
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

One part that worked well about the system was that 

### What worked well about the controller and what didn't?


The controller that we used for our device is the same one that is used for the "Wizarding the Device" section in the first part of the lab, but was modified to no longer use the accelerometer as our device did not require motion detection. Being able to change the speech on the fly based on what the user said to the device was very helpful and allowed the person that was controlling the device to do so much more dynamically. One bad thing about how we had the controller set up was that everything was separate from one another, meaning that when we were running the wizarding software, we could not run other prorgams on the pi, so we instead utilized powerpoint to display the animations/images that corresponded to the function the user was using. Doing so, however, also lead to problems, as the person controlling the device was required to do multiple tasks at the same time, which might work better if some than 1 person controlled the device.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

In order to design a more autonomous version of our device, it would require us to have better word recognition for speech to text. With the text that was recorded, we could then pass it through several preprocessing steps such as removing stop word and searching for keywords like "yes" and "no." Utilizing the data we are able to properly process via speech to text methods, we would then be able to control our device based off of what the user said. Having good natrual language processing methods is they most important key in creating any voice activated system, as long as the device is able to process and understand what the user is asking, then they can give a proper response.

Another way to make this device completely autonomous would be to remove the voice controlled aspects and always have all features activated. A simple way to implement this into our device would be to have a camera detect the color of the users clothes, and then give a color that would match well automatically without any user input. Another way to make our device more autonomous would be to have the device set alarms for the user without asking based on previous user input. This would require some machine learning and would also likely not be a useful function as it would scare/surprise people. To automate the function of waving/greeting people would be relatively easy, but could be implemented in varying complexity. For example, it could automatically give a generic greeting based off of motion sensing, or it could integrate facial recognition and greet people by their name if the device is aware of it and ask for their name if it is not.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

For our device, a way to make a useful dataset of interactions would be to track the frequency of use of each function of the device that is used, and then suggest the user to create or use the device at these times, similar to how people set reminders for themselves, but instead they would just be reminded by the device who has kept track of all the previous uses.

Another sensor that would make sense to be included in the device is a camera. The addition of a camera would allow the device to recognize colors, which would be helpful for the part of the device that helps you select what to wear. Having only a vague color description given by the user would not yield very good results for the devices suggestions of what color to accompany the shirt or pants with.
