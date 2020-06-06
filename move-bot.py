# run a raspberry pi robot using keyboard inputs
import curses
import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

# initialize servo for the robot's base
servoBase=GPIO.PWM(17,50)
servoBase.start(0)

# initialize curses to accept keyboard input
# from user
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# at the start, always change the servo's position to start.
# this is only for testing, may be removed later.

lastAngle=0
minAngle=18
servoBase.ChangeDutyCycle(2+(lastAngle/18))

# the main program starts
if __name__ == '__main__':

    while True:

        Char = screen.getch()


        # if the user presses the <- key on the keyboard
        # then we need to move the robot to the left by 30 degree.
        if Char == curses.KEY_LEFT and lastAngle <= 180:

            # set the angle as 15deg. more than the last angle.
            # after that, move the servo usingChangeDutyCycle
            # and ensure it doesn't jitter
            lastAngle += minAngle
            servoBase.ChangeDutyCycle(2+(lastAngle/18))
            time.sleep(0.4)
            servoBase.ChangeDutyCycle(0)
            time.sleep(0.1)
            print ("<-")

        #if the user presses the -> key then 
        # move the motor 15 deg. to the right.
        if Char == curses.KEY_RIGHT and lastAngle >= 0:
            lastAngle -= minAngle
            servoBase.ChangeDutyCycle(2+(lastAngle/18))
            time.sleep(0.4)
            servoBase.ChangeDutyCycle(0)
            time.sleep(0.1)
            print ("->")

        if Char==ord('s'):
           # close gripper arm
            print ("v")

        if Char==ord('w'):
            # open gripper arm
            print ("^")

        #if Char == curses.KEY_UP:
            #pi.set_servo_pulsewidth(18, 1600)
         #   print ("telescope up")

        #if Char==curses.KEY_DOWN:
            #pi.set_servo_pulsewidth(18, 1400)
            #print ("telescope Down")

        # exit the progam gracefully.
        # move the servo back to its initial position.
        if Char==ord('x'):
            print("xoxo")
            servoBase.ChangeDutyCycle(2);
            time.sleep(0.5)
            break


GPIO.cleanup()
curses.nocbreak();
screen.keypad(0);
curses.echo()
curses.endwin()
