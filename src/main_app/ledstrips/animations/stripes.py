import time
from rpi_ws281x import *
import random
from .. import controller as c

PALETTE = [
  [255, 119, 0],
  [255, 0, 111],
  [0, 115, 255],
  [111, 0, 255],

  [255, 0, 20],
  [255, 251, 0],
  [0, 68, 255],
  [0, 255, 174],

  [0, 106, 255],
  [255, 25, 0],
  [0, 0, 0],
  [0, 255, 42],

  [0, 255, 123],
  [247, 255, 5],
  [118, 0, 255],
  [255, 0, 0],
]

def get_random_color_RGB():
  global PALETTE
  return random.choice(PALETTE)

SQUARES = 4
LEDS_PER_SQUARE = 11

def show_palette(controller):
  for i in range(16):
    global PALETTE
    controller.set_range_color(int(i / 4), (i % 4) * 11, (i % 4) * 11 + 10, c.RGB_to_color(PALETTE[i]))
    
  controller.show()
  time.sleep(1)

def stripes(controller, iterations=30):

  # show_palette(controller)

  for _ in range(iterations):
    horizontal = random.random() > .5
    colrow = random.randint(0, 3)

    new_RGB = get_random_color_RGB()

    for sq in range(SQUARES):

      row = colrow if horizontal else sq

      led_index = sq * LEDS_PER_SQUARE if horizontal else colrow * LEDS_PER_SQUARE

      current_color = controller.get_color(row, led_index + 5)
      current_RGB = c.color_to_RGB(current_color)

      steps = 50
      for step in range(steps):
        progress = step / steps
        stepped_RGB = c.interpolate_rgb(current_RGB, new_RGB, progress)
        stepped_color = c.RGB_to_color(stepped_RGB)

        controller.set_range_color(row, led_index, led_index + LEDS_PER_SQUARE - 1, stepped_color)
        controller.show()
    time.sleep(.1)

