#include <wiringPi.h>
#include <stdio.h>
#define LED_r 4
#define LED_g 5
#define LED_y 6

int main (void)
{
  //wiringPiSetup () ; //physical pin번호로 할때
  wiringPiSetupGpio(); //bcm pin번호로 할때
  pinMode (LED_r, OUTPUT);
  pinMode (LED_g, OUTPUT);
  pinMode (LED_y, OUTPUT);
  
  digitalWrite (LED_r, HIGH);
  printf("led RED on\n");
  delay (2000);
  digitalWrite (LED_r,  LOW);
  digitalWrite (LED_g, HIGH);
  printf("led RED off and led GREEN on\n");
  delay (2000);
  digitalWrite (LED_g,  LOW);
  digitalWrite (LED_y, HIGH);
  printf("led GREEN off and led YELLOW on\n");
  delay (2000);
  digitalWrite (LED_y, LOW);
  printf("led YELLOW off\n");
  
  pinMode (LED_r, INPUT);
  pinMode (LED_g, INPUT);
  pinMode (LED_y, INPUT);
  
  return 0 ; 
}