import pygame
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
mh = Adafruit_MotorHAT(addr=0x60)
pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

while (joystick_count < 1):
    print ('Please Connect a Joy Stick: ',joystick_count)
    pygame.quit()
    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
        
#Initialize Global Variables
loop = True
repeatHZ = 0
repeatVT = 0
axesHZ = 0
axesVT = 0

#Set Motor Pin numbers
myMotorLT = mh.getMotor(3)
myMotorRT = mh.getMotor(4)
joystick = pygame.joystick.Joystick
#Initialize Joysticks
for i in range (joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

while (loop == True):
    axesVT = joystick.get_axis(1)
    axesHZ = joystick.get_axis(0)
    pygame.event.pump()
    axesVT = round((axesVT * float(-150)))
    if (repeatHZ != axesHZ or repeatVT != axesVT):
        repeatHZ = axesHZ
        repeatVT = axesVT
        if (axesVT > 0):
            try:
                myMotorRT.run(Adafruit_MotorHAT.FORWARD)
                myMotorLT.run(Adafruit_MotorHAT.FORWARD)
            except OSError:
                mh = Adafruit_MotorHAT(addr=0x60)
                print ("error error error error error")
            axesMotorRT = axesVT
            axesMotorLT = axesVT
            if (axesHZ > 0):
                axesMotorRT = (axesVT *(1- axesHZ))
                print('right')
            elif (axesHZ < 0):
                axesMotorLT = (axesVT *(1- (axesHZ*(-1))))
                print('left')
            try:
                myMotorLT.setSpeed(int(axesMotorLT))
                myMotorRT.setSpeed(int(axesMotorRT))
            except OSError:
                mh = Adafruit_MotorHAT(addr=0x60)
                print ("error error error error error")
           # print ("LEFT: ", axesMotorLT)
           # print ("RIGHT: ", axesMotorRT)

        elif (axesVT == 0 and axesHZ ==0):
            myMotorRT.run(Adafruit_MotorHAT.RELEASE);
            myMotorLT.run(Adafruit_MotorHAT.RELEASE);
            print ("release")

def forwar():
    
    pygame.event.pump()
    
