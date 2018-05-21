/*
  Blank Simple Project.c
  http://learn.parallax.com/propeller-c-tutorials 
*/
#include "simpletools.h"                      // Include simple tools

i2c *mainBus;
int cogNum = NULL;

void i2c_test()
{
  int SDAPin = 14;
  int SCLPin = 15;
  
  mainBus = i2c_newbus(SCLPin,SDAPin,0);
  
  char test[1] = {5};
  while(1 == 1){
    i2c_out(mainBus, 0xFF , NULL, 0,test, 1);
    pause(200);
  } 
}  

int main()                                    // Main function
{
  // Add startup code here.
 int cogInfo;
 int stackSize = 40;
 cogInfo = cog_run(i2c_test(), stackSize);
 cogNum = cog_num(cogInfo);

}


