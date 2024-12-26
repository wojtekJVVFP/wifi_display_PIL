from websocket_devices import Disp_data, devices

#returns expanding coefficient
def fit_to_screen(base_disp: Disp_data, fit_screen: Disp_data) -> float:
    return fit_screen.dpi/base_disp.dpi
    print(base_disp.resolution[0], base_disp.dpi)

def calc_scaled_resolution(disp: Disp_data, base_disp: Disp_data) -> tuple[int, int]:  #scaling the resolution of the device to the base dpi
    scale_coef = base_disp.dpi / disp.dpi
    return (int(disp.resolution[0]*scale_coef), int(disp.resolution[1]*scale_coef))

#converting margins from disp to pixels according to base_disp
def convert_margins(disp: Disp_data, base_disp: Disp_data)->list:
    ret = []
    for i in disp.margins:
        ret.append(mm_to_pixel(base_disp, i))
    return ret


if __name__ == '__main__':
    #fit_to_screen(devices[0].disp_data, devices[1].disp_data)
    print(mm_to_pixel(devices[0].disp_data, 10))
    print(convert_margins(devices[0].disp_data, devices[0].disp_data))

