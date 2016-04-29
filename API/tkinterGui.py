#!/usr/bin/env python

from Tkinter import *
from time import sleep
import Decoder
import thread

def clickMethod():
    print("Creating Thread")
    createThread()


def createThread():
    try:
        #thread.daemon = true
        thread.start_new_thread(startRefresh, ())
    except:
        print("Error: unable to start thread")
    #runT = thread(target = startRefresh)
    #runT.setDaemon(True)
    #runT.start()

def getPID():
    test = e1.get()
    #print(Decoder.SendOBD(test))
    Response.set(Decoder.SendOBD(test))

def startRefresh():
    while(1):
        speed.set(Decoder.getSpeed())
        rpm.set(Decoder.getRPM())
        sleep(0.5)


root = Tk()
global Response
global speed
global rpm
Response = StringVar()
speed = StringVar()
rpm = StringVar()
Decoder.setup()

startbutton = Button(root, text = 'Start', command = clickMethod).grid(row=0, column=0, columnspan=6)

Label(root, text = "Speed:").grid(row=1, column=0)
Label(root, textvariable=speed).grid(row=1, column=1)
Label(root, text = "km/h").grid(row=1, column=2)

Label(root, text = "Engine RPM:").grid(row=1, column=3)
Label(root, textvariable=rpm).grid(row=1, column=4)
Label(root, text = "rpm").grid(row=1, column=5)

Label(root, text = "PID Requested:").grid(row=2)
Label(root, text = "Response:").grid(row=3)
L3 = Label(root, textvariable=Response).grid(row=3, column=1, columnspan=5)
global e1
e1 = Entry(root)
e1.grid(row=2, column=1, columnspan=4)
button1 = Button(root, text = 'Send PID', command = getPID).grid(row=2, column=5)
getPID()
root.mainloop()
