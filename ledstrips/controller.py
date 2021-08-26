import time
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT = 11 * 4      # Number of LED pixels.

# https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/
# https://i.stack.imgur.com/gaU6t.png
LED_PIN_0 = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN_1 = 13
LED_PIN_2 = 19
LED_PIN_3 = 12

LED_FREQ_HZ = 800000    # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10            # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest


# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False

LED_CHANNEL_0 = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_CHANNEL_1 = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_CHANNEL_2 = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_CHANNEL_3 = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


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


def rainbow(strips, wait_ms=20, iterations=1):
  """Draw rainbow that fades across all pixels at once."""
  for j in range(256 * iterations):
    strip_i = 0
    for strip in strips:
      for i in range(strip.numPixels()):
        strip.setPixelColor(i, wheel((i + j) & 255))
      strip.show()
      strip_i += 1
  time.sleep(wait_ms / 1000.0)

def start():

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

  # Create NeoPixel objects with appropriate configuration.
  strips = [
    Adafruit_NeoPixel(
      LED_COUNT, LED_PIN_0, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL_0
    ),
    Adafruit_NeoPixel(
      LED_COUNT, LED_PIN_1, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL_1
    ),
    Adafruit_NeoPixel(
      LED_COUNT, LED_PIN_2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL_2
    ),
    Adafruit_NeoPixel(
      LED_COUNT, LED_PIN_3, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL_3
    )
  ]

  i = 0
  for strip in strips:
    # Intialize the library (must be called once before other functions).
    print("Initializing strip", i)
    strip.begin()
    i += 1

  while True:
    rainbow(strips)
