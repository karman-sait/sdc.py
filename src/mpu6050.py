import smbus
import time

class MPU6050:
    def __init__(self, address=0x68, bus_num=1):
        self.address = address
        self.bus = smbus.SMBus(bus_num)
        # Wake up MPU6050 (exit sleep mode)
        self.bus.write_byte_data(self.address, 0x6B, 0)
    
    def read_raw_data(self, reg):
        # Read high and low bytes and combine them
        high = self.bus.read_byte_data(self.address, reg)
        low = self.bus.read_byte_data(self.address, reg + 1)
        value = (high << 8) | low
        if value > 32767:
            value -= 65536
        return value
    
    def get_accel_gyro(self):
        accel_x = self.read_raw_data(0x3B)
        accel_y = self.read_raw_data(0x3D)
        accel_z = self.read_raw_data(0x3F)
        gyro_x = self.read_raw_data(0x43)
        gyro_y = self.read_raw_data(0x45)
        gyro_z = self.read_raw_data(0x47)
        return {
            "accel_x": accel_x,
            "accel_y": accel_y,
            "accel_z": accel_z,
            "gyro_x": gyro_x,
            "gyro_y": gyro_y,
            "gyro_z": gyro_z
        }
