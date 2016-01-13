#/usr/bin/env python

from SSD1331 import *

if __name__ == "__main__":
    raw_balloon  = GetRawPixelDataFromBmp24File("balloon.bmp")
    data_balloon = UnpackRawPixelBmp24Data(raw_balloon)
    raw_splash = GetRawPixelDataFromBmp24File("splash.bmp")
    data_splash = UnpackRawPixelBmp24Data(raw_splash)
    device = SSD1331(SSD1331_PIN_DC, SSD1331_PIN_RST, SSD1331_PIN_CS)
    try:
        while 1:
            device.DrawFullScreenBitMap(data_balloon)
            print "drew balloon"
            device.DrawFullScreenBitMap(data_splash)
            print "drew splash"
    finally:
        device.Remove()

