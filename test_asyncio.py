import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import threading
import asyncio
import time

def button1_command(button: ttk.Button):
    button.config(text="wow")
    return

def button2_command(label: ttk.Label):
    global image_tk_obj
    label.config(image=image_tk_obj)
    return



def ui():
    root = Tk()

    # # Create a photoimage object of the image in the path
    image1 = Image.open(os.path.join('obrazy', 'dodge.bmp'))
    im2 = Image.open(os.path.join('obrazy', 'dodge2.bmp'))
    global image_tk_obj
    image_tk_obj = ImageTk.PhotoImage(image1)
    test2 = ImageTk.PhotoImage(im2)

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    label1 = ttk.Label(frm, image=test2)
    label1.grid(column=0, row=0)

    ttk.Button(frm, text='Quit', command=root.destroy).grid(column=0, row=1)
    button1 = ttk.Button(frm, text='press')
    ttk.Button(frm, text='im1', command=lambda: button2_command(label1)).grid(column=0, row=3)
    button1.grid(column=0, row=2)

    button1.config(command=lambda: button1_command(button1))

    # label1 = tkinter.Label(image=test)

    # label1.image = test


    ## Position image
    #label1.place(x=0, y=0)
    root.mainloop()

def tu():
    while True:
        print("counter")
        time.sleep(2)



async def main():
    R = await asyncio.gather(
        asyncio.to_thread(ui),
        #asyncio.to_thread(tu)
    )


asyncio.run(main())