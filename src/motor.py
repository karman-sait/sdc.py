import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pin1, pin2, enable):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable = enable
        
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.enable, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.enable, 1000)  # 1kHz frequency
        self.pwm.start(0)
    
    def move_forward(self, speed=50):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)
    
    def move_backward(self, speed=50):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
    
    def stop(self):
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
