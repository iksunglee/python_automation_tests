import pyautogui, time, tkinter
from tkinter import *
from tkinter import messagebox

pyautogui.PAUSE =1
pyautogui.FAILSAFE = True


print("what music would like sir? ")
music = input()
print("input outlook email id: ")
email = input()
print("Starting...")


#music
time.sleep(3)
pyautogui.click(637, 743)
time.sleep(5)
pyautogui.click(300, 50)
pyautogui.typewrite('www.youtube.com\n')
time.sleep(4)
pyautogui.click(258, 109)
pyautogui.typewrite(music+'\n')
time.sleep(2)
pyautogui.click(450, 243)
time.sleep(1)



#internet email
pyautogui.click(704, 751)
time.sleep(5)
pyautogui.click(238, 37)
pyautogui.typewrite('www.outlook.com\n')
time.sleep(4)
pyautogui.click(785, 526)
pyautogui.click(692, 269)
pyautogui.typewrite(email+'\n')
time.sleep(2)
pyautogui.click(683,248)
#pyautogui.typewrite('')

#window pop-up tkinter application

top = Tk()
top.geometry("100x100")

messagebox.showinfo("Blake AI", "All Set Sir, Andrew")

top.mainloop
