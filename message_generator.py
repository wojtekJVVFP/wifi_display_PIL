import io
import struct
import pickle
import asyncio
import websockets
import json
from ws_client import ws_comm
from PIL import Image, ImageTk

def image_file_to_bytes(image_name: str):
    with Image.open(image_name) as im:
        return {'width': im.width, 'height': im.height, 'image_data':  im.tobytes()}
def image_to_dict(image) -> dict:
    image_bytesIO = io.BytesIO()
    image.save(image_bytesIO, "JPEG")  # writing image to bytesIO object
    image_bytes = image_bytesIO.getvalue()  # to bytes

    image_list = list(image_bytes)
    print('rozmiar image_list: ', len(image_list))
    return {'width': image.width, 'height': image.height, 'image_data': image_list }

def image_to_list(image) -> list:
    image_bytesIO = io.BytesIO()
    image.save(image_bytesIO, "JPEG")  # writing image to bytesIO object
    image_bytes = image_bytesIO.getvalue()  # to bytes

    image_list = list(image_bytes)
    #image_list = list(image_.tobytes())
    print('rozmiar image_list: ', len(image_list))
    return image_list
def bytes_to_image(input: bytes, width: int, height: int) -> Image:
    return Image.frombytes('RGB', (width,height), input)

def image_to_message(image):
    image_list = image_to_list(image)
    json_image = json.dumps(image_list)

    return json_image

def message_to_array(json_message):
    message_dict = json.loads(json_message) #message_dict to odkodowany ciąg json (typ dict)
    unpacked_message = message_dict["image_data"]
    width = message_dict["width"]
    height = message_dict["height"]

def send_message(message, target):
    asyncio.run(ws_comm(message, target))