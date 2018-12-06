"""
Driver for the TCA9548A I2C Multiplexer.
Based on Adafruit_CircuitPython_TCA9548A: https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A

Fixed to work with MicroPython
"""

from machine import I2C


class TCA9548AChannel:
    """Helper class to represent an output channel on the TCA9548A and take care
       of the necessary I2C commands for channel switching. This class needs to
       behave like an I2CDevice."""

    def __init__(self, tca, channel):
        self.tca = tca
        self.channel_switch = bytes([1 << channel])

    def _switch(self):
        if bytes(self.tca.i2c.readfrom(self.tca.address, 1)) != self.channel_switch:
            self.tca.i2c.writeto(self.tca.address, self.channel_switch)

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            getattr(self.tca.i2c, name)(*args, **kwargs)

        return wrapper

    def readfrom_into(self, address, buffer, **kwargs):
        """Pass thru for readfrom_into."""
        if address == self.tca.address:
            raise ValueError("Device address must be different than TCA9548A address.")
        self._switch()
        return self.tca.i2c.readfrom_into(address, buffer, **kwargs)

    def writeto(self, address, buffer, **kwargs):
        """Pass thru for writeto."""
        if address == self.tca.address:
            raise ValueError("Device address must be different than TCA9548A address.")
        self._switch()
        return self.tca.i2c.writeto(address, buffer, **kwargs)


class TCA9548A:
    """Class which provides interface to TCA9548A I2C multiplexer."""

    def __init__(self, i2c: I2C, address=0x70):
        self.i2c = i2c
        self.address = address
        self.channels = [None]*8

    def __len__(self):
        return 8

    def __getitem__(self, key: int):
        if not 0 <= key <= 7:
            raise IndexError("Channel must be an integer in the range: 0-7")
        if self.channels[key] is None:
            self.channels[key] = TCA9548AChannel(self, key)
        return self.channels[key]
