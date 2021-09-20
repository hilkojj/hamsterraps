import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
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

NOTES = {
  "B0": 31, "C1": 33, "CS1": 35, "D1":  37, "DS1": 39, "E1":  41, "F1":  44, "FS1": 46, "G1":  49, "GS1": 52, "A1":  55, "AS1": 58, "B1":  62, "C2":  65, "CS2": 69, "D2":  73, "DS2": 78, "E2":  82, "F2":  87, "FS2": 93, "G2":  98, "GS2": 104, "A2":  110, "AS2": 117, "B2":  123, "C3":  131, "CS3": 139, "D3":  147, "DS3": 156, "E3":  165, "F3":  175, "FS3": 185, "G3":  196, "GS3": 208, "A3":  220, "AS3": 233, "B3":  247, "C4":  262, "CS4": 277, "D4":  294, "DS4": 311, "E4":  330, "F4":  349, "FS4": 370, "G4":  392, "GS4": 415, "A4":  440, "AS4": 466, "B4":  494, "C5":  523, "CS5": 554, "D5":  587, "DS5": 622, "E5":  659, "F5":  698, "FS5": 740, "G5":  784, "GS5": 831, "A5":  880, "AS5": 932, "B5":  988, "C6":  1047, "CS6": 1109, "D6":  1175, "DS6": 1245, "E6":  1319, "F6":  1397, "FS6": 1480, "G6":  1568, "GS6": 1661, "A6":  1760, "AS6": 1865, "B6":  1976, "C7":  2093, "CS7": 2217, "D7":  2349, "DS7": 2489, "E7":  2637, "F7":  2794, "FS7": 2960, "G7":  3136, "GS7": 3322, "A7":  3520, "AS7": 3729, "B7":  3951, "C8":  4186, "CS8": 4435, "D8":  4699, "DS8": 4978
}


MARIO_MELODY = [
  "E7", "E7", 0, "E7",
  0, "C7", "E7", 0,
  "G7", 0, 0,  0,
  "G6", 0, 0, 0,

  "C7", 0, 0, "G6",
  0, 0, "E6", 0,
  0, "A6", 0, "B6",
  0, "NS6", "A6", 0,

  "G6", "E7", "G7",
  "A7", 0, "F7", "G7",
  0, "E7", 0, "C7",
  "D7", "B6", 0, 0,

  "C7", 0, 0, "G6",
  0, 0, "E6", 0,
  0, "A6", 0, "B6",
  0, "NS6", "A6", 0,

  "G6", "E7", "G7",
  "A7", 0, "F7", "G7",
  0, "E7", 0, "C7",
  "D7", "B6", 0, 0
]
MARIO_TEMPO = [
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
]


UNDERWORLD_MELODY = [
  "C4", "C5", "A3", "A4",
  "AS3", "AS4", 0,
  0,
  "C4", "C5", "A3", "A4",
  "AS3", "AS4", 0,
  0,
  "F3", "F4", "D3", "D4",
  "DS3", "DS4", 0,
  0,
  "F3", "F4", "D3", "D4",
  "DS3", "DS4", 0,
  0, "DS4", "CS4", "D4",
  "CS4", "DS4",
  "DS4", "GS3",
  "G3", "CS4",
  "C4", "FS4", "F4", "E3", "AS4", "A4",
  "GS4", "DS4", "B3",
  "AS3", "A3", "GS3",
  0, 0, 0
]
UNDERWORLD_TEMPO = [
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  6, 18, 18, 18,
  6, 6,
  6, 6,
  6, 6,
  18, 18, 18, 18, 18, 18,
  10, 10, 10,
  10, 10, 10,
  3, 3, 3
]

TETRIS_MELODY = [
  "E5", "B4", "C5", "D5", "C5", "B4", "A4", "A4", "C5", "E5", "D5", "C5", "B4", "B4", "C5", "D5", "E5", "C5", "A4", "A4", "R",
  "D5", "F5", "A5", "G5", "F5", "E5", "C5", "E5", "D5", "C5", "B4", "B4", "C5", "D5", "E5", "C5", "A4", "A4", "R",

  # part 2
  "E4", "C4", "D4", "B3", "C4", "A3", "GS3", "B3",
  "E4", "C4", "D4", "B3", "C4", "E4", "A4", "A4", "GS4", "R"
]
TETRIS_TEMPO = [

  3 / x for x in
  [
    # part 1
    0.5,  0.5,  0.5,  0.5,  0.5,  0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5,  0.5,  0.5,  0.5,  0.5,  0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,

    # part 2
    0.5,  0.5,  0.5,  0.5,  0.5,  0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5,  0.5,  0.5,  0.5,  0.5,  0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5
  ]
]


BLUB_MELODY = [
  list(NOTES.keys())[list(NOTES.values()).index(freq)] for freq in
  [262,294,330,262,262,294,330,262,330,349,392,330,349,392,392,440,392,349,330,262,392,440,392,349,330,262,262,196,262,262,196,262]
]
BLUB_TEMPO = [
  3 / x for x in
  [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,1,0.25,0.25,0.25,0.25,0.5,0.5,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,1,0.5,0.5,1]
]

def play(melody, tempo):
  try:
    i = 0
    for note in melody:
      duration = 1 / tempo[i]
      if note in NOTES:
        freq = NOTES[note]
        buzz(freq, duration)
        
      else:
        time.sleep(duration)

      time.sleep(duration * 1.)
      i += 1

  except: #KeyboardInterrupt:
    GPIO.output(BUZZER, False)

# play(MARIO_MELODY, MARIO_TEMPO)
play(UNDERWORLD_MELODY, UNDERWORLD_TEMPO)
time.sleep(1)
play(TETRIS_MELODY, TETRIS_TEMPO)
time.sleep(1)
play(BLUB_MELODY, BLUB_TEMPO)
