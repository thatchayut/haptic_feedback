from gpiozero import Button
from subprocess import check_call
from signal import pause
import time
import RPi.GPIO as GPIO

pin_out_BCM23 = 23 # BCM23 physical pin = 16 connected with RED LED

def shutdown():
    print('The system is shutting down...')
    count = 0
    while (count < 3):
    	GPIO.output(pin_out_BCM23, GPIO.LOW)
	time.sleep(0.3)
	GPIO.output(pin_out_BCM23, GPIO.HIGH)
        time.sleep(0.3)
	count += 1
    check_call(['sudo', 'poweroff'])

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_out_BCM23, GPIO.OUT)

    shutdown_btn = Button(17, hold_time=3) # pin number is in BCM && physical pin = 11

    shutdown_btn.when_held = shutdown 

    pause()

if __name__ == '__main__':
    main()
