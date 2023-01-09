import pyautogui
import time

words =open("word","r")
time.sleep(5)

for words in words :
    pyautogui.typewrite(words)
    pyautogui.press("enter")
    time.sleep(5)
