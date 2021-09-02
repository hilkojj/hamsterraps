import time
from rpi_ws281x import Color

def test(controller):

  for i in range(4):
    for j in range(4):
      if j == i:
        controller.set_range_color(i, 0, 43, Color(0, 0, 0))
        controller.set_color(i, 1, Color(255, 0, 0))
        controller.set_color(i, 11, Color(0, 255, 0))
        controller.set_color(i, 22, Color(0, 0, 255))
        controller.set_color(i, 33, Color(255, 255, 255))
      else:
        controller.set_range_color(j, 0, 10, Color(255, 0, 0))
        controller.set_range_color(j, 11, 21, Color(0, 255, 0))
        controller.set_range_color(j, 22, 32, Color(0, 0, 255))
        controller.set_range_color(j, 33, 43, Color(255, 255, 255))
    controller.show()
    time.sleep(2)
  controller.clear()

