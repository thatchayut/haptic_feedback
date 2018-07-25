# haptic_feedback

1. COMPILE
# manual compile
	 g++ -O3 -Wall -I/usr/local/include -Winline -pipe -L/usr/local/lib haptic_feedback.cpp  -lwiringPi -lwiringPiDev -lpthread -lm -lcrypt -lrt -o haptic_feedback
# use MAKE
	make

2. EXECUTE
	./haptic_feedback