import pyautogui as ps
import time

ps.click(x=221, y=1052)
time.sleep(5)
ps.typewrite("sni")
time.sleep(2)
print(ps.position())
ps.click(x=155, y=381)
time.sleep(2)
print(ps.position())
ps.click(x=872, y=301)

