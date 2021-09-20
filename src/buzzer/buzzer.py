import RPi.GPIO as GPIO
import time
from . import songs, notes

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER = 23
GPIO.setup(BUZZER, GPIO.OUT)

def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
      GPIO.output(BUZZER, True)
      time.sleep(halveWaveTime)
      GPIO.output(BUZZER, False)
      time.sleep(halveWaveTime)

def play(melody, tempo, sleep_multiplier=1):
  try:
    i = 0
    for note in melody:
      duration = 1 / abs(tempo[i])
      if note in notes.NOTES:
        freq = notes.NOTES[note]
        buzz(freq, duration)
        
      else:
        time.sleep(duration)

      time.sleep(duration * sleep_multiplier)
      i += 1

  except: #KeyboardInterrupt:
    GPIO.output(BUZZER, False)

if __name__ == "__main__":

  # play(MARIO_MELODY, MARIO_TEMPO)
  print("mario underworld")
  play(songs.UNDERWORLD_MELODY, songs.UNDERWORLD_TEMPO)
  time.sleep(1)
  print("tetris")
  play(songs.TETRIS_MELODY, songs.TETRIS_TEMPO, 1.5)
  time.sleep(1)
  print("?????")
  play(songs.BLUB_MELODY, songs.BLUB_TEMPO)
  time.sleep(1)
  print("mii")
  play(songs.MII_MELODY, songs.MII_TEMPO)
