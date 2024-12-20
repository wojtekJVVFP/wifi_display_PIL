class Disp_data():
    def __init__(self, resolution: tuple, dpi: int):
        self.resolution = resolution
        self.dpi = dpi

class Ws_devices():
    def __init__(self, ip, name, greet, isActive, resolution=(640,480), dpi = 500):
        self.ip = ip
        self.name = name
        self.greet = greet
        self.port_no = '8765' # można zmienić numer portu dla danego urządzenia jeśli jest inny
        self.isActive = isActive
        #self.resolution = resolution # tuple (szer, wys), szerokość mniejsza
        self.disp_data = Disp_data(resolution, dpi)
    def return_address(self):
        return 'ws://'+self.ip+':'+self.port_no


devices = []
devices.append(Ws_devices(ip='localhost', name='lokalne', greet='jestem lokalne', isActive = True, resolution = (1000, 1000), dpi = 127))               #0
devices.append(Ws_devices(ip='192.168.1.117', name='samsung note 9', greet='jestem note 9', isActive = True, resolution = (1440, 2990), dpi = 514))   #1
devices.append(Ws_devices(ip='192.168.1.107', name='samsung J5 #1', greet='jestem J5 mamy', isActive = False, resolution = (720, 1280)))    #2
devices.append(Ws_devices(ip='192.168.1.108', name='samsung xCover', greet='jestem xCover', isActive = False, resolution = (480, 800), dpi = 207))     #3
devices.append(Ws_devices(ip='192.168.1.109', name='samsung J5 #2', greet='jestem J5 #2', isActive = False, resolution = (720, 1280)))    #4
devices.append(Ws_devices(ip='192.168.1.110', name='Xiaomi Redmi Szczep', greet='Redmi Szczep', isActive = False, resolution = (720, 1280)))    #5
devices.append(Ws_devices(ip='192.168.1.111', name='Xiaomi Redmi Bogd', greet='Redmi Bogd', isActive = False, resolution = (720, 1280)))    #6
devices.append(Ws_devices(ip='192.168.1.103', name='Galaxy Tab S7', greet='Tab S7', isActive = False, resolution = (2800, 1752), dpi = 226))    #7
devices.append(Ws_devices(ip='192.168.1.115', name='LG G2 mini', greet='g2 mini', isActive = False, resolution = (540, 960), dpi = 234))    #8