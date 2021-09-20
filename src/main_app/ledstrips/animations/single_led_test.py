import time
from rpi_ws281x import Color

def single_led_test(controller):
  controller.override_cage_color = True
  controller.clear()
  controller.set_color(3, 1, Color(1, 0, 0))
  controller.show()
  time.sleep(.5)
  controller.clear()
  time.sleep(.5)
  controller.override_cage_color = False