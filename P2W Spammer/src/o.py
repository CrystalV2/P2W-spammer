import keyboard
import pyautogui
import time
p=0
a=(input("cooldown of each message: "))
b=(input("delay before the nuke: "))
c=(input("text to nuke with: "))
d=(input('amount of nukes: '))






if len(a)<=2:
    p=1
else:
    p=0
    
time.sleep(int(b))
for i in range(int(d)):
    time.sleep(0.01)
    keyboard.press('t')
    time.sleep(0.01)
    keyboard.write(c) 
    time.sleep(0.01)
    keyboard.press('enter')
    if p==1:
        time.sleep(float(a))
    elif p==0:
        time.sleep(int(a))
    time.sleep(0.05)

exec(open("o.py").read())