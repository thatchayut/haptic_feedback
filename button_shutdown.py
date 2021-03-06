from gpiozero import Button
from subprocess import check_call
from signal import pause
import time
import RPi.GPIO as GPIO

pin_out_BCM_23 = 23 # BCM23 physical pin = 16 connected to RED LED
pin_out_BCM_24 = 24 # BCM24 physical pin = 18 connected to GREEN LED
pin_out_BCM_27 = 27 # BCM27 physical pin = 13 connected to WHITE LED

def onLED(pin):
    GPIO.output(pin, GPIO.HIGH)

def offLED(pin):
    GPIO.output(pin, GPIO.LOW)

def blink():
    count = 0
    offLED(pin_out_BCM_23)
    offLED(pin_out_BCM_24)
    offLED(pin_out_BCM_27)
    while(count < 3):
	onLED(pin_out_BCM_23)
	offLED(pin_out_BCM_24)
	offLED(pin_out_BCM_27)
	time.sleep(0.3)
	offLED(pin_out_BCM_23)
	onLED(pin_out_BCM_24)
	offLED(pin_out_BCM_27)
	time.sleep(0.3)
	offLED(pin_out_BCM_23)
	offLED(pin_out_BCM_24)
	onLED(pin_out_BCM_27)
	time.sleep(0.3)
	count += 1
    onLED(pin_out_BCM_23)
    offLED(pin_out_BCM_24)
    offLED(pin_out_BCM_27)

def shutdown():
    print('The system is shutting down...')
    #count = 0
    #while (count < 3):
    #	GPIO.output(pin_out_BCM_23, GPIO.LOW)
	#time.sleep(0.3)
	#GPIO.output(pin_out_BCM_23, GPIO.HIGH)
        #time.sleep(0.3)
	#count += 1
    blink()
    check_call(['sudo', 'poweroff'])

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_out_BCM_23, GPIO.OUT)
    GPIO.setup(pin_out_BCM_24, GPIO.OUT)
    GPIO.setup(pin_out_BCM_27, GPIO.OUT)

    shutdown_btn = Button(17, hold_time=3) # pin number is in BCM && physical pin = 11

    shutdown_btn.when_held = shutdown 

    pause()

if __name__ == '__main__':
    main()
