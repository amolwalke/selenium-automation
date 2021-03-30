import pyautogui as ps
import time

##ps.hotkey('winleft')
##time.sleep(3)
a=ps.prompt("type name of application:?")
print(a)
#ps.typewrite('')

'''
time.sleep(3)
ps.press('\n')

ps.hotkey('winleft','up')
'''
print(ps.position())
#pyautogui.moveTo()