import time

import pyautogui

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("https://www.youtube.com/")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=856 , y=111)
time.sleep(1)

pyautogui.write("elefante brandao")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=718 , y=367)
time.sleep(2)

pyautogui.alert("press OK and enjoy this moment")