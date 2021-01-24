#!/usr/bin/python3
import RPi.GPIO as GPIO
from signal import pause
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

dutyCycleServo1 = 2 # default value of duty cycle
dutyCycleServo2 = 2 # default value of duty cycle

# when button is pressed, check the pin number
# and then either move the motor CW or CCW
def pressed1(pin):
    global dutyCycleServo1
    global btn1Servo1
    global btn2Servo1

    if pin == btn1Servo1 and dutyCycleServo1 <= 12:
        dutyCycleServo1 += 1
        servo1.ChangeDutyCycle(dutyCycleServo1)
        sleep(0.5)
        servo1.ChangeDutyCycle(0)
    elif pin == btn2Servo1 and dutyCycleServo1 >= 2:
        dutyCycleServo1 -= 1
        servo1.ChangeDutyCycle(dutyCycleServo1)
        sleep(0.5)
        servo1.ChangeDutyCycle(0)

    # only use the following line for debugging
    #print(str(pin) + " pressed")


def pressed2(pin):
    global dutyCycleServo2
    global btn1Servo2
    global btn2Servo2

    if pin == btn1Servo2 and dutyCycleServo2 <= 12:
        dutyCycleServo2 += 1
        servo2.ChangeDutyCycle(dutyCycleServo2)
        sleep(0.5)
        servo2.ChangeDutyCycle(0)
    elif pin == btn2Servo2 and dutyCycleServo2 >= 2:
        dutyCycleServo2 -= 1
        servo2.ChangeDutyCycle(dutyCycleServo2)
        sleep(0.5)
        servo2.ChangeDutyCycle(0)

    # only use the following line for debugging
    #print(str(pin) + " pressed")

def exiit(pin):
    servo1.ChangeDutyCycle(2)
    sleep(0.5)
    servo2.ChangeDutyCycle(2)
    sleep(0.5)
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
    print("** EXIT **")
    exit()

# SERVO
GPIO.setup(17,GPIO.OUT)
servo1 = GPIO.PWM(17,50) # pin 11 for servo1
GPIO.setup(18,GPIO.OUT)
servo2 = GPIO.PWM(18,50) # pin 12 for servo2

# Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

# INITIALIZE GPIO PINS
btn1Servo1 = 19
btn2Servo1 = 13
btn1Servo2 = 6
btn2Servo2 = 5
btnExit = 26

# BUTTON - SERVO 1
GPIO.setup(btn1Servo1, GPIO.IN, GPIO.PUD_UP) # CW
GPIO.setup(btn2Servo1, GPIO.IN, GPIO.PUD_UP) # CCW

# BUTTON - SERVO 2
GPIO.setup(btn1Servo2, GPIO.IN, GPIO.PUD_UP) # CW
GPIO.setup(btn2Servo2, GPIO.IN, GPIO.PUD_UP) # CCW

# Exit button
GPIO.setup(btnExit, GPIO.IN, GPIO.PUD_UP)

GPIO.add_event_detect(btn1Servo1, GPIO.FALLING, pressed1)
GPIO.add_event_detect(btn2Servo1, GPIO.FALLING, pressed1)
GPIO.add_event_detect(btn1Servo2, GPIO.FALLING, pressed2)
GPIO.add_event_detect(btn2Servo2, GPIO.FALLING, pressed2)
GPIO.add_event_detect(btnExit, GPIO.FALLING, exiit)
#GPIO.add_event_detect(26, GPIO.RISING, released)

print("All systems ready...")
pause()
