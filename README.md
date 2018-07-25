Haptic Feedback Device for a Realistic Experience of Grinder Accidents

This repository consists of 2 main parts.

1. haptic_feedback.py
This code is used to controlled the levels of vibration on the Raspberry Pi3. It uses the signal sent from PC via WIFI to control the levels of vibration.
The PWM (Pulse Width modulation) is used in this system to adjust vibration levels.

2. button_shutdown.py
This is used to safely poweroff the raspberry pi since it doesn't have any internal button. This is also used to control LEDs to show the status of the
Raspberry Pi.

These 2 files are included in rc.local to make the Raspberry Pi automatically executes them after it finishes booting. Moreover, these files should be 
run on background since the Raspberry Pi is not connected with any input devices.