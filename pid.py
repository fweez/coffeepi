#!/usr/bin/env python

class Pid:
    lastTime = -1

    def __init__(self, setpoint, initialPosition):
        self.setpoint = setpoint

    def update(self, position, t):
        error = self.setpoint - position
        return self.proportion(error) + self.integral(error) + self.differential(position)

    proportionGain = 0.5
    def proportion(self, error):
        return error * self.proportionGain

    integralGain = 0.5
    integralState = 0
    integralStateMax = 2
    integralStateMin = 0
    def integral(self, error):
        self.integralState += error
        if self.integralState > self.integralStateMax:
            self.integralState = self.integralStateMax
        if self.integralState < self.integralStateMin:
            self.integralState = self.integralStateMin
        return self.integralState * self.integralGain

    differentialGain = 0.2
    lastPosition = 0
    def differential(self, position):
        d = self.differentialGain * (position - self.lastPosition)
        self.lastPosition = position
        return d

if __name__ == "__main__":
    # Run a crude testing simulator
    t = 0
    ambient = 18
    
    pid = Pid(93, ambient)

    temp = ambient
    while 1:
        t = t + 1
        temp = (0.999 * (temp - ambient)) + ambient
        drive = pid.update(temp, t)
        if drive > 2:
            drive = 2
        if drive < 0:
            drive = 0
        temp += drive
        
        print ambient, pid.setpoint, drive, temp
        i = raw_input()
        if i == 'p':
            temp = temp - 15
