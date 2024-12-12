
import json
from websocket_devices import Ws_devices, devices



surf_size = [10,30,40,60]
# surf_size_bytes = json.dumps(surf_size) #serializacja
#
# decoded = json.loads(surf_size_bytes)


print(surf_size_bytes)
print("zdekodowane", decoded)


# spak = pickle.dumps(devices) # zamiana obiektu na postać bajtową
#
# rozpak = pickle.loads(spak) #przywrócenie obiektu ze strumienia bajtów
# print(rozpak[2].ip)
#
#
#
# lis = [4,5,237]
# a = bytearray(lis)
# a1 = bytes(lis)
#
#
# a[2]=6 # do obiektu tego typu można przypisać nowe dane
# #a1[2]=6 # ta instrukcja wygeneruje błąd
#
# adec = a.decode()
# print(a, str(adec[0]), a1)
#
#
# int1 = 1
# st = f'{int1:5d}'
# print(len(st), st)
#
# ms = 'wert'
# print(ms[2:4])