import time

class ApplicationFunctionSet:
    def __init__(self, devices):
        self.devices = devices
        
    def run(self):
        # Example behavior:
        # 1. Read ultrasonic sensor for obstacle detection.
        distance = self.devices.ultrasonic.get_distance()
        print(f"Distance: {distance:.2f} cm")
        
        # 2. Simple obstacle avoidance:
        #    If an obstacle is closer than 20 cm, stop; otherwise, move forward.
        if distance < 20:
            print("Obstacle detected! Stopping.")
            self.stop()
            # Set LED to red to indicate obstacle
            self.devices.rgb_led.set_color(0, (255, 0, 0))
        else:
            print("Path is clear. Moving forward.")
            self.move_forward()
            # Set LED to green to indicate clear path
            self.devices.rgb_led.set_color(0, (0, 255, 0))
            
        # 3. Read MPU6050 data (for debugging/monitoring)
        mpu_data = self.devices.mpu6050.get_accel_gyro()
        print(f"MPU6050 Data: {mpu_data}")
        
        # 4. Check for IR remote signal (example)
        if self.devices.ir_receiver.read_signal():
            print("IR Signal detected! Executing command.")
            # Here you could implement different actions based on IR commands
            
    def move_forward(self, speed=70):
        self.devices.left_motor.move_forward(speed)
        self.devices.right_motor.move_forward(speed)
        
    def move_backward(self, speed=70):
        self.devices.left_motor.move_backward(speed)
        self.devices.right_motor.move_backward(speed)
        
    def stop(self):
        self.devices.left_motor.stop()
        self.devices.right_motor.stop()
