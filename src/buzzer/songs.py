from . import notes

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
  list(notes.NOTES.keys())[list(notes.NOTES.values()).index(freq)] for freq in
  [262,294,330,262,262,294,330,262,330,349,392,330,349,392,392,440,392,349,330,262,392,440,392,349,330,262,262,196,262,262,196,262]
]
BLUB_TEMPO = [
  4 / x for x in
  [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,1,0.25,0.25,0.25,0.25,0.5,0.5,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,1,0.5,0.5,1]
]


MII_MELODY = [
  "FS4",8,           "REST",8,           "A4",8,          "CS5",8,         "REST",8,         "A4",8,        "REST",8,       "FS4",8, # 1
  "D4",8,          "D4",8,          "D4",8,        "REST",8,         "REST",4,       "REST",8,        "CS4",8,
  "D4",8,          "FS4",8,         "A4",8,          "CS5",8,         "REST",8,         "A4",8,       "REST",8,        "F4",8,
  "E5",-4,           "DS5",8,           "D5",8,          "REST",8,         "REST",4,

  "GS4",8,           "REST",8,           "CS5",8,           "FS4",8,           "REST",8,         "CS5",8,         "REST",8,         "GS4",8, # 5
  "REST",8,           "CS5",8,           "G4",8,          "FS4",8,         "REST",8,         "E4",8,        "REST",8,
  "E4",8,          "E4",8,          "E4",8,        "REST",8,         "REST",4,       "E4",8,         "E4",8,
  "E4",8,          "REST",8,         "REST",4,         "DS4",8,       "D4",8, 

  "CS4",8,           "REST",8,           "A4",8,          "CS5",8,         "REST",8,         "A4",8,        "REST",8,       "FS4",8, # 9
  "D4",8,          "D4",8,          "D4",8,        "REST",8,         "E5",8,        "E5",8,       "E5",8,          "REST",8,
  "REST",8,           "FS4",8,           "A4",8,          "CS5",8,         "REST",8,         "A4",8,        "REST",8,         "F4",8,
  "E5",2,          "D5",8,          "REST",8,         "REST",4,

  "B4",8,          "G4",8,          "D4",8,        "CS4",4,         "B4",8,        "G4",8,       "CS4",8, # 13
  "A4",8,          "FS4",8,         "C4",8,          "B3",4,        "F4",8,        "D4",8,       "B3",8,
  "E4",8,          "E4",8,          "E4",8,        "REST",4,         "REST",4,       "AS4",4,
  "CS5",8,           "D5",8,          "FS5",8,         "A5",8,          "REST",8,         "REST",4, 

  "REST",2,           "A3",4,          "AS3",4, # 17 
  "A3",-4,           "A3",8,          "A3",2,
  "REST",4,           "A3",8,          "AS3",8,         "A3",8,          "F4",4,        "C4",8,
  "A3",-4,           "A3",8,          "A3",2,

  "REST",2,           "B3",4,          "C4",4, # 21
  "CS4",-4,          "C4",8,          "CS4",2,
  "REST",4,           "CS4",8,           "C4",8,          "CS4",8,         "GS4",4,         "DS4",8,
  "CS4",-4,          "DS4",8,         "B3",1,

  "E4",4,          "E4",4,          "E4",4,        "REST",8,# 25
]
MII_TEMPO = MII_MELODY[1::2]
MII_MELODY = MII_MELODY[::2]