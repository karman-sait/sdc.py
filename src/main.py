#!/usr/bin/env python3
import time
from application_function_set import ApplicationFunctionSet
from device_driver_set import DeviceDriverSet

def main():
    print("Starting ELEGOO Smart Robot Car in Python...")
    
    # Initialize device drivers (motors, sensors, etc.)
    devices = DeviceDriverSet()
    # Initialize the high-level application logic with the devices
    app = ApplicationFunctionSet(devices)
    
    try:
        while True:
            app.run()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Stopping robot car...")
        devices.cleanup()

if __name__ == "__main__":
    main()
