# PropellerPi

## Description

This project is about facilitating communication between the [Propeller microcontroller](https://www.parallax.com/microcontrollers/propeller) and the Raspberry Pi. The general idea behind this is to take advantage of the Propeller's parallel processing capabilities to handle the transfer of information from one computer to another. 

We approached this project by analyzing the Propeller's architecture and the Propeller C language. We initially wanted to communicate over Serial Peripheral Interface (SPI), but we had trouble because we couldn't assign one device to be the slave. 

We did get communication working using I2C. We were able to send values from the propeller to the Pi.

## Next Steps
To make communication work, we would have to script a method for the propeller to notify the Pi that's responsible for receiving the computed results. That way, we can have two-way communication between the Propeller and the Pi.

To make SPI feasible, We would have to write some low-level code to make the Propeller take on the slave role.

## Instructions
Run this command in the Raspberry Pi terminal:
> sudo pigpiod
You should also [make sure the Raspberry Pi has I2C enabled](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial#i2c-on-pi). 

Next:
Open the i2c_test.c in the SimpleIDE. Run the program in that IDE. 
Then run the getsignal_I2C.py program in the Pi terminal:
> python getsignal_I2C.py

You should obtain the second input in the i2c_out() method in the i2c_test() function. 

## Further Notes
Make sure the Propeller and Raspberry Pi are grounded
Make sure you use GPIO Pins 18 and 19 in the Raspberry Pi