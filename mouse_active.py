import pyautogui;
import time;
x = 240
y = 1070
i = 1
time.sleep(30)
while True:
    for i in range(1, 5):

        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(3)
        x += 40
    x = 240