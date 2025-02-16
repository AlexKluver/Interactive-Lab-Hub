# Interactive Prototyping: The Clock of Pi

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

[Lab prep](prep.md) is extra long this week! Make sure you read it over in time to prepare for lab on Thursday.

### Get your kit
If you are remote but in the US, let the teaching team know you need the parts mailed.

If you are in New York, you can come to the campus and pick up your parts. If you have not picked up your parts by Thursday lab you should come to Tata 351.

### Set up your Lab 2

1. [Pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub. (This may have to be done again at the start of lab on Thursday.)
  
  If you are organizing your Lab Hub through folder in local machine, go to terminal, cd into your Interactive-Lab-Hub folder and run:

  ```
  Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
  Interactive-Lab-Hub $ git pull upstream Fall2021
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m'merge'
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.

2. Go to the [lab prep page](prep.md) to inventory your parts and set up your Pi before the lab session on Thursday.


## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi

### Setup Personal Access Tokens on GitHub

## Part B. 
### Try out the Command Line Clock


## Part C. 
### Set up your RGB Display


## Part D. 
### Set up the Display Clock Demo


## Part E.
### Modify the barebones clock to make it your own

**We strongly discourage and will reject the results of literal digital or analog clock display.**

I have chose to design a clock that requires the user to "Log in" to view the time similar to logging in to a mobile device. This gamifies the use of a clock on a pi display and makes the interaction more interesting. When the clock is unlocked, the way the time is displayed consists of three horizontal bars across the screen representing the hour, second, and minute hands respectively.

\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

The code can be found in screen_clock.py and the original clock for the earlier part can be found in changed_clock.py.


## Part F. 
## Make a short video of your modified barebones PiClock

\*\*\***Take a video of your PiClock.**\*\*\*


https://user-images.githubusercontent.com/89855265/134063930-9219bed1-793f-40d2-b735-a4d28bfb39d8.mov

This video displays the unlocking and visual interface of the clock. 

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.
To improve upon the clock design that I have made in the first part of the lab, I would like to make a more intuitive way to represent that the current button selection was incorrect other than just displaying a red bar across the screen in place of the green bar. I think this could be done by giving the user a message that the selected button was incorrect or possibly having the signifier be circles that get connected as the user gets closer to the right pattern of button presses.

For the actual clock part, I would like to change it so that the bars go across the screen from left to right instead of the opposite, and also display the actual number of the hour/minute/second values somewhere next to the time bars.

![image](https://user-images.githubusercontent.com/89855265/134969407-ebee9f37-9b44-4ced-9094-1e4107b894fa.png)


# Prep for Part 2

1. Pick up remaining parts for kit.

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As stated in the last lab writeup, I wanted to improve upon my first iteration by adding the digits of time to the bars as well as flipping the bars to go from left to right instead of right to left. I was able to implement both of these in my second iteration of the lab by doing some simple algebra. I was unable to create circles for the unlocking sequence so I opted to make it a smaller rectangle and allowed for room to display the correct button pushes on the side as seen in the video below.

https://user-images.githubusercontent.com/89855265/134968515-ba0deafb-4592-4d2b-9b2b-3136c45dbf39.mov






