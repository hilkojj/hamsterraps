import time
from rpi_ws281x import *

def wheel(pos):
  """Generate rainbow colors across 0-255 positions."""
  if pos < 85:
    return Color(pos * 3, 255 - pos * 3, 0)
  elif pos < 170:
    pos -= 85
    return Color(255 - pos * 3, 0, pos * 3)
  else:
    pos -= 170
    return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strips, wait_ms=20, iterations=10):
  """Draw rainbow that fades across all pixels at once."""
  for j in range(256 * iterations):
    strip_i = 0
    # strip = strips[0]
    for strip in strips:
      for i in range(strip.numPixels()):
        strip.setPixelColor(i, wheel((i + j) & 255))
      strip.show()
      strip_i += 1
    ##
    time.sleep(wait_ms / 1000.0)
