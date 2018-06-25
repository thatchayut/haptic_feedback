#include <iostream>
// #include <wiringPi.h>
// #include</mnt/c/Users/totay/Desktop/LinuxEnvironment/wiringPi-8d188fa/wiringPi/wiringPi.h> //for WINDOWS
//#include</home/raspberrypi3/Desktop/wiringPi-8d188fa/wiringPi/wiringPi.h> //for LINUX (Ubuntu)
#include <wiringPi.h>

#define pin_out_GPIO_22 7 //physical pin = 31
#define pin_out_GPIO_23 21 //physical pin = 33

using namespace std;

int main(void)
{
    //check if the wiring pi is completely set up
    cout << "testttttttttttttttttttttttt";
    wiringPiSetup();
    cout << "\nwiring Pi is completely set up...";
    delay(200);
    //define pin mode
    pinMode(pin_out_GPIO_22, OUTPUT); 
    pinMode(pin_out_GPIO_23, OUTPUT);
    cout << "\npins are completely setup...";
    delay(200);
    //turn on the light 
    while(true)
    {
        cout << "\nLoop is accessible";
        digitalWrite(pin_out_GPIO_22, LOW);
        digitalWrite(pin_out_GPIO_23, HIGH);
        delay(200);
    }
    
    cout << "\nProgram is terminated";
    return 0;
}
