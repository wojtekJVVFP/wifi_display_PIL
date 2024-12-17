from websocket_devices import Ws_devices, devices
from PIL import Image
from image_splitter import image_split
from message_generator import send_surface, send_message, image_to_message, message_to_array
import json
import os
import itertools

DEVICE_NO = 0
DEBUG_MESSAGE = False
local_device = devices[DEVICE_NO]

print(local_device.return_address())

WIDTH, HEIGHT = 1024, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# prost = pg.Rect(30,20,200,400)
# for i in range(1,15,1):
#     prost = pg.Rect(i*60, i*70, 200, 400)
#     pg.draw.rect(obr, BLACK, prost, width=4)

target_devices = []
target_devices.append(devices[0])
target_devices.append(devices[1])

#send_surface(obr, target_device)

path = os.path.join('obrazy', 'tram1.jpg')
image = Image.open(path)
dev_order, images = image_split(image, 0)

for dev, im in zip(dev_order, images):
    json_message = image_to_message(im) #spakowanie do danej typu dict i do json
    if DEBUG_MESSAGE:
        print(json_message)
    #dim3 = message_to_array(json_message)
    #send_message(json_message, local_device)
    send_message(json_message, devices[dev])
#send_message('hello', local_device)

# for i in test_images:
#     json_message = image_to_message(i) #spakowanie do danej typu dict i do json
#     dim3 = message_to_array(json_message)
#     send_message(json_message, local_device)




