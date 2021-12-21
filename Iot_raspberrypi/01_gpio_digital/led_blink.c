#include <wiringPi.h>
#include <stdio.h>
#define LED 4

int main (void)
{
  //wiringPiSetup () ; //physical pin번호로 할때
  wiringPiSetupGpio(); //bcm pin번호로 할때
  pinMode (LED, OUTPUT) ;
  for (int i=1;i<11;i++)
  {
    digitalWrite (LED, HIGH) ; delay (50*i) ;
    printf("led on\n");
    digitalWrite (LED,  LOW) ; delay (50*i) ;
    printf("led off\n");
  }
  return 0 ; 
}