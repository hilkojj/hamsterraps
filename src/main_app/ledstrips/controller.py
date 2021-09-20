import random
from rpi_ws281x import *
from .animations import rainbow, stripes, test, randbow, checkeredrainbow, snake, single_led_test

# LED strip configuration:
LED_COUNT = 11 * 8      # Number of LED pixels.

# https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/
# https://i.stack.imgur.com/gaU6t.png
LED_PIN_0 = 12          # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN_1 = 13

LED_FREQ_HZ = 800000    # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10            # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest


# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False

LED_CHANNEL_0 = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_CHANNEL_1 = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def color_to_RGB(color):
  return [color >> 16 & 0xff,
          color >> 8  & 0xff,
          color       & 0xff]

def RGB_to_color(rgb):
  return Color(rgb[0], rgb[1], rgb[2])

def interpolate_rgb(old, new, progress):
  return [int(old[i] * (1. - progress) + new[i] * progress) for i in range(3)]

"""
LEDS PER SQUARE
& index range

         ╔════════╦════════╦════════╦════════╗
         ║ 10     ║ 11     ║ 11     ║ 11     ║  ↰ DATA CONTINUES UP IN OPPOSITE DIRECTION (R→L)
         ║        ║        ║        ║        ║
         ║ 86..77 ║ 76..66 ║ 65..55 ║ 54..44 ║  row 3
         ╠════════╬════════╩════════╬════════╣
DATA 1 → ║ 11     ║ 11     │ 11     ║ 11     ║
         ║        ║        │        ║        ║
         ║ 0..10  ║ 11..21 │ 22..32 ║ 33..43 ║  row 2
         ╠════════╬════════╦════════╬════════╣
DATA 0 → ║ 11     ║ 11     ║ 11     ║ 9      ║
         ║        ║        ║        ║        ║
         ║ 0..10  ║ 11..21 ║ 22..32 ║ 33..41 ║  row 1
         ╠════════╬════════╬════════╬════════╣
         ║ 10     ║ 11     ║ 11     ║ 11     ║  ↲ DATA CONTINUES DOWN IN OPPOSITE DIRECTION (R→L)
         ║        ║        ║        ║        ║
         ║ 84..75 ║ 74..64 ║ 63..53 ║ 52..42 ║  row 0
         ╚════════╩════════╩════════╩════════╝

"""

CAGE_ROW = 2
CAGE_RANGE = range(11, 32)

class Controller:

  def __init__(self):
    # Create NeoPixel objects with appropriate configuration.
    self.datalines = [
      Adafruit_NeoPixel(
        LED_COUNT, LED_PIN_0, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL_0
      ),
      Adafruit_NeoPixel(
        LED_COUNT, LED_PIN_1, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL_1
      )
    ]

    i = 0
    for line in self.datalines:
      # Intialize the library (must be called once before other functions).
      print("Initializing LED-strip/dataline", i)
      line.begin()
      i += 1

    self.cage_color = Color(25, 15, 8)
    self.override_cage_color = False

  def row_i_to_dataline_i(self, row, i):
    """
    As seen in the table above, the indexes of LEDs on the two data lines is extremely confusing.
    
    Therefore animations should not bother trying to use indices on the data lines,
    instead they can locate a LED by row (0 - 3) and LED-index (0 - 43).

    This function will take that as input and return the right dataline and LED-index on the dataline.
    """

    dataline = 0 if row < 2 else 1
    dataline_i = -1
    
    if dataline == 0:
      if row == 1:
        dataline_i = i if i <= 41 else 41
      else:
        dataline_i = 85 - i
    else:
      if row == 2:
        dataline_i = i
      else:
        dataline_i = 87 - i

    return self.datalines[dataline], dataline_i

  def get_color(self, row, i):
    line, led = self.row_i_to_dataline_i(row, i)
    return line.getPixelColor(led)

  def set_color(self, row, i, color):
    line, led = self.row_i_to_dataline_i(row, i)
    line.setPixelColor(led, color)

  def set_range_color(self, row, i0, i1, color):
    line, led0 = self.row_i_to_dataline_i(row, i0)
    _,    led1 = self.row_i_to_dataline_i(row, i1)
    for led in range(min(led0, led1), max(led0, led1) + 1):
      line.setPixelColor(led, color)

  def show(self):
    if not self.override_cage_color:
      self.set_range_color(CAGE_ROW, CAGE_RANGE.start, CAGE_RANGE.stop, self.cage_color)

    for line in self.datalines:
      line.show()

  def clear(self, color=Color(0, 0, 0)):
    for row in range(4):
      self.set_range_color(row, 0, 43, color)
    self.show()


ANIMATIONS = [
  # rainbow.rainbow,
  # stripes.stripes,
  # randbow.randbow,
  # checkeredrainbow.checkeredrainbow,
  # snake.snake,
  single_led_test.single_led_test
]

def start():

  controller = Controller()
  controller.clear()

  # test.test(controller)

  while True:
    random.choice(ANIMATIONS)(controller)



# # Finding right pin & channel combinations:
# for i in range(0, 40):
#   for c in range(0, 1):
#     try:
#       strip = Adafruit_NeoPixel(
#         LED_COUNT, i, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, c
#       )
#       strip.begin()
#       print("yes ", i, c)
#     except Exception:
#       print("not ", i, c)