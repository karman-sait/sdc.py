try:
    import pigpio
except ImportError:
    pigpio = None

class IRReceiver:
    def __init__(self, pin):
        self.pin = pin
        if pigpio:
            self.pi = pigpio.pi()
            self.pi.set_mode(self.pin, pigpio.INPUT)
        else:
            self.pi = None
            print("pigpio library not available; IR functionality will be simulated.")
    
    def read_signal(self):
        if self.pi:
            return self.pi.read(self.pin)
        else:
            # Return 0 (no signal) as dummy behavior.
            return 0
