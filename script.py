import pyautogui, time
time.sleep(5)
f = open("YourTextHere.txt", 'r')
for i in f:
    pyautogui.typewrite(i)
    pyautogui.press("enter")