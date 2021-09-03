import time
from rpi_ws281x import *
from .rainbow import *


def randbow(controller, wait_ms=20, iterations=10):
  
  for j in range(256 * iterations):
    for row in range(4):
      for sq in range(4):
        for i in range(11):
          controller.set_color(row, sq * 11 + i, wheel((i * 8 + j + (row * 938 + sq * 365)) & 255))
    controller.show()
    time.sleep(wait_ms / 1000.0)
