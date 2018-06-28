import RPi.GPIO as GPIO
#import RPi.GPIO.PWM as PWM
import time
import socket

# define pins
pin_out_BCM_4 = 7 # physical pin = 7
pin_out_PWM = 18 # BCM18 physical pin = 12

# define host and port number
host = '' # all available interfaces
port = 54345 # arbitrary port


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

def noVibration(vibration_motor):
    print('NO vibration...')
    print('')
    vibration_motor.ChangeFrequency(50)
    vibration_motor.ChangeDutyCycle(0)

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

def testVibrationLevel(vibration_motor):
    print('Loop is accessible...')
    print('')
    noVibration(vibration_motor)
    time.sleep(2)
    minVibration(vibration_motor)
    time.sleep(2)
    medVibration(vibration_motor)
    time.sleep(2)
    maxVibration(vibration_motor)
    time.sleep(2)

def testCommandViaWIFI(data, addr, vibration_motor):
    print('Loop is accessible...')
    print('')
    print('Received data: ')
    print(data)
    print('')      
    if(data == "on"):
        maxVibration(vibration_motor)
    elif(data == "off"):
        noVibration(vibration_motor)    


def main():
    initializePins()

    #socket section
    print('Establishing connection...')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 54345)) # host and port number are defined above

    # setup PWM
    vibration_motor_1 = GPIO.PWM(pin_out_PWM, 260) # initialize with freq. 260 Hz (Near maximum)
    vibration_motor_1.start(0) # start vibration with 0% duty cycle (NO VIBRATION)
    print('Motor is completely setup...')
    print('')
    time.sleep(2)

    while(True):
        print('Loop is accessible...')
        print('')
        data, addr = sock.recvfrom(1024)
        #testVibrationLevel(vibration_motor_1)
	    if not data:
            print('NO DATA')
            print('')
	    else:
            print('Connected by : ', addr)
            print('')
        	testCommandViaWIFI(data, addr, vibration_motor1)

    #clean up when program is end
    #conn.close()
    vibration_motor_1.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':
    main()
