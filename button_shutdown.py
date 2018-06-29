from gpiozero import Button
from subprocess import check_call
from signal import pause
import time

def shutdown():
    print('The system is shutting down...')
    time.sleep(2)
    check_call(['sudo', 'poweroff'])

def showInformation():
    print('This device uses the safety shutdown...')
    print('Press the button 3 seconds to shut down...')
    print('')

def main():
    shutdown_btn = Button(17, hold_time=3) # pin number is in BCM && physical pin = 11

    shutdown_btn.when_pressed = showInformation

    shutdown_btn.when_held = shutdown 

    pause()

if __name__ == '__main__':
    main()
