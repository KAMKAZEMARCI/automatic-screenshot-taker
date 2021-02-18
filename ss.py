import pyautogui, time
from time import sleep

##########
count = 0#
##########

while True:
    time.sleep(10)
    count += 1 
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'Screenshot\screenshot{}.png'.format(count))