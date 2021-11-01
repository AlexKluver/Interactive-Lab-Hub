
### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


### Part A
### Play with different sense-making algorithms.



```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

#### Contours

As seen below, I used the contours program when in the in-class lab session. The program uses the webcam and outlines everything that it can detect in a bright green color. One design that would be a very useful application of the contour detection is image or shape recognition. If you point this camera at a certain image and it can properly correlate the contour outlines with a corresponding output, then it could be used to unlock or verify the identity of someone. A common use of technology similar to this is Apple's FaceID, which pairs face contours with classical image classification.

<img width="325" alt="contour" src="https://user-images.githubusercontent.com/89855265/139725430-c190e56d-f747-4e1b-98bc-6b23b1167231.PNG">

#### Face-Detection
From my experience with the use of the facial recognition in the lab session, I could see that there were a large amount of flaws in the program. One of those being that it was generally not very successful at detecting the overall features of the face. The screenshot that was provided was one of the short periods of time that I was able to get the program to run correctly. One major issue I experienced was that it kept detecting my nostrils as eyes, and would rarely detect my eyes, especially when I was wearing my glasses. One good application of a working face-detecting device would be to simply turn a device on when it is looked at. More commonly, devices are movement or touch sensitive to turn on, but face detection would be a cool way to implement a similar feature.

<img width="325" alt="face detection w glasses" src="https://user-images.githubusercontent.com/89855265/139725439-de13624d-5146-4975-aecb-0f1ebe453c41.PNG">

#### Optical Flow
Optical flow on the pi was very finicky, most of the time when the program was run it would crash before the webcam display would launch, presumably because the program was unable to find any anchor points for the optical flow. This program would be useful to tracking the path and position of objects over time. For example,it could be used to follow the path of a golf ball in flight if it had the optical capablities.

<img width="321" alt="flow detection" src="https://user-images.githubusercontent.com/89855265/139725454-30e30952-3b2f-477c-a50d-9647e6a1fb06.PNG">

#### Detect
The object detection was the program that I found to have much less useful applications for compared to the others. One simple way it could be used however, would be to count the number of people in a venue. If the object detection was better, then it could assign each person as an object and then count the number of assigned objects and that would correspond to the amount of people present. This would require a birds-eye view of the venue so that it would be able to see all people at the same time, lowering the risk of double counting. Below shows detection of my hand, and the next photo shows detection of the keypad.

<img width="325" alt="object detection hand" src="https://user-images.githubusercontent.com/89855265/139725579-6aab1982-b207-4ba8-90df-03c4ab23fc91.PNG">
<img width="327" alt="number pad detection" src="https://user-images.githubusercontent.com/89855265/139731327-913d9604-a9ca-4cfc-ae7e-d764905441fd.PNG">

#### MediaPipe


**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)

While I found this program to be very interesting, using it on the raspberry pi was not pleasant in my experience, as it significantly slowed down the entire pi and caused other running programs to crash, which is likely due to the higher complexity of computations being done in the program. 

Similar programs are used in bodytracking in motion pictures. The important areas of motion on ones body will be mapped with a dot like seen at the joints of my hand in the photo below. This data will then be filmed to collect data on natural movements and then is often used as the movements of cgi characters in film or sometimes even used as a guide for movement in 2D animation. Another more novel application of this could be to again track the movements of peoples bodies, but in a medical setting where a doctor can overlook the range of motion their patient has in certain parts of their body. A place where this could be significantly useful would be in physical therapy to gauge progress.
<img width="326" alt="handpose" src="https://user-images.githubusercontent.com/89855265/139731660-624f0e22-de43-4f71-b4ad-727599c2b1fa.PNG">



#### Teachable Machines

```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

I am unsure of the intended classifications of the provided teachable machine, but the only two outputs I was able to get in several sessions of using it was "mask" and "background." A useful application for a teachable machine would be for it to be able to detect fraudulant ID cards. Using the data that is available about ID's a teachable machine could be made to check for obvious flaws in fake drivers licenses and categorize them as either fake or real. A teachable machine like this seems to use a larger amount of machine learning to be able to actively take in an image and correctly classify it. This greater amount of image processing allows for objects to be more complexly classified rather than relying on individual shapes present in the image, which was a large downfall of most of the openCV options.
<img width="405" alt="teachables" src="https://user-images.githubusercontent.com/89855265/139727307-9268ac32-b134-41c7-8fd5-f34410fd32b6.PNG">



### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

For this interaction, I have decided that I wanted to use the teachable model to detect if I was wearing my glasses or not because I often forget to wear my glasses and don't realize it until I have gotten to class and cannot see what is on the board or projector. For something like this to be useful, it would have to be set up at the exit of my apartment and make a noise if I am trying to leave without having my glasses on. To implement this, I used the google teachable model interface that was suggested earlier in the lab. For the device to be useful to me, however, it must be able to detect that I am wearing any one of my three pairs of glasses, meaning it assigns a binary output to a continuous input. A video of live feed interaction with the device can be seen below in part D.

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
  
After programming the teachable machine with many about 100 different images of me wearing and not wearing glasses into the respective classes and testing out the device, I noticed that this was not nearly enough images for it to correctly classify as I had only kept myself centered in the photos for each of the classes, which lead to many misiclassifications when i was uncentered in the frame. To fix this I added an additional 1000 photos at various angles and locations to add variation to the model. After adding these additional images and retraining the model, the output was much more accurate at detecting if I was wearing my glassses.

