from websocket_devices import Ws_devices, devices
from image_ops import fit_to_screen, calc_scaled_resolution
from PIL import ImageOps, Image
import os
from itertools import chain

class Image_split():
    def __init__(self):
        pass

#device_order = [3, 6, 7, 5]
#device_order = [0]
def image_split(image, base_dev_no):
    #device_layout = [[1, 3],
     #                [8, 6]] #how the devices are located
    device_layout = [[0]]


    base_disp = devices[base_dev_no].disp_data
    start_pos = [0,0] #current crop point (left upper corner)
    images = []
    points = [] #list of points


    for row in range(len(device_layout)):
        points.append([])
        for i, dev_no in enumerate(device_layout[row]):
            device = devices[dev_no]
            dev_res = device.disp_data.resolution
            scaled_res = calc_scaled_resolution(device.disp_data, base_disp)
            print(device.disp_data.resolution)
            print(scaled_res)

            image_upper =  start_pos[1]#
            image_left = start_pos[0]#

            if row == 0:
                if i == 0:  #row = 0, i=0
                    points[row].append([scaled_res[0]+start_pos[0], scaled_res[1]+start_pos[1]])    #first column with x=0
                else:   #row=0, i>0
                    points[row].append([points[row][i-1][0] + scaled_res[0], scaled_res[1]+start_pos[1]])
                    image_left = points[row][i - 1][0]
            else:   #row > 0
                if i == 0:  #row > 0, i=0
                    points[row].append([scaled_res[0]+start_pos[0], scaled_res[1]+points[row-1][i][1]])    #first column with x=0
                else:   #row > 0, i>0
                    points[row].append([scaled_res[0]+points[row][i-1][0], scaled_res[1]+points[row-1][i][1]])
                    image_left = points[row][i - 1][0]
                image_upper =  points[row-1][i][1]

            #image_left = points[row][i-1][0]
            image_right = points[row][i][0]
            image_lower = points[row][i][1]

            cropped_image = image.crop((image_left, image_upper, image_right, image_lower))    #crop (left, upper, right, lower)
            images.append(cropped_image)
            #cropped_image.show()
    print(points)
    device_order = list(chain.from_iterable(device_layout)) #flat version of devide_layout
    return device_order, images

        #ret = ImageOps.scale(cropped_image, fit_to_screen(base_disp, device.disp_data))

    #return ImageOps.cover(ret_image, dev_res)

    # x_coord = 0
    # for i in device_order:
    #     if i == dev_no: # jeśli jest znalezione aktualne urządzenie to koniec pętli, x_coord zostało znalezione
    #         break
    #     else:
    #         x_coord += devices[i].resolution[0]
    # ret_sur.blit(image, (-x_coord,0))

if __name__ == '__main__':
    im = Image.open(os.path.join('obrazy', 'tram1.jpg'))
    image_split(im, 0)
    #im3 = im.crop(box=(100, 0, 200, 500)) #crop (left, upper, right, lower)
    #im3.show()




