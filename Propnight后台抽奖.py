import time
import threading
import random

import keyboard
from win32api import GetKeyState

import win32gui
import win32con
import win32api

space = 0x20
run = 0

def checkkeyboard():
    global run
    while(1):
        time.sleep(0.1)
        if keyboard.is_pressed('=') and keyboard.is_pressed('ctrl'): 
             if(run == 0): 
                 run = 1
                 print("运行中...")
             else:
                 run = 0
                 print("停止中...")
             time.sleep(1)

def bkPress(a):
    win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, a, 0)
    time.sleep(0.05)
    win32api.PostMessage(hwndMain, win32con.WM_KEYUP, a, 0)

hwndMain = win32gui.FindWindow(None, "Propnight  ")
check = threading.Thread(target = checkkeyboard)
check.start()

print("长按Ctrl + = 以开关")

rand = 0
while(1):
    time.sleep(0.6+rand)
    if(run == 1):
        rand = random.uniform(0.1,0.3)
        bkPress(space)
                