2. When does it fail?

When testing the device further, I noticed that my webcam would attempt to dynamically change the lighting so that it could better bring images into focus, howver, this lead to there being an instance where the model could not tell if I had my glasses on or not, which caused the output to be erratic and inconsistent. This tells me that for this device to work, there must be consistant lighting so that the camera does not attempt to adjust itself or I have to disable this feature in the camera. 

Also another part where the machine was having difficulties classifying was when I wore my glasses that had thin wire frames. This is most likely due to the fact that the camera is not high enough resolution and did not have enough contrast present to tell if I was wearing glasses. In a way, a false negative classification of not wearing glasses would be most appropriate in the scenario as the purpose of thin framed glasses to for people to not notice them as much. I believe that a similar situation would happen if one was to test the device with clear framed glasses.

3. When it fails, why does it fail?

As discussed in the section above, the device ususally fails when it is unable to gather enough information to correctly classify the datapoint. root causes for this in my experiences were usually due to the small amount of classification training data and lack of consistancy when testing the teachable machine. The largest factor in this, however, seemed to be the positioning of my head in the frame. If I was positioned in a place where I have no data from either class, then the classification would erratically change because the output was undetermined. The only way that it would be possible to fix this would be to train the device with enough variation in the rest of the environment that it could focus specifically on the fact that I was or wasn't wearing glasses. Lighting also played a large factor because of the visibility of objects in the frame, but if this device were to be used in the real world, a high variation of lighting will need to be used in the training data, or other methods such as infrared cameras could be used so that lighting is not important. 

4. Based on the behavior you have seen, what other scenarios could cause problems?

Other situations that I could see this device having problems clsasifying correcly would be if the user was wearing any type of headwear so that thte device was not able to see the users face directly, and therefore could not determine if their glasses were on.Ultimately, the only thing that leads to failure in a teachable machine like this is obstruction of view or lack of training data. If we assume that the users face is visible in the frame , the camera has a high enough resolution to detect the glasses, and we have a near infinite amount of training data, then the device's classification would be near perfect.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?

If someone was using a image classification system like the one I have implemented to detect if the user is wearing glasses, I would be under the assumption that the user is aware of the behavior of the system and that the user must be clearly visible to the camera so that it can make a proper detection. The other uncertainties in the system, such as the dynamic lighting adjustments of the camera or the possible depth uncertainty would not be immediately apparent to the user, and could definitely cause problems.

2. How bad would they be impacted by a miss classification?

Being experienced in often forgetting to put on my glasses before I leave my apartment, I can say that the impact is heavily based on the things that they will be doing throughout the day as well as the type of activities they are doing. For example, the times that it would affect me the most is if I forget my glasses when I am leaving to attend lecture, then I am unable to see what the professor is displaying and cannot learn as much. However, if I am not going anywhere that I need to be able to read anything at long distances, I will be minimally affected. This impact would be case-by-case and vary rgeatly for each user.

3. How could change your interactive system to address this?

Some simple ways that the system could deal with these misclassifications is going to be put into a list format below:
-Camera changing lighting: fix the camera so that it does not dynamically change with the environment or autofocus on any objects
-lack of datapoints for training: add active classification datapoints with a ligh likelihood to the training data pool so that a higher variation of data can be used to train the model. This is similar to how must unsupervised machine learning method work.
-Users face is obstructed by an object: have several cameras at different angles or have a wide angle lens to that the users face is always in view.

5. Are there optimizations you can try to do on your sense-making algorithm.

Without access to the actual algorithm behind the teachable model, no algorithmic optimizations can be done. The only things that I would be able to change so that the model has a higher likelihood of the correct classification is to ensure the physical environment is in a constant state and to train the model with a very arge amount of training datapoints to ensure the model fits correctly with a variety of different inputs.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?

The purpose of the device is to detect if the user is wearing their glasses when they are leaving their home. The device uses basic image processing and an unknown classification model to determine a binary output, which is true if the user is wearing glasses and false if not. The device will then beep to tell the user to go back and put their glasses on.

* What is a good environment for X?

An ideal environment for a device like this would be near the exit to ones house or apartment as well as has sufficient lighting and a clear view of the user as they exit. With these three aspects in the environment, the model can reliably classify in most instances.

* What is a bad environment for X?

A bad environment for the device would be in a unlit room, where it cannot properly see the users face to determine the classification point or if the device is obstructed by another object or is in a place that it cannot easily seee the users face.

* When will X break?

Theoretically, a device like this would not break if implemented correctly. The only time there would be a misclassification is if the user is not clearly visible in the frame of the camera or the lighting is poor. However, such a device shouold only output true is it has a very high certainty, so a high likelihood threshold would have to be set. The device would not work as well at night because the natural lighting is likely not going to be as beneficial to the device as during the day.

* When it breaks how will X break?

As discussed in most of the prior paragraphs the device will only break if their is insufficient lighting or an obstruction of view of the camera where it cannot properly see the user of the device.

* What are other properties/behaviors of X?

Another behavior of the device could be to have a red or green light present on the exit of the room to signify if the user is wearing their glasses, this way they do not have the possibility of accidentily missing the beep.

* How does X feel?
Good I guess? The user would not forget to wear their glasses as often and would live a better life.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***


https://user-images.githubusercontent.com/89855265/139757209-3fd57583-6867-4bec-98e1-833a87286542.mp4




### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
