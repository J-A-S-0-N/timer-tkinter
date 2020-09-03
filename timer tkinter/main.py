from tkinter import *
from time import sleep
from playsound import playsound
import os


root = Tk()

font = ("Helventica", 19)

# def change(num):
#     label.config(root, text = num)
def playSound():
    name = ""
    os.chdir("C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\tkinter app1\\sound")
    playsound(name)

def command1():
    Button.pack_forget(root)

    for i in range(0,10):
        label.config(root, text = str(i))
        sleep(1)
        if i == 0:
            playSound()

def printText(string):
    label = Label(root, text = string, font = ("Helventica", 19))
    label.config(text = string)
    label.place(relx = 0.5, rely = 0.5, anchor = 'center')

root.title("timer")
root.geometry("300x300")

label = Label(root, text = "start?", font = ("Helventica", 19))
label.place(relx = 0.5, rely = 0.5, anchor = 'center')
label.pack()

button = Button(root, text = "yes", command=command1())
button.pack()
# for i in range(0,10):
#     label.config(root, text = str(i))
#     sleep(1)

root.mainloop()