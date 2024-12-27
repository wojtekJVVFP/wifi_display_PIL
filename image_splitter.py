from websocket_devices import Ws_devices, devices
from image_ops import fit_to_screen, calc_scaled_resolution, convert_margins
from PIL import ImageOps, Image
import os
from itertools import chain

class Margins():
    def __init__(self, margin_list = [0,0,0,0]):
        self.left = margin_list[0]
        self.upper = margin_list[1]
        self.right = margin_list[2]
        self.lower = margin_list[3]


#device_order = [3, 6, 7, 5]
#device_order = [0]
def image_split(image, base_dev_no):
    device_layout = [[3, 1], [8, 6]]
    #[[3, 8, 6, 1]]
                     #[3, 8]] #how the devices are located
    #device_layout = [[1]]

    base_disp = devices[base_dev_no].disp_data
    start_pos = [0,0] #current crop point (left upper corner)
    images = []
    points = [] #list of points
    #dodac tablice dwuwymiarową z marginesami

    for row in range(len(device_layout)):
        points.append([])
        for i, dev_no in enumerate(device_layout[row]):
            device = devices[dev_no]
            disp_data = device.disp_data
            dev_res = device.disp_data.resolution

            current_margins = Margins(disp_data.calc_margins)    #margins (left, upper, right, lower)
            if i > 0:
                margins_on_the_left = Margins(devices[device_layout[row][i - 1]].disp_data.calc_margins)
            if row > 0:
                margins_above = Margins(devices[device_layout[row-1][i]].disp_data.calc_margins)

            scaled_res = calc_scaled_resolution(device.disp_data, base_disp)
            print(device.disp_data.resolution)
            print(scaled_res)

            image_upper =  start_pos[1] + current_margins.upper
            image_left = start_pos[0]

            if row == 0:
                if i == 0:  #row = 0, i=0
                     points[row].append([scaled_res[0] + start_pos[0] + current_margins.left, scaled_res[1] + start_pos[1] + current_margins.upper])    #first column with x=0
                else:   #row=0, i>0
                    points[row].append([points[row][i-1][0] + scaled_res[0] + margins_on_the_left.right + current_margins.right, scaled_res[1]+start_pos[1]+current_margins.upper])
                    image_left = points[row][i-1][0]
            else:   #row > 0
                if i == 0:  #row > 0, i=0
                    points[row].append([scaled_res[0]+start_pos[0]+current_margins.left, scaled_res[1]+points[row-1][i][1]+current_margins.upper+margins_above.lower])    #first column with x=0
                else:   #row > 0, i>0
                    points[row].append([scaled_res[0]+points[row][i-1][0]+current_margins.left+margins_on_the_left.right, scaled_res[1]+points[row-1][i][1]+current_margins.upper+margins_above.lower])
                    image_left = points[row][i - 1][0]
                image_upper =  points[row-1][i][1]

            #image_left = points[row][i-1][0]
            image_right = points[row][i][0]
            image_lower = points[row][i][1]

            cropped_image = image.crop((image_left, image_upper, image_right, image_lower))    #crop (left, upper, right, lower)
            images.append(cropped_image)
            #cropped_image.show()
    print(points)
    device_order = list(chain.from_iterable(device_layout)) #flat version of device_layout
    return device_order, images

if __name__ == '__main__':
    im = Image.open(os.path.join('obrazy', 'linie.jpg'))
    image_split(im, 0)
    #im3 = im.crop(box=(100, 0, 200, 500)) #crop (left, upper, right, lower)
    #im3.show()




