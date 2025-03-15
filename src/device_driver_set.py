import sys
import os

# Ensure GPIO uses the correct mode
if sys.platform != "win32":
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
else:
    # On Windows, our mocks will print messages instead of controlling hardware.
    pass

from motor import Motor
from ultrasonic_sensor import UltrasonicSensor
from mpu6050 import MPU6050
from rgb_led import RGBLED
from ir_remote import IRReceiver

class DeviceDriverSet:
    def __init__(self):
        # Initialize two motors (left and right)
        self.left_motor = Motor(pin1=17, pin2=27, enable=22)
        self.right_motor = Motor(pin1=23, pin2=24, enable=25)
        
        # Initialize ultrasonic sensor (front sensor)
        self.ultrasonic = UltrasonicSensor(trig_pin=5, echo_pin=6)
        
        # Initialize MPU6050 sensor for accelerometer/gyroscope data
        self.mpu6050 = MPU6050()
        
        # Initialize an RGB LED strip (assume 8 LEDs on pin 18)
        self.rgb_led = RGBLED(pin=18, num_leds=8)
        
        # Initialize IR receiver on GPIO pin 12
        self.ir_receiver = IRReceiver(pin=12)
        
    def cleanup(self):
        try:
            import RPi.GPIO as GPIO
            GPIO.cleanup()
        except ImportError:
            print("[Mock] GPIO cleanup called")
