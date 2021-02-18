import pyautogui, time #imports pyautogui and time modules
from time import sleep #imports sleep from time module

##########
count = 0#  #counter
##########

while True:
    time.sleep(10) #you can change the time if u want (second)
    count += 1 #Don't change this
    myScreenshot = pyautogui.screenshot() #Takes the screenshot
    myScreenshot.save(r'path here\screenshot{}.png'.format(count)) #saves the screenshot, change "path here".
