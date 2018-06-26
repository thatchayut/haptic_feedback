#include <iostream>
// #include <wiringPi.h>
// #include</mnt/c/Users/totay/Desktop/LinuxEnvironment/wiringPi-8d188fa/wiringPi/wiringPi.h> //for WINDOWS
//#include</home/raspberrypi3/Desktop/wiringPi-8d188fa/wiringPi/wiringPi.h> //for LINUX (Ubuntu)
#include <wiringPi.h>

#define pin_out_GPIO_7 7 //physical pin = 7
#define pin_out_GPIO_21 21 //physical pin = 29

using namespace std;

int main(void)
{
    //check if the wiring pi is completely set up
    cout << "testttttttttttttttttttttttt";
    wiringPiSetup();
    cout << "\nwiring Pi is completely set up...";
    delay(200);
    //define pin mode
    pinMode(pin_out_GPIO_7, OUTPUT); 
    pinMode(pin_out_GPIO_21, OUTPUT);
    cout << "\npins are completely setup...";
    delay(200);
    //turn on the light 
    while(true)
    {
        cout << "\nLoop is accessible";
        //digitalWrite(pin_out_GPIO_7, LOW);
        digitalWrite(pin_out_GPIO_21, LOW);
        delay(1000);
	//digitalWrite(pin_out_GPIO_7, HIGH);
	digitalWrite(pin_out_GPIO_21, HIGH);
	delay(1000);
    }
    
    cout << "\nProgram is terminated";
    return 0;
}
