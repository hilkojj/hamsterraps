import RPi.GPIO as GPIO
import time
from . import songs, notes
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

NICE_BUZZER = 24
HORROR_BUZZER = 23

GPIO.setup(NICE_BUZZER, GPIO.OUT)
GPIO.setup(HORROR_BUZZER, GPIO.OUT)

def buzz(buzzer, noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for _ in range(waves):
      GPIO.output(buzzer, True)
      time.sleep(halveWaveTime)
      GPIO.output(buzzer, False)
      time.sleep(halveWaveTime)

def play(buzzer, melody, tempo, sleep_multiplier=1):
  try:
    i = 0
    for note in melody:
      duration = 1 / abs(tempo[i])
      if note in notes.NOTES:
        freq = notes.NOTES[note]
        buzz(buzzer, freq, duration)
        
      else:
        time.sleep(duration)

      time.sleep(duration * sleep_multiplier)
      i += 1

  except KeyboardInterrupt:
    GPIO.output(buzzer, False)


if __name__ == "__main__":

  buzzer = NICE_BUZZER

  if len(sys.argv) > 1:
    if sys.argv[1] == "horror":
      buzzer = HORROR_BUZZER

  if len(sys.argv) > 2:
    song = sys.argv[2]
    if song in songs.SONG_NAMES:
      play(buzzer, songs.SONG_NAMES[song][0], songs.SONG_NAMES[song][1])



  # # play(MARIO_MELODY, MARIO_TEMPO)
  # print("mario underworld")
  # play(NICE_BUZZER, songs.UNDERWORLD_MELODY, songs.UNDERWORLD_TEMPO)
  # time.sleep(1)
  # print("tetris")
  # play(NICE_BUZZER, songs.TETRIS_MELODY, songs.TETRIS_TEMPO, 1.5)
  # time.sleep(1)
  # print("?????")
  # play(NICE_BUZZER, songs.BLUB_MELODY, songs.BLUB_TEMPO)
  # time.sleep(1)
  # print("mii")
  # play(NICE_BUZZER, songs.MII_MELODY, songs.MII_TEMPO)
