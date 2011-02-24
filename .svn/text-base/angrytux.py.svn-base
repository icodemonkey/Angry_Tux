#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: GPL v3
# file: angrytux.py
# Authors: lkjoeldev@gmail.com, (developers, add your e-mail address here)
import Tkinter
from Tkconstants import *

import tkMessageBox
import webbrowser
import time
import os
import sys
import Image
import ImageTk
import codecs
tk = Tkinter.Tk()
 
def motion(event):
    xm = event.x
    ym = event.y
    #x = 463
    #y = 447
    #delta = 100 # range
    #if abs(xm - x) < delta and abs(ym - y) < delta:
    #    print "x=%d  y=%d" % (xm, ym)
    #else:
    #    return
 
def clickleft(event):
    xm = event.x
    ym = event.y
    x = 460
    y = 446
    deltax = 110  # range for X
    deltay = 100 # range for Y
    if xm - x < deltax and xm -x > -1 and ym - y < deltay and ym - y > -1:
        startgame()
    else:
        return
 
def startgame():
    print "Clicked Play Button"
    # Do something
    return

tk.title("Angry Tux")
can = Tkinter.Canvas(tk, width=1024, height=724)
can.bind("<Motion>", motion)
can.bind("<Button-1>", clickleft)
can.pack(fill='both', expand='yes')
splash = Image.open("data/angrytux.jpg")
splashim = ImageTk.PhotoImage(splash)
can.create_image(512, 362, image=splashim)
#frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=5)
#frame.pack(fill=X, expand=1)
#label = Tkinter.Label(frame, text="Angry Tux")
#label.pack(fill=X, expand=1)
b1 = Tkinter.Button(tk, text="START", command=startgame, state=NORMAL)
b1.pack(side=BOTTOM)
tk.mainloop()
