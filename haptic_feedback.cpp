#include <iostream>
// #include <wiringPi.h>
// #include</mnt/c/Users/totay/Desktop/LinuxEnvironment/wiringPi-8d188fa/wiringPi/wiringPi.h> //for WINDOWS
//#include</home/raspberrypi3/Desktop/wiringPi-8d188fa/wiringPi/wiringPi.h> //for LINUX (Ubuntu)
#include <wiringPi.h>

#define pin_out_GPIO_7 7 //physical pin = 7
#define pin_out_PWM 1 //physical pin = 12

using namespace std;

void initializeWiringPi()
{
	wiringPiSetup();
	cout << "Wiring Pi is completely setup...";
	delay(1000);
}

void initializePins()
{
 	pinMode(pin_out_GPIO_7, OUTPUT);
	pinMode(pin_out_PWM, PWM_OUTPUT);
	cout << "\nPins are completely setup...";
	delay(1000);
}

void testDigitalWrite()
{
    digitalWrite(pin_out_GPIO_7, LOW); //L298N module is active LOW
    delay(1000);
    digitalWrite(pin_out_GPIO_7, HIGH);
    delay(1000);
}

void testDecreaseVibrationLevel()
{
	for (int vibration_level = 1023; vibration_level >= 100; vibration_level --)
		{
            //range PWM : 0-1023 
	        //preferred range of vibration level : 100-1023
			cout << vibration_level << endl;
			pwmWrite(pin_out_PWM, vibration_level);
			delay(5);
		}
	pwmWrite(pin_out_PWM, 0);
	delay(2000); 
}

void testIncreaseVibrationLevel()
{
	for (int vibration_level = 100; vibration_level <= 1023; vibration_level ++)
		{
            //range PWM : 0-1023 
	        //preferred range of vibration level : 100-1023
			cout << vibration_level << endl;
			pwmWrite(pin_out_PWM, vibration_level);
			delay(5);
		}
	pwmWrite(pin_out_PWM, 0);
	delay(2000); 
}

int main(void)
{
    initializeWiringPi();
    initializePins();

    //test vibration motor
    while(true)
    {
        cout << "\nLoop is accessible\n";
	    //testDecreaseVibrationLevel();
	    testIncreaseVibrationLevel();
    }
    
    return 0;
}
