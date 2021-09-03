import time
from rpi_ws281x import *
from .rainbow import *


def checkeredrainbow(controller, wait_ms=20, iterations=10):
  
  for j in range(256 * iterations):
    for row in range(4):
      for sq in range(4):
        for i in range(11):
          controller.set_color(row, i + sq * 11, wheel((i + j + sq * 11 + (0 if (row % 2 == 0 and (sq % 2 == 0)) or (row % 2 != 0 and (sq % 2 != 0)) else 128)) & 255))
    controller.show()
    time.sleep(wait_ms / 1000.0)
