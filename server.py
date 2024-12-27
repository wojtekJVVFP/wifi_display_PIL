#27.12.2024 20:13

import io
import json
import asyncio
import websockets
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageOps
from image_ops import fit_to_screen
import os
from message_generator import image_to_message, message_to_array, bytes_to_image
from image_splitter import *
import time
from disp_no import DEVICE_NO, BASE_DISP  #number of current and base display

from websocket_devices import Ws_devices, devices
local_device = devices[DEVICE_NO]

image_update = False    #do synchronizowania odbioru z wyświetlaniem

def quit_command(tk):
    global task_websocket
    try:
        task_websocket.cancel('cancelled')
        tk.destroy()
    except asyncio.CancelledError:
        ...

def window_close(tk):
    close = messagebox.askyesno("Exit?", "Are you sure you want to exit?")
    if close:
        quit_command(tk)

async def ui():
    root = tk.Tk()
    global image_update
    global image_pil    #do przekazywania obiektu obrazu pil
    global window_size

    # # Create a photoimage object of the image in the path
    #im = Image.open(os.path.join('obrazy', 'test_cz.bmp'))

    #image_tk_obj = ImageTk.PhotoImage(im)
    #test2 = ImageTk.PhotoImage(im2)
    #imTk = ImageTk.PhotoImage(image_split(im2, 0))

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    root.protocol("WM_DELETE_WINDOW", lambda: window_close(root))

    label1 = ttk.Label(frm)#image=image_tk_obj
    label1.grid(column=0, row=0)

    ttk.Button(frm, text='Quit', command=lambda: quit_command(root)).grid(column=0, row=1)

    window_size = (root.winfo_screenwidth(), root.winfo_screenheight())

    while True:
        if image_update:
            print('image_update')
            test2 = ImageTk.PhotoImage(image_pil)
            label1.config(image=test2)
            await asyncio.sleep(.05)
            image_update = False
        root.update()
        await asyncio.sleep(.1)

'''
send1 - wysyłanie gotowej odpowiedzi na zapytanie od klienta

'''
async def send1(websocket):
    async for message in websocket:
        global image_pil
        global image_update
        global window_size
        print("Wiadomość odebrana:")

        image_file_array = json.loads(message)
        image_file_bytes = bytes(image_file_array)

        image_bytesIO = io.BytesIO()
        image_bytesIO.write(image_file_bytes)
        image_base_pil = Image.open(image_bytesIO)

        #image_base_pil = bytes_to_image(image_bytes, width, height)
        image_pil = ImageOps.scale(image_base_pil, fit_to_screen(devices[BASE_DISP].disp_data, devices[DEVICE_NO].disp_data))
        await asyncio.sleep(.05)
        image_update = True

        return_data_dict = {
            'data': local_device.greet,
            'width': image_base_pil.width,
            'height': image_base_pil.height,
            'window_width': window_size[0],
            'window_height': window_size[1]
        }
        await websocket.send(json.dumps(return_data_dict))



async def server_routine():
    async with websockets.serve(send1, local_device.ip, local_device.port_no, max_size=None):
        await asyncio.Future()  # run forever

async def main():
    #task_ui = asyncio.create_task(ui())
    global task_websocket
    task_websocket = asyncio.create_task(server_routine())
    task_ui = asyncio.create_task(ui())
    try:
        await task_websocket
    except asyncio.CancelledError:
        print('task_websocket cancelled')


WIDTH, HEIGHT = 1024, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


asyncio.run(main())
