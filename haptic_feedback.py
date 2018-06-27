import RPi.GPIO as GPIO
import RPi.PWM as PWM
import time

#define pins
pin_out_BCM_4 = 7 #physical pin = 7
pin_out_PWM = 18 #BCM18 physical pin = 12

def initializePins():
    GPIO.setmode(GPIO.BCM)  #using BCM numbering
    GPIO.setup(pin_out_BCM_4, GPIO.OUT)
    GPIO.setup(pin_out_PWM, GPIO.OUT)
    print('Pins are completely setup...')
    print()

def setupPWM():
    vibration_motor_1 = PWM(pin_out_PWM, 0) #initialize with freq. 0 Hz

def main():
    initializePins()
    while(True):
        vibration_motor_1.ChangeDutyCycle(10)
        time.sleep(1)
        vibration_motor_1.ChangeDutyCycle(50)
        time.sleep(1)
        vibration_motor_1.ChangeDutyCycle(100)
        time.sleep(1)
        
    #clean up when program is end
    vibration_motor_1.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':
    main()