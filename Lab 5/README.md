
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


<img width="405" alt="teachables" src="https://user-images.githubusercontent.com/89855265/139727307-9268ac32-b134-41c7-8fd5-f34410fd32b6.PNG">



### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
