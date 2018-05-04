#!/usr/bin/env python

import time
import pigpio

I2C_ADDR=0xFF

def i2c(id, tick):
   global pi

   s, b, d = pi.bsc_i2c(I2C_ADDR)
   if b:
      print(int.from_bytes(d, byteorder='big'))
      #print(int(d[:-1]))
#def bytes_to_int(bytes):
#   result = 0
#   for b in bytes:
#	result = result * 256 + int(b)
#   return result

# pi = pigpio.pi('soft', 8888)
pi = pigpio.pi(port=8888)

if not pi.connected:
    print("!connected")
    exit()

pi.set_pull_up_down(18, pigpio.PUD_UP)
pi.set_pull_up_down(19, pigpio.PUD_UP)
# Respond to BSC slave activity

e = pi.event_callback(pigpio.EVENT_BSC, i2c)

pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave

time.sleep(600)

e.cancel()
print("cancelled")
pi.bsc_i2c(0) # Disable BSC peripheral

pi.stop()
