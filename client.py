import io

from websocket_devices import Ws_devices, devices
from PIL import Image
from image_splitter import image_split
from message_generator import send_message, image_to_message, message_to_array
import json
import os
import itertools
import time

DEVICE_NO = 0
DEBUG_MESSAGE = False
local_device = devices[DEVICE_NO]

print(local_device.return_address())

WIDTH, HEIGHT = 1024, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def dodaj_czas(kom: str, l:list):
    l.append((kom, time.monotonic()))

def diff(l:list) -> list:
    dif = []
    for i in range(0, len(l)):
        if i > 0:
            kom = "czas pomiędzy: " + l[i-1][0] + ', a: ' + l[i][0]
            kom_war = (kom, 1000*(l[i][1]-l[i-1][1]))
            dif.append(kom_war)
            print(kom_war)
    return dif

# prost = pg.Rect(30,20,200,400)
# for i in range(1,15,1):
#     prost = pg.Rect(i*60, i*70, 200, 400)
#     pg.draw.rect(obr, BLACK, prost, width=4)

# target_devices = []
# target_devices.append(devices[1])

#send_surface(obr, target_device)
czasy = []
dodaj_czas('pocz', czasy)

path = os.path.join('obrazy', 'wes.jpg')   #tram1.jpg
image = Image.open(path)

image_string = io.BytesIO()
image.save(image_string, "JPEG")    #writing image to bytesIO object
image_bytes = image_string.getvalue()   #to bytes

secondary_image_io = io.BytesIO()   #receiving data from the bytes
secondary_image_io.write(image_bytes)

secondary_image = Image.open(secondary_image_io)


print('image_bytes: ', len(image_bytes))

dodaj_czas('przed image_split', czasy)

dev_order, images = image_split(image, 3)

dodaj_czas('przed for dev,im', czasy)

print('rozmiar image: ', len(images))



for dev, im in zip(dev_order, images):




    json_message = image_to_message(im) #spakowanie do danej typu dict i do json
    print('rozmiar wiadomości: ', len(json_message))
    if DEBUG_MESSAGE:
        print(json_message)
    #dim3 = message_to_array(json_message)
    #send_message(json_message, local_device)

    dodaj_czas('przed send_message', czasy)

    send_message(json_message, devices[dev])

    dodaj_czas('po send_message', czasy)
#send_message('hello', local_device)
print(czasy)
diff(czasy)
# for i in test_images:
#     json_message = image_to_message(i) #spakowanie do danej typu dict i do json
#     dim3 = message_to_array(json_message)
#     send_message(json_message, local_device)




