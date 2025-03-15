import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
    
    def get_distance(self):
        # Send a 10 microsecond pulse.
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)
        
        # Wait for the echo start.
        start_time = time.time()
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()
        
        # Wait for the echo end.
        stop_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()
            
        # Calculate the distance (speed of sound is ~34300 cm/s).
        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2
        return distance
