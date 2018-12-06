Introduction
============

MicroPython driver for the TCA9548A I2C Multiplexer based on Adafruit CircuitPython TCA9548A.

Usage Example
=============

.. code-block :: python

    # This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
    # Use with other I2C sensors would be similar.
    from machine import Pin, I2C
    import tca9548a
    from ssd1306 import SSD1306_I2C

    # Create I2C bus as normal
    i2c = I2C(Pin(25), Pin(26))

    # Create the TCA9548A object and give it the I2C bus
    tca = TCA9548A(i2c)

    # For each sensor, create it using the TCA9548A channel instead of the I2C object
    oled1 = SSD1306_I2C(tca[0])
    oled2 = SSD1306_I2C(tca[1])

    oled1.text("HELLO", 0, 0)
    oled2.text("WORLD", 0, 0)

    oled1.show()
    oled2.show()

