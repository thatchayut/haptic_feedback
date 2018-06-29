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

print('')
print('Safety shutdown is activated')
print('')
print('Press the button 5 seconds to shut down...')
print('')
shutdown_btn = Button(17, hold_time=5) # pin number is in BCM && physical pin = 11
while True:
	#shutdown_btn.when_held = shutdown
	if shutdown_btn.is_pressed:
	print("button is pressed") 
#pause()
