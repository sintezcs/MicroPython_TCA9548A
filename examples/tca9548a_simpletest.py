# This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
# Use with other I2C sensors would be similar.
import time
from tca9548a import TCA9548A
from ssd1306 import SSD1306_I2C
from machine import Pin

# Create I2C bus as normal
i2c = I2C(sda=Pin(12), scl=Pin(11))

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# For each sensor, create it using the TCA9548A channel instead of the I2C object
tsl1 = adafruit_tsl2591.TSL2591(tca[0])
tsl2 = adafruit_tsl2591.TSL2591(tca[1])

# After initial setup, can just use sensors as normal.
while True:
    print(tsl1.lux, tsl2.lux)
    time.sleep(0.1)
