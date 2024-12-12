
import tkinter
from tkinter import ttk, messagebox, Tk
from PIL import Image, ImageTk, ImageOps
import os
import asyncio

def image_save(image_name: str) -> bytes:
    with Image.open(image_name) as im:
        return im.tobytes()
def bytes_to_image(input: bytes, width, height) -> Image:
    return Image.frombytes('RGB', (width,height), input)

def quit_command(tk):
    global task_ui
    print('test')
    try:
        task_ui.cancel('cancelled')
        tk.destroy()
        global loop_running
        loop_running = False
    except asyncio.CancelledError:
        ...
def window_close(tk):
    close = messagebox.askyesno("Exit?", "Are you sure you want to exit?")
    if close:
        quit_command(tk)

async def ui():
    root = Tk()
    global loop_running
    loop_running = True

    # # Create a photoimage object of the image in the path
    im = Image.open(os.path.join('obrazy', 'dodge2.bmp'))
    test = ImageTk.PhotoImage(im)

    im_large = ImageOps.scale(im, 0.4)
    test_large = ImageTk.PhotoImage(im_large)

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    root.protocol("WM_DELETE_WINDOW", lambda: window_close(root))

    ttk.Label(frm, image=test).grid(column=0, row=0)
    ttk.Label(frm, image=test_large).grid(column=1, row=0)
    ttk.Button(frm, text='Quit', command=lambda: quit_command(root)).grid(column=0, row=1)

    # label1 = tkinter.Label(image=test)

    # label1.image = test

    ## Position image
    #label1.place(x=0, y=0)
    while loop_running:
        root.update()
async def tu():
    print("counter")


async def main():
    global task_ui
    task_ui = asyncio.create_task(ui())
    try:
        await task_ui
    except asyncio.CancelledError:
        print('task_ui cancelled')



asyncio.run(main())

# by = image_save(os.path.join('obrazy', 'test_1pik.bmp'))
# im = bytes_to_image(by, 50, 50)
# im.show('te')
