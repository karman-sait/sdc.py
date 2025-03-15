import smbus

class I2CDev:
    def __init__(self, bus_num=1):
        self.bus = smbus.SMBus(bus_num)
    
    def read_byte(self, address, reg):
        return self.bus.read_byte_data(address, reg)
    
    def write_byte(self, address, reg, value):
        self.bus.write_byte_data(address, reg, value)
