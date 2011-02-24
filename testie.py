#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: GPL v3
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
 
def showxy(event):
    xm = event.x
    ym = event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym)
    tk.title(str1)
    # switch color to red if mouse enters a set location range
    x = 463
    y = 447
    delta = 100  # range
    if abs(xm - x) < delta and abs(ym - y) < delta:
        return
    else:
        return
 
def showxy2(event):
    xm = event.x
    ym = event.y
    str1 = "YAY at x=%d  y=%d" % (xm, ym)
    tk.title(str1)
    # switch color to red if mouse enters a set location range
    x = 463
    y = 447
    delta = 100  # range
    if abs(xm - x) < delta and abs(ym - y) < delta:
        print "YAYAYAYAY!!!! x=%d  y=%d" % (xm, ym)
    else:
        return
 
def startgame():
    # Do something
    return

tk.title("Angry Tux")
can = Tkinter.Canvas(tk, width=1024, height=724)
can.bind("<Motion>", showxy)
can.bind("<Button-1>", showxy2)
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
