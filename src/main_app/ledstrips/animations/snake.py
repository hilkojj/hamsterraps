import time
from rpi_ws281x import *
import random
from .. import controller as c

PALETTE = [
  [255, 119, 0],
  [255, 0, 111],
  [0, 115, 255],
  [111, 0, 255]
]

def get_random_color_RGB():
  global PALETTE
  return random.choice(PALETTE)

ROWS = 4
SQUARES = 4
LEDS_PER_SQUARE = 11

def fade_out_each_square(controller, step_size=0.01, to=[0, 0, 0]):
  for row in range(ROWS):
    for sq in range(SQUARES):
      current_color = controller.get_color(row, sq * LEDS_PER_SQUARE + 5)
      current_RGB = c.color_to_RGB(current_color)
      faded_RGB = c.interpolate_rgb(current_RGB, to, step_size)
      controller.set_range_color(row, sq * 11, sq * 11 + 10, Color(faded_RGB[0], faded_RGB[1], faded_RGB[2]))


def snake(controller, wait_ms=15, iterations=5):
  
  order = [(2, 2), (1, 2), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)]

  for _ in range(iterations):
    
    color = get_random_color_RGB()

    for sq in order:
      steps = 20
      for step in range(steps):

        fade_out_each_square(controller)

        progress = step / steps
        current_color = controller.get_color(sq[1], sq[0] * LEDS_PER_SQUARE + 5)
        current_RGB = c.color_to_RGB(current_color)
        faded_RGB = c.interpolate_rgb(current_RGB, color, progress)
        controller.set_range_color(sq[1], sq[0] * 11, sq[0] * 11 + 10, Color(faded_RGB[0], faded_RGB[1], faded_RGB[2]))

        controller.show()
        time.sleep(wait_ms / 1000.0)

    

