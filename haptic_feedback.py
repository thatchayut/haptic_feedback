import RPi.GPIO as GPIO
#import RPi.GPIO.PWM as PWM
import time

# define pins
pin_out_BCM_4 = 7 # physical pin = 7
pin_out_PWM = 18 # BCM18 physical pin = 12


def initializePins():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # using BCM numbering
    GPIO.setup(pin_out_BCM_4, GPIO.OUT)
    GPIO.setup(pin_out_PWM, GPIO.OUT)
    print('Pins are completely setup...')
    print('')


# 3 modes of vibrations 
# This motor limits at 16,000RPM (~266HZ)
# Duty cycle : range 0 - 100 is allowed
def minVibration(vibration_motor):
    print('MINIMUM vibration...')
    print('')
    vibration_motor.ChangeFrequency(50)
    vibration_motor.ChangeDutyCycle(10)

def medVibration(vibration_motor):
    print('MEDIUM vibration...')
    print('')
    vibration_motor.ChangeFrequency(260)
    vibration_motor.ChangeDutyCycle(30)

def maxVibration(vibration_motor):
    print('MAXIMUM vibration...')
    print('')
    vibration_motor.ChangeFrequency(260)
    vibration_motor.ChangeDutyCycle(100)


def main():
    initializePins()
    #setupPWM()

    vibration_motor_1 = GPIO.PWM(pin_out_PWM, 260) #initialize with freq. 5 Hz
    vibration_motor_1.start(0) #start vibration with 0% duty cycle (NO VIBRATION)
    time.sleep(2)

    while(True):
        print('Loop is accessible...')
	print('')
       # vibration_motor_1.ChangeDutyCycle(100)
       # vibration_motor_1.ChangeDutyCycle(90)
       # time.sleep(1)
       # vibration_motor_1.ChangeDutyCycle(50)
       # time.sleep(1)
       # vibration_motor_1.ChangeDutyCycle(100)
       # time.sleep(1)
       # vibration_motor_1.ChangeFrequency(100000)
        minVibration(vibration_motor_1)
        time.sleep(2)
        medVibration(vibration_motor_1)
        time.sleep(2)
        maxVibration(vibration_motor_1)
        time.sleep(2)
        
    #clean up when program is end
    vibration_motor_1.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':
    main()
