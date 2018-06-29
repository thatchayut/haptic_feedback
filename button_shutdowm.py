from gpiozero import Button
from subprocess import check_call
from signal import pause
import time

def shutdown():
    print('')
    print('The system is shutting down...')
    print('')
    time.sleep(2)
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(17, hold_time=3)
shutdown_btn.when_held = shutdown

pause()