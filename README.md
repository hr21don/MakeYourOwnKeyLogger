# MakeYourOwnKeyLogger
Creating a basic keylogger that records &amp; stores key strokes from keyboard onto a logfile using python. 

## History 
A keylogger is a type of surveillance technology used to monitor and record each keystroke typed on a specific computer's keyboard.

## Something useful?
Well, a script kiddie uses this for unethical purposes, he or she will register everything you type in the keyboard including your credentials (credit card numbers, passwords, etc.).

The goal of this tutorial is to make you aware of these kind of scripts as well as learning how to implement such malicious scripts on your own for educational purposes, let's get started!

## Input Requirements

 * Should be able to listen to user keystrokes in the background
 * Should be able to add a key to a global string variable (condition: pressed and released)
 * Should be able to report the content of this string variable to a local file. 

## Output 

You should be able to view the content of log file to display something like this 

Here are some example results!

```
 2021-12-09 x:x:x,860 - Key.alt_l
 2021-12-09 x:x:x,927 - Key.tab
 2021-12-09 x:x:x,170 - Key.enter
 2021-12-09 x:x:x,336 - Key.enter
 2021-12-09 x:x:x,546 - '#'
 2021-12-09 x:x:x,702 - '#'
 2021-12-09 x:x:x,002 - Key.space
 2021-12-09 x:x:x,157 - Key.caps_lock
 2021-12-09 x:x:x,272 - 'h'
 2021-12-09 x:x:x,386 - Key.caps_lock
 2021-12-09 x:x:x,438 - 'o'
 2021-12-09 x:x:x,603 - 'w'
 2021-12-09 x:x:x,633 - Key.space
 2021-12-09 x:x:x,842 - 't'
 2021-12-09 x:x:x,885 - 'o'

```
 
## How to run? || Download the zip file to your downloads directory and extract it.

* Open up the file & change to the directory with test.py in it
* Run test.py locally and notice the creation of the log file on the system


