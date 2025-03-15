try:
    import board
    import neopixel
except ImportError:
    board = None
    neopixel = None

class RGBLED:
    def __init__(self, pin, num_leds):
        self.num_leds = num_leds
        if neopixel and board:
            # Here we assume the pin provided corresponds to board.D18.
            self.pixels = neopixel.NeoPixel(board.D18, num_leds, auto_write=True)
        else:
            # Fallback dummy implementation for testing.
            self.pixels = [(0, 0, 0)] * num_leds
            print("neopixel library not found; using dummy LED output.")
    
    def set_color(self, index, color):
        if 0 <= index < self.num_leds:
            self.pixels[index] = color
            print(f"LED {index} set to {color}")
    
    def clear(self):
        if hasattr(self.pixels, "fill"):
            self.pixels.fill((0, 0, 0))
        else:
            self.pixels = [(0, 0, 0)] * self.num_leds
