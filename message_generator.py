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
    #image_list = list(image_.tobytes())
    print('rozmiar image_list: ', len(image_list))
    return {'width': image.width, 'height': image.height, 'image_data': image_list }
def bytes_to_image(input: bytes, width: int, height: int) -> Image:
    return Image.frombytes('RGB', (width,height), input)

def image_to_message(image):
    image_dict = image_to_dict(image)

    #str_image = image_dict['image_data']
    #błąd bytes_image = str_image.encode()
    #list_image = list(str_image)
    # message = {
    #     "width": image_dict['width'],
    #     "height": image_dict['height'],
    #     "image_data": list_image
    # }
    json_image = json.dumps(image_dict)

    return json_image

def message_to_array(json_message):
    message_dict = json.loads(json_message) #message_dict to odkodowany ciąg json (typ dict)
    unpacked_message = message_dict["image_data"]
    width = message_dict["width"]
    height = message_dict["height"]

    #ponizszy kod nie jest potrzebny do odkodowania danej, jest przykładem dla odkodowania i sprawdzenie formatu
    # t = []
    # for i in range(0,height):
    #     t.append([])
    #     for j in range(0,width):
    #         curr_byte = i*3*width+3*j
    #         t[i].append([unpacked_message[curr_byte], unpacked_message[curr_byte+1], unpacked_message[curr_byte+2]])
    #     #t.append(unpacked_message[i*3*width:(i+1)*3*width]) #dodane 3* ponieważ jest 3 razy więcej bajtów we wierszu z powodu kolorów
    #     print(t[i])
    #podział na poszczególne kolory
    #poszczególne wiersze będą jeszcze podzielone na kolory
    #tablica t, tablica trzywymiarowa t[wiersz][kolumna][R, G, B]
    # print(t[1][0]) #kolor z wiersza 1 i kolumny 0
    # print(t[0][4]) #kolor z wiersza 0 i kolumny 4, żółty
    # print(t[0][4][1]) #kolor z wiersza 0 i kolumny 4, składowa G(reen) koloru
    # print(t)


def send_message(message, target):
    asyncio.run(ws_comm(message, target))