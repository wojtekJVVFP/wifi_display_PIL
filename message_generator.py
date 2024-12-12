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
def image_to_bytes(image):
    return {'width': image.width, 'height': image.height, 'image_data':  image.tobytes()}
def bytes_to_image(input: bytes, width: int, height: int) -> Image:
    return Image.frombytes('RGB', (width,height), input)

def send_surface(surf, target_ws_device):
    #messa = []
    spak = pg.image.tostring(surf, 'RGB') # obrazki na telefony w formie bytes do wysłania

    surf_size = (surf.get_width(), surf.get_height())
    surf_size_bytes = pickle.dumps(surf_size)
    beginning = len(surf_size_bytes)
    beginning_bytes = beginning.to_bytes(2,'little')
    load = beginning_bytes + surf_size_bytes
    message = load + spak
    #messa.append((local_device, message))
    asyncio.run(ws_comm(message, target_ws_device))


def image_to_message(image):
    #str_image = pg.image.tostring(image, 'RGB')  # obrazki na telefony w formie bytes do wysłania
    image_dict = image_to_bytes(image)
    str_image = image_dict['image_data']
    #błąd bytes_image = str_image.encode()
    list_image = list(str_image)
    message = {
        "width": image_dict['width'],
        "height": image_dict['height'],
        "image_data": list_image
    }
    #obr_size_bytes = json.dumps(obr_size)
    #beginning = len(obr_size_bytes)
    #beginning_bytes = beginning.to_bytes(2, 'little')
    #load = beginning_bytes + obr_size_bytes
    #surface = pg.Surface((image.get_width, image.get_height,)
    json_image = json.dumps(message)

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