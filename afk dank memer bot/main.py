import pynput
import random
import time
from pynput.keyboard import Key, Controller
memetypes = ["n" , "e" , "r" , "d"]
keyboard = Controller()
i = 0

while i < 1:
    
    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    print('attempting to bet')
    time.sleep(2)
    keyboard.type('pls fish')
    keyboard.press(Key.enter)
    print('attempting to fish')
    time.sleep(3)
    keyboard.type('pls hunt')
    keyboard.press(Key.enter)
    print('attempting to hunt')
    time.sleep(3)
    keyboard.type('pls highlow')
    keyboard.press(Key.enter)
    print('running highlow')
    time.sleep(3)
    keyboard.type('low')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls slots 200')
    keyboard.press(Key.enter)
    print('attempting to win slots')
    time.sleep(3)
    keyboard.type('pls trivia')
    keyboard.press(Key.enter)
    print('attempting trivia')
    time.sleep(3)
    keyboard.type('c')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls postmeme')
    keyboard.press(Key.enter)
    print('attempting to postmeme')
    time.sleep(3)
    keyboard.type('r')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls work')
    keyboard.press(Key.enter)
    print('working')
    time.sleep(3)
    keyboard.type('asd')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls gamble 150')
    keyboard.press(Key.enter)
    print('trying to gamble')
    time.sleep(3)
    keyboard.type('pls lottery')
    keyboard.press(Key.enter)
    print('joining the lottery.....')
    time.sleep(3)
    keyboard.type('yes')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls daily')
    keyboard.press(Key.enter)
    print('getting daily money')
    time.sleep(3)
    print('Repeating!!!!')
    time.sleep(10)
    
    
