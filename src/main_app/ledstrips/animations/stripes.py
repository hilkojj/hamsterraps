import time
from rpi_ws281x import *
import random

def get_random_color_RGB():
  PALETTE = [
    [255, 119, 0],
    [255, 0, 111],
    [0, 115, 255],
    [111, 0, 255],
    [251, 0, 255],
    [255, 251, 0],
    [115, 255, 0],
    [0, 255, 174],
    [255, 170, 0],
    [255, 25, 0],
    [0, 0, 0],
    [242, 0, 255],
    [0, 255, 30],
    [252, 215, 3],
    [173, 102, 255],
    [255, 0, 0],
  ]
  return random.choice(PALETTE)

SQUARES = 4
LEDS_PER_SQUARE = 11

def color_to_RGB(color):
  return [color >> 16 & 0xff,
          color >> 8  & 0xff,
          color       & 0xff]

def RGB_to_color(rgb):
  return Color(rgb[0], rgb[1], rgb[2])

def interpolate_rgb(old, new, progress):
  return [int(old[i] * (1. - progress) + new[i] * progress) for i in range(3)]

def stripes(strips, iterations=10):

  for _ in range(iterations):
    time.sleep(2)
    horizontal = True #random.random() > .5
    colrow = random.randint(0, 3)
    print("colrow", colrow)

    new_RGB = get_random_color_RGB()

    for sq in range(SQUARES):
      print("sq", sq)

      strip = strips[colrow] if horizontal else strips[sq]
      print("strip", strip)

      led_index = sq * LEDS_PER_SQUARE if horizontal else colrow * LEDS_PER_SQUARE
      print("led_index", led_index)

      current_color = strip.getPixelColor(led_index)
      current_RGB = color_to_RGB(current_color)

      steps = 100
      for step in range(steps):
        progress = step / steps
        stepped_RGB = interpolate_rgb(current_RGB, new_RGB, progress)
        stepped_color = RGB_to_color(stepped_RGB)
        for led in range(LEDS_PER_SQUARE):
          strip.setPixelColor(led_index + led, stepped_color)
        strip.show()


