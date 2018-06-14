#include <iostream>
#include <wiringPi.h>

#define pin_out_GPIO0 0

using namespace std;

int main(void)
{
    //check if the wiring pi is completely set up
    // if (wiringPiSetup() == -1)
    // {
    //     return 1;
    // }
    wiringPiSetup();
    cout << "wiring Pi is completely set up...";
    delay(200);
    //define pin mode
    pinMode(pin_out_GPIO0,OUTPUT); //set GPIO 0 (pin11) as an output
    cout << "pins are completely setup...";
    delay(200);
    //turn on the light 
    while(true)
    {
        digitalWrite(pin_out_GPIO0,HIGH);
    }

    return 0;
}