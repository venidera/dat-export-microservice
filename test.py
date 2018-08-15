

from pyvirtualdisplay import Display as pvDisp
from Xlib.display import Display
import pyautogui
import os
from easyprocess import EasyProcess
from time import sleep

display = pvDisp(backend='xvfb', visible=True, size=(1000, 600))
# Starting pyvirtualdisplay
display.start()

pyautogui.FAILSAFE = False
pyautogui._pyautogui_x11._display = Display(os.environ['DISPLAY'])
print(os.environ['DISPLAY'])
os.environ['WINEPREFIX'] = '/home/andre/git/vazoes-export-ms/wine-bottle'
with EasyProcess('/usr/bin/wine /home/andre/git/vazoes-export-ms/thirdparty/VazEdit.exe'):
    sleep(2)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('right')
    pyautogui.hotkey('space')
    pyautogui.hotkey('tab')
    pyautogui.typewrite('oi')
    sleep(100)
# Destroying PyVirtualDisplay process
# display.sendstop()
