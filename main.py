import pygame
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
mh = Adafruit_MotorHAT(addr=0x60)
pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

def turnOffMotors():
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    atexit.register(turnOffMotors)
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

#Initialize Joysticks
for i in range (joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

while (loop == True):

        pygame.event.pump()
        axesHZ = joystick.get_axis(0)
        axesTurn = axesHZ
        if (axesHZ < 0):
            axesHZ = (axesHZ*(-1))
        axesVT = round((joystick.get_axis(1) * float(-150)))
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
                if (axesTurn > 0):
                    axesMotorRT = (axesVT *(1- axesHZ))
                elif (axesTurn < 0):
                    axesMotorLT = (axesVT *(1- axesHZ))
                r = int(axesMotorLT)
                l = int(axesMotorRT)
                try:
                    myMotorLT.setSpeed(l)
                    myMotorRT.setSpeed(r)
                except OSError:
                    mh = Adafruit_MotorHAT(addr=0x60)
                    print ("error error error error error")
                print ("LEFT: ",  l)
                print ("RIGHT: ",  r)

            elif (axesVT == 0 and axesHZ ==0):
                myMotorRT.run(Adafruit_MotorHAT.RELEASE);
                myMotorLT.run(Adafruit_MotorHAT.RELEASE);
                print ("release")

