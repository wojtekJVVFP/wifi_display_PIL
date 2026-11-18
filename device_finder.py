#funkcja używana do przeszukiwania określonej podsieci do znaleznienia serwerów websocket i zapisania danych odebranych od nich
#serwery są kolejnymi urządzeniami, które jako zwrotne dane zwracają nazwy, wymiary wyświetlacza i jego gęstość
'''
Funkcja ma wysłać przykładowe zdjęcie do urządzenia i odebrać dane od niego. Dane mają być zapisane na liście urządzeń
+ Przeszukiwanie IP w określonym adresie i zbieranie danych
+ znalezione dane zapisać do pliku
- usunąć zbędne pola z ws_devices



'''


import os
from websocket_devices import Ws_devices, devices
import asyncio
import websockets
import websockets.exceptions
import json
from PIL import Image
from message_generator import send_message, image_to_message, message_to_array
#from image_splitter import image_split

addresses = ['ws://192.168.1.116:8765', 'ws://localhost:8765']
path = os.path.join('obrazy', 'test_1pik.jpg')   #utworzenie ścieżki do obrazu
example_image = Image.open(path)
#cropped_image = image.crop((0,0,100,100))
json_message = image_to_message(example_image) #spakowanie do danej typu dict i do json
device_list = []  # list for storing data from device finder, objects class Ws_devices

def dict_to_devices(data_dict):
    pass


async def find_device(message, device_ip_addr):
    ip_subnet_addr = 'ws://192.168.1.'#-------------------

    port = ':8765'
    local_ip = "ws://localhost:8765"
    for i in range(193,194):
        try:
            #check_ip = ip_subnet_addr + str(i) + port
            check_ip = local_ip
            print(check_ip)
            async with websockets.connect(check_ip, open_timeout = 1) as websocket:
                    await websocket.send(message)
                    received = await websocket.recv()
                    data_dict = json.loads(received)
                    print('dane: ' + data_dict['name'] + ', screen width: ' + str(data_dict['width_px']) + ', screen height: ' + str(data_dict['height_px']) + ', dpi: ' + str(data_dict['dpi']))
                    current_device = Ws_devices(ip=check_ip, name=data_dict['name'], resolution=(data_dict['width_px'], data_dict['height_px']), dpi=data_dict['dpi'])
                    print(current_device)
                    device_list.append(current_device)

        except websockets.exceptions.InvalidURI as e:
            print(e.uri)
            print(e.msg)
            continue
        except asyncio.exceptions.TimeoutError:
            print("asyncio timeout")

def dict_to_ws_devices(dict: {}):  # translating dict with phone config to Ws_devices object
    #for key, value in vars
    return Ws_devices(ip = dict['ip'], name = dict['name'],
                      resolution = dict['resolution'], dpi = dict['dpi'])


def save_config_to_file(device_list: list[Ws_devices]):
    file_name = "phone_config.txt"
    temp = []
    for row in device_list:  # creating list of dicts
        temp.append(row.to_dict())
    with open(file_name, 'w') as f:
        json.dump(temp, f)

def read_config_from_file(file_name):
    with open(file_name, 'r') as f:
        decoded_config = json.load(f) #decoded config is list of dictionaries
        for i in decoded_config:
            print(dict_to_ws_devices(i))

   
if __name__ == '__main__':
    asyncio.run(find_device(json_message, addresses[1]))
    save_config_to_file(device_list)
    read_config_from_file('phone_config.txt')

