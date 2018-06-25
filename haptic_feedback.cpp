#include <iostream>
// #include <wiringPi.h>
// #include</mnt/c/Users/totay/Desktop/LinuxEnvironment/wiringPi-8d188fa/wiringPi/wiringPi.h> //for WINDOWS
//#include</home/raspberrypi3/Desktop/wiringPi-8d188fa/wiringPi/wiringPi.h> //for LINUX (Ubuntu)
#include <wiringPi.h>

#define pin_out_GPIO0 0 //on board = GPIO17

using namespace std;

int main(void)
{
    //check if the wiring pi is completely set up
    // if (wiringPiSetup() == -1)
    // {
    //     return 1;
    // }
    cout << "testttttttttttttttttttttttt";
    wiringPiSetup();
    cout << "\nwiring Pi is completely set up...";
    delay(200);
    //define pin mode
    pinMode(pin_out_GPIO0,OUTPUT); //set GPIO 0 (pin11) as an output
    cout << "\npins are completely setup...";
    delay(200);
    //turn on the light 
    while(true)
    {
	cout << "\nLoopn is accessible";
        digitalWrite(pin_out_GPIO0,HIGH);
    }
    
    cout << "\nProgram is terminated";
    return 0;
}
