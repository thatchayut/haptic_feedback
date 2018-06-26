#include <iostream>
// #include <wiringPi.h>
// #include</mnt/c/Users/totay/Desktop/LinuxEnvironment/wiringPi-8d188fa/wiringPi/wiringPi.h> //for WINDOWS
//#include</home/raspberrypi3/Desktop/wiringPi-8d188fa/wiringPi/wiringPi.h> //for LINUX (Ubuntu)
#include <wiringPi.h>

#define pin_out_GPIO_7 7 //physical pin = 7
#define pin_out_PWM 1 //physical pin = 12

using namespace std;

int main(void)
{
    //check if the wiring pi is completely set up
    wiringPiSetup();
    cout << "\nwiring Pi is completely set up...";
    delay(200);

    //define pin mode
    pinMode(pin_out_GPIO_7, OUTPUT);
    pinMode(pin_out_PWM, PWM_OUTPUT);
    cout << "\npins are completely setup...";
    delay(200);

    //test vibration motor

    while(true)
    {
        cout << "\nLoop is accessible";
        // digitalWrite(pin_out_GPIO_7, LOW); //L298N module is active LOW
        // delay(1000);
        // digitalWrite(pin_out_GPIO_7, HIGH);
        // delay(1000);
       // for (int vibration_level = 0; vibration_level < 1023; vibration_level++)
        //{
           pwmWrite(pin_out_PWM, 300); //THIS VALUE (700) IS WORKED!!!!
	 //cout << vibration_level;
	 //pwmWrite(pin_out_PWM, vibration_level);
	 //delay(500);
       // }
       // pwmWrite(pin_out_PWM, 1023);
        delay(2000);
    }
    
    cout << "\nProgram is terminated";
    return 0;
}
