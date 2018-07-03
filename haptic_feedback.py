import RPi.GPIO as GPIO
#import RPi.GPIO.PWM as PWM
import time
import socket

# define pins
pin_out_BCM_4 = 4 # physical pin = 7
pin_out_PWM = 18 # BCM18 physical pin = 12
pin_out_BCM_23 = 23 # BCM23 physical pin = 16 connected with RED LED
pin_out_BCM_24 = 24 # BCM24 physical pin = 18 connected with GREEN LED

# define host and port number
host = "10.232.160.40" # Raspberrypi3 IP address
port = 12345 # arbitrary port
size = 1024
backlog = 1


def initializePins():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # using BCM numbering
    GPIO.setup(pin_out_BCM_4, GPIO.OUT)
    GPIO.setup(pin_out_PWM, GPIO.OUT)
    GPIO.setup(pin_out_BCM_23, GPIO.OUT)
    GPIO.setup(pin_out_BCM_24, GPIO.OUT)
    print('')
    print('Pins are completely setup...')
    print('')


# 4 modes of vibration
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
   # print('Loop is accessible...')
   # print('')
   # print('Received data: ')
   # print(data)
    print('')      
    if(data == "on"):
        maxVibration(vibration_motor)
	print(data)
    elif(data == "off"):
        noVibration(vibration_motor)
	print(data)

def commandVibrationViaWIFI(data, addr, vibration_motor):
    #print('Loop is accessible...')
    #print('')
    #print('Received data: ')
    #print(data)
    #print('')      
    if(data == "min"):
        minVibration(vibration_motor)
	print(data)
    elif(data == "med"):
        medVibration(vibration_motor)
	print(data)    
    elif(data == "max"):
        maxVibration(vibration_motor)
	print(data)


def main():  
    initializePins()

    # the red LED shows that the device is ON
    GPIO.output(pin_out_BCM_23, GPIO.HIGH)

    # setup PWM
    vibration_motor_1 = GPIO.PWM(pin_out_PWM, 260) # initialize with freq. 260 Hz (Near maximum)
    vibration_motor_1.start(0) # start vibration with 0% duty cycle (NO VIBRATION)
    print('Motor is completely setup...')
    print('')
    time.sleep(2)

    #socket section
    print('Establish connection...')
    print('')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # use TCP protocol 
    sock.bind((host, port)) # host and port number are defined above
    sock.listen(backlog)
    sock.settimeout(5) # 10 seconds

    #print('Wating for connection...')
    #print('')
    #conn, addr = sock.accept()
    #print('Connected by : ', addr)
    #print('')
    #The green LED shows that the connection is established
    #GPIO.output(pin_out_BCM_24, GPIO.HIGH)

    while(True):
	try:
		#sock.connect((host, port))
		conn, addr = sock.accept()
		print('Connected by: ', addr)
		GPIO.output(pin_out_BCM_24, GPIO.HIGH)
        	data = conn.recv(size)
        	print(data)
        	print('')
        	#testVibrationLevel(vibration_motor_1)
        	#testCommandViaWIFI(data, addr, vibration_motor_1)
        	commandVibrationViaWIFI(data, addr, vibration_motor_1)
	except socket.error, message:
		print("Caught exception socket.error: %s" % message)
		print('Wating for connection...')
		noVibration(vibration_motor_1)
		GPIO.output(pin_out_BCM_24, GPIO.LOW)
                
    print('closing socket...')
    print('')

    #clean up when program is end
    conn.close()
    socket.close()
    GPIO.output(pin_out_BCM_24, GPIO.LOW)
    vibration_motor_1.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':
    main()
