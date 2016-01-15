#/usr/bin/env python

from SSD1331 import *
import glob
import RPi.GPIO as GPIO

def currtemp():
    device_paths = glob.glob('/sys/bus/w1/devices/28*')
    temps = []
    for path in device_paths:
        with open(path + "/w1_slave") as f:
            lines = f.readlines()
            if len(lines) != 2:
                print "Invalid output from", path
                continue
            valid = lines[0][-4:] == 'YES\n'
            if not valid:
                print path, "does not have a temperature"
                continue
            temps.append(float(lines[1][-6:].strip()) / 1000)
    return temps
                
if __name__ == "__main__":
    device = SSD1331(SSD1331_PIN_DC, SSD1331_PIN_RST, SSD1331_PIN_CS)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    try:
        while 1:
            temps = currtemp()
            y = 0
            for idx, temp in enumerate(temps):
                device.DrawStringBg(0, y, "Sensor " + str(idx) + ": " + str(temp), COLOR_WHITE, COLOR_RED)
                y += 10

            if GPIO.input(17):
                device.DrawStringBg(0, y, "Button on", COLOR_WHITE, COLOR_BLUE)
                GPIO.output(18, 1)
            else:
                device.DrawStringBg(0, y, "Button off", COLOR_WHITE, COLOR_BLUE)
                GPIO.output(18, 0)
                    
    finally:
        device.Remove()

