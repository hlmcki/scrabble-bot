# TO-DO: Remove hard-coding of 15 as maximum word length from possible_words function

import copy
import random

BOARD = [["TW", "  ", "  ", "DL", "  ", "  ", "  ", "TW", "  ", "  ", "  ", "DL", "  ", "  ", "TW"],
         ["  ", "DW", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "DW", "  "],
         ["  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  "],
         ["DL", "  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  ", "DL"],
         ["  ", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "  "],
         ["  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  "],
         ["  ", "  ", "DL", "  ", "  ", "  ", "DL", "  ", "DL", "  ", "  ", "  ", "DL", "  ", "  "],
         ["TW", "  ", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "  ", "TW"],
         ["  ", "  ", "DL", "  ", "  ", "  ", "DL", "  ", "DL", "  ", "  ", "  ", "DL", "  ", "  "],
         ["  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  "],
         ["  ", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "  "],
         ["DL", "  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  ", "DL"],
         ["  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  "],
         ["  ", "DW", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "DW", "  "],
         ["TW", "  ", "  ", "DL", "  ", "  ", "  ", "TW", "  ", "  ", "  ", "DL", "  ", "  ", "TW"]
        ]

BLANK_BOARD = [["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
              ]

WORD_MULTIPLIERS =  [[3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3],
                     [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
                     [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
                     [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
                     [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 3],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
                     [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
                     [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
                     [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
                     [3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3]
                    ]

LETTER_MULTIPLIERS = [[1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
                      [1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1],
                      [2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1],
                      [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
                      [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
                      [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
                      [1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2],
                      [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1],
                      [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]
                     ]

SCORES = {" ": 0,
          "A": 1, 
          "B": 3, 
          "C": 3,
          "D": 2,
          "E": 1,
          "F": 4,
          "G": 2,
          "H": 4,
          "I": 1,
          "J": 8,
          "K": 5,
          "L": 1,
          "M": 3,
          "N": 1,
          "O": 1,
          "P": 3,
          "Q": 10,
          "R": 1,
          "S": 1,
          "T": 1,
          "U": 1,
          "V": 4,
          "W": 4,
          "X": 8,
          "Y": 4,
          "Z": 10
         }

TILES =  {" ": 2,
          "A": 9, 
          "B": 2, 
          "C": 2,
          "D": 4,
          "E": 12,
          "F": 2,
          "G": 3,
          "H": 2,
          "I": 9,
          "J": 1,
          "K": 1,
          "L": 4,
          "M": 2,
          "N": 6,
          "O": 8,
          "P": 2,
          "Q": 1,
          "R": 6,
          "S": 4,
          "T": 6,
          "U": 4,
          "V": 2,
          "W": 2,
          "X": 1,
          "Y": 2,
          "Z": 1
         }

COORDINATES = {"A1" : {"A": 0 , "D": 0 }, 
               "B1" : {"A": 1 , "D": 0 },
               "C1" : {"A": 2 , "D": 0 },
               "D1" : {"A": 3 , "D": 0 }, 
               "E1" : {"A": 4 , "D": 0 },
               "F1" : {"A": 5 , "D": 0 },
               "G1" : {"A": 6 , "D": 0 },
               "H1" : {"A": 7 , "D": 0 },
               "I1" : {"A": 8 , "D": 0 },
               "J1" : {"A": 9 , "D": 0 },
               "K1" : {"A": 10, "D": 0 },
               "L1" : {"A": 11, "D": 0 },
               "M1" : {"A": 12, "D": 0 },
               "N1" : {"A": 13, "D": 0 },
               "O1" : {"A": 14, "D": 0 },
               "A2" : {"A": 0 , "D": 1 }, 
               "B2" : {"A": 1 , "D": 1 },
               "C2" : {"A": 2 , "D": 1 },
               "D2" : {"A": 3 , "D": 1 }, 
               "E2" : {"A": 4 , "D": 1 },
               "F2" : {"A": 5 , "D": 1 },
               "G2" : {"A": 6 , "D": 1 },
               "H2" : {"A": 7 , "D": 1 },
               "I2" : {"A": 8 , "D": 1 },
               "J2" : {"A": 9 , "D": 1 },
               "K2" : {"A": 10, "D": 1 },
               "L2" : {"A": 11, "D": 1 },
               "M2" : {"A": 12, "D": 1 },
               "N2" : {"A": 13, "D": 1 },
               "O2" : {"A": 14, "D": 1 },
               "A3" : {"A": 0 , "D": 2 }, 
               "B3" : {"A": 1 , "D": 2 },
               "C3" : {"A": 2 , "D": 2 },
               "D3" : {"A": 3 , "D": 2 }, 
               "E3" : {"A": 4 , "D": 2 },
               "F3" : {"A": 5 , "D": 2 },
               "G3" : {"A": 6 , "D": 2 },
               "H3" : {"A": 7 , "D": 2 },
               "I3" : {"A": 8 , "D": 2 },
               "J3" : {"A": 9 , "D": 2 },
               "K3" : {"A": 10, "D": 2 },
               "L3" : {"A": 11, "D": 2 },
               "M3" : {"A": 12, "D": 2 },
               "N3" : {"A": 13, "D": 2 },
               "O3" : {"A": 14, "D": 2 },
               "A4" : {"A": 0 , "D": 3 }, 
               "B4" : {"A": 1 , "D": 3 },
               "C4" : {"A": 2 , "D": 3 },
               "D4" : {"A": 3 , "D": 3 }, 
               "E4" : {"A": 4 , "D": 3 },
               "F4" : {"A": 5 , "D": 3 },
               "G4" : {"A": 6 , "D": 3 },
               "H4" : {"A": 7 , "D": 3 },
               "I4" : {"A": 8 , "D": 3 },
               "J4" : {"A": 9 , "D": 3 },
               "K4" : {"A": 10, "D": 3 },
               "L4" : {"A": 11, "D": 3 },
               "M4" : {"A": 12, "D": 3 },
               "N4" : {"A": 13, "D": 3 },
               "O4" : {"A": 14, "D": 3 },
               "A5" : {"A": 0 , "D": 4 }, 
               "B5" : {"A": 1 , "D": 4 },
               "C5" : {"A": 2 , "D": 4 },
               "D5" : {"A": 3 , "D": 4 }, 
               "E5" : {"A": 4 , "D": 4 },
               "F5" : {"A": 5 , "D": 4 },
               "G5" : {"A": 6 , "D": 4 },
               "H5" : {"A": 7 , "D": 4 },
               "I5" : {"A": 8 , "D": 4 },
               "J5" : {"A": 9 , "D": 4 },
               "K5" : {"A": 10, "D": 4 },
               "L5" : {"A": 11, "D": 4 },
               "M5" : {"A": 12, "D": 4 },
               "N5" : {"A": 13, "D": 4 },
               "O5" : {"A": 14, "D": 4 },
               "A6" : {"A": 0 , "D": 5 }, 
               "B6" : {"A": 1 , "D": 5 },
               "C6" : {"A": 2 , "D": 5 },
               "D6" : {"A": 3 , "D": 5 }, 
               "E6" : {"A": 4 , "D": 5 },
               "F6" : {"A": 5 , "D": 5 },
               "G6" : {"A": 6 , "D": 5 },
               "H6" : {"A": 7 , "D": 5 },
               "I6" : {"A": 8 , "D": 5 },
               "J6" : {"A": 9 , "D": 5 },
               "K6" : {"A": 10, "D": 5 },
               "L6" : {"A": 11, "D": 5 },
               "M6" : {"A": 12, "D": 5 },
               "N6" : {"A": 13, "D": 5 },
               "O6" : {"A": 14, "D": 5 },
               "A7" : {"A": 0 , "D": 6 }, 
               "B7" : {"A": 1 , "D": 6 },
               "C7" : {"A": 2 , "D": 6 },
               "D7" : {"A": 3 , "D": 6 }, 
               "E7" : {"A": 4 , "D": 6 },
               "F7" : {"A": 5 , "D": 6 },
               "G7" : {"A": 6 , "D": 6 },
               "H7" : {"A": 7 , "D": 6 },
               "I7" : {"A": 8 , "D": 6 },
               "J7" : {"A": 9 , "D": 6 },
               "K7" : {"A": 10, "D": 6 },
               "L7" : {"A": 11, "D": 6 },
               "M7" : {"A": 12, "D": 6 },
               "N7" : {"A": 13, "D": 6 },
               "O7" : {"A": 14, "D": 6 },
               "A8" : {"A": 0 , "D": 7 }, 
               "B8" : {"A": 1 , "D": 7 },
               "C8" : {"A": 2 , "D": 7 },
               "D8" : {"A": 3 , "D": 7 }, 
               "E8" : {"A": 4 , "D": 7 },
               "F8" : {"A": 5 , "D": 7 },
               "G8" : {"A": 6 , "D": 7 },
               "H8" : {"A": 7 , "D": 7 },
               "I8" : {"A": 8 , "D": 7 },
               "J8" : {"A": 9 , "D": 7 },
               "K8" : {"A": 10, "D": 7 },
               "L8" : {"A": 11, "D": 7 },
               "M8" : {"A": 12, "D": 7 },
               "N8" : {"A": 13, "D": 7 },
               "O8" : {"A": 14, "D": 7 },
               "A9" : {"A": 0 , "D": 8 }, 
               "B9" : {"A": 1 , "D": 8 },
               "C9" : {"A": 2 , "D": 8 },
               "D9" : {"A": 3 , "D": 8 }, 
               "E9" : {"A": 4 , "D": 8 },
               "F9" : {"A": 5 , "D": 8 },
               "G9" : {"A": 6 , "D": 8 },
               "H9" : {"A": 7 , "D": 8 },
               "I9" : {"A": 8 , "D": 8 },
               "J9" : {"A": 9 , "D": 8 },
               "K9" : {"A": 10, "D": 8 },
               "L9" : {"A": 11, "D": 8 },
               "M9" : {"A": 12, "D": 8 },
               "N9" : {"A": 13, "D": 8 },
               "O9" : {"A": 14, "D": 8 },
               "A10": {"A": 0 , "D": 9 }, 
               "B10": {"A": 1 , "D": 9 },
               "C10": {"A": 2 , "D": 9 },
               "D10": {"A": 3 , "D": 9 }, 
               "E10": {"A": 4 , "D": 9 },
               "F10": {"A": 5 , "D": 9 },
               "G10": {"A": 6 , "D": 9 },
               "H10": {"A": 7 , "D": 9 },
               "I10": {"A": 8 , "D": 9 },
               "J10": {"A": 9 , "D": 9 },
               "K10": {"A": 10, "D": 9 },
               "L10": {"A": 11, "D": 9 },
               "M10": {"A": 12, "D": 9 },
               "N10": {"A": 13, "D": 9 },
               "O10": {"A": 14, "D": 9 },
               "A11": {"A": 0 , "D": 10}, 
               "B11": {"A": 1 , "D": 10},
               "C11": {"A": 2 , "D": 10},
               "D11": {"A": 3 , "D": 10}, 
               "E11": {"A": 4 , "D": 10},
               "F11": {"A": 5 , "D": 10},
               "G11": {"A": 6 , "D": 10},
               "H11": {"A": 7 , "D": 10},
               "I11": {"A": 8 , "D": 10},
               "J11": {"A": 9 , "D": 10},
               "K11": {"A": 10, "D": 10},
               "L11": {"A": 11, "D": 10},
               "M11": {"A": 12, "D": 10},
               "N11": {"A": 13, "D": 10},
               "O11": {"A": 14, "D": 10},
               "A12": {"A": 0 , "D": 11}, 
               "B12": {"A": 1 , "D": 11},
               "C12": {"A": 2 , "D": 11},
               "D12": {"A": 3 , "D": 11}, 
               "E12": {"A": 4 , "D": 11},
               "F12": {"A": 5 , "D": 11},
               "G12": {"A": 6 , "D": 11},
               "H12": {"A": 7 , "D": 11},
               "I12": {"A": 8 , "D": 11},
               "J12": {"A": 9 , "D": 11},
               "K12": {"A": 10, "D": 11},
               "L12": {"A": 11, "D": 11},
               "M12": {"A": 12, "D": 11},
               "N12": {"A": 13, "D": 11},
               "O12": {"A": 14, "D": 11},
               "A13": {"A": 0 , "D": 12}, 
               "B13": {"A": 1 , "D": 12},
               "C13": {"A": 2 , "D": 12},
               "D13": {"A": 3 , "D": 12}, 
               "E13": {"A": 4 , "D": 12},
               "F13": {"A": 5 , "D": 12},
               "G13": {"A": 6 , "D": 12},
               "H13": {"A": 7 , "D": 12},
               "I13": {"A": 8 , "D": 12},
               "J13": {"A": 9 , "D": 12},
               "K13": {"A": 10, "D": 12},
               "L13": {"A": 11, "D": 12},
               "M13": {"A": 12, "D": 12},
               "N13": {"A": 13, "D": 12},
               "O13": {"A": 14, "D": 12},
               "A14": {"A": 0 , "D": 13}, 
               "B14": {"A": 1 , "D": 13},
               "C14": {"A": 2 , "D": 13},
               "D14": {"A": 3 , "D": 13}, 
               "E14": {"A": 4 , "D": 13},
               "F14": {"A": 5 , "D": 13},
               "G14": {"A": 6 , "D": 13},
               "H14": {"A": 7 , "D": 13},
               "I14": {"A": 8 , "D": 13},
               "J14": {"A": 9 , "D": 13},
               "K14": {"A": 10, "D": 13},
               "L14": {"A": 11, "D": 13},
               "M14": {"A": 12, "D": 13},
               "N14": {"A": 13, "D": 13},
               "O14": {"A": 14, "D": 13},
               "A15": {"A": 0 , "D": 14}, 
               "B15": {"A": 1 , "D": 14},
               "C15": {"A": 2 , "D": 14},
               "D15": {"A": 3 , "D": 14}, 
               "E15": {"A": 4 , "D": 14},
               "F15": {"A": 5 , "D": 14},
               "G15": {"A": 6 , "D": 14},
               "H15": {"A": 7 , "D": 14},
               "I15": {"A": 8 , "D": 14},
               "J15": {"A": 9 , "D": 14},
               "K15": {"A": 10, "D": 14},
               "L15": {"A": 11, "D": 14},
               "M15": {"A": 12, "D": 14},
               "N15": {"A": 13, "D": 14},
               "O15": {"A": 14, "D": 14}
              }

with open("dictionary.txt", "r") as file:
    DICTIONARY = file.read()
    DICTIONARY = DICTIONARY.split("\n")

class Scrabble():
    """
    Scrabble game representation
    """
    def __init__(self, players, board=BLANK_BOARD):
        
        # Number of players
        self.players = players

        # Board
        self.board = board

    def print(self):
        """
        Prints board in user-friendly format
        """
        print("\nBoard:")
        print("\n    A B C D E F G H I J K L M N O")
        for i in range(15):
            row = ""
            for j in range(15):
                if self.board[i][j] == "":
                    row += " _"
                else:
                    row += " " + self.board[i][j]
            print((" " + str(i + 1))[-2:], row)
        print("")

    def play_word(self, word, start, direction):
        """
        Plays a word on board
        """
        D = COORDINATES[start]["D"]
        A = COORDINATES[start]["A"]
        for i in range(len(word)):
            letter = word[i]
            if direction == "D":
                self.board[D + i][A] = letter
            if direction == "A":
                self.board[D][A + i] = letter

class Scrabble_old():
    """
    Scrabble game representation
    """
    def __init__(self, players=2):

        # Number of players
        self.players = players

        # Scores for each player
        self.scores = {}
        for i in range(players):
            self.scores[i + 1] = 0

        # Turn
        self.turn = 1

        # Tiles
        self.tiles = [" ", " ", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C",
                      "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
                      "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I",
                      "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N",
                      "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R",
                      "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U",
                      "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z"
                     ]
        random.shuffle(self.tiles)

        # Give seven tiles to each player
        self.hands = {}
        for i in range(players):
            self.hands[i + 1] = self.tiles[0:7]
            del(self.tiles[0:7])

        # Board
        self.board = [["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                     ]
        
    def print(self):
        """
        Prints current board in user-friendly format
        """
        print("\nBoard:")
        print("\n    A B C D E F G H I J K L M N O")
        for i in range(15):
            row = ""
            for j in range(15):
                if self.board[i][j] == "":
                    row += " _"
                else:
                    row += " " + self.board[i][j]
            print((" " + str(i + 1))[-2:], row)
        print("")

    def scan_board(self, board):
        """
        Returns a list of all words on the board and the squares they occupy
        """
        words = []
        # Scan rows
        for i in range(15):
            word = ""
            location = []
            for j in range(15):
                letter = board[i][j]
                if letter == "":
                    if len(word) > 1:
                        words.append((word, location))
                    word = ""
                    location = []
                else:
                    word += letter
                    location.append((j, i))
        
        # Scan columns
        for i in range(15):
            word = ""
            location = []
            for j in range(15):
                letter = board[j][i]
                if letter == "":
                    if len(word) > 1:
                        words.append((word, location))
                    word = ""
                    location = []
                else:
                    word += letter
                    location.append((i, j))
        
        return words

    def compare_boards(self, board_before, board_after):
        """
        Returns list of locations where tiles have been played on most recent turn
        """
        locations = []
        for i in range(15):
            for j in range(15):
                if board_before[i][j] != board_after[i][j]:
                    locations.append((j, i))
        
        return locations

    def new_words(self, board_before, board_after):
        """
        Returns list of all new words on board after move played and where they are located
        """
        words = []
        words_before = self.scan_board(board_before)
        words_after = self.scan_board(board_after)

        for word in words_after:
            if word in words_before:
                words_before.remove(word)
            else:
                words.append(word)

        return words

    def score_word(self, word, board_before, board_after):
        """
        Returns number of points scored for a word
        """
        points = 0
        word_multiplier = 1
        locations = self.compare_boards(board_before, board_after)
        for i in range(len(word[0])):
            letter = word[0][i]
            x = word[1][i][0]
            y = word[1][i][1]
            if (x, y) in locations:
                points += SCORES[letter] * LETTER_MULTIPLIERS[y][x]
                word_multiplier *= WORD_MULTIPLIERS[y][x]
            else:
                points += SCORES[letter]
        points = points * word_multiplier

        return points

    def score_move(self, board_before, board_after):
        """
        Returns number of points scored for a move
        """
        points = 0
        words = self.new_words(board_before, board_after)
        for word in words:
            points += self.score_word(word, board_before, board_after)

        return points

    def play_word(self, word, start, direction):
        """
        Plays a word on board and updates scores accordingly
        """
        # Play word on board
        board_before = copy.deepcopy(self.board)
        x = COORDINATES[start]["A"]
        y = COORDINATES[start]["D"]
        for i in range(len(word)):
            letter = word[i]
            if direction == "A":
                if self.board[y][x + i] == "":
                    self.board[y][x + i] = letter
                    self.hands[self.turn].remove(letter)
            if direction == "D":
                if self.board[y + i][x] == "":
                    self.board[y + i][x] = letter
                    self.hands[self.turn].remove(letter)
        board_after = copy.deepcopy(self.board)

        # Update scores
        self.scores[self.turn] += self.score_move(board_before, board_after)

        if len(self.hands[self.turn]) == 0:
            self.scores[self.turn] += 50
        
        # locations = []
        # for i in range(len(word)):
        #     locations.append((x, y))
        #     if direction == "A":
        #         x += 1
        #     if direction == "D":
        #         y += 1
        # score = 0
        # word_multiplier = 1
        # for location in locations:
        #     x = location[0]
        #     y = location[1]
        #     score += SCORES[self.board[y][x]] * LETTER_MULTIPLIERS[y][x]
        #     if BOARD[y][x] == "DW":
        #         word_multiplier = 2
        #     if BOARD[y][x] == "TW":
        #         word_multiplier = 3
        # self.scores[self.turn] += score * word_multiplier
        
        # Update turn
        self.turn = (self.turn % self.players) + 1
    
    def draw_tiles(self):
        """
        Draws tiles to the current player's hand
        """
        draw = 7 - len(self.hands[self.turn])
        for tile in self.tiles[0:draw]:
            self.hands[self.turn].append(tile)
        del(self.tiles[0:draw])

    def is_valid_move(self, board, word, location, direction):
        """
        Returns True if word can be played on board from starting square in given direction, otherwise returns False
        """
        x = location[0]
        y = location[1]

        # Check if word in dictionary
        if word not in DICTIONARY:
            return False
        
        # Check if there is enough space to play word on board from starting square in given direction
        if direction == "A":
            if x + len(word) > 15:
                return False
        if direction == "D":
            if y + len(word) > 15:
                return False
        
        # Check if word will fit with existing letters on the board
        if direction == "A":
            for i in range(len(word)):
                letter = word[i]
                if board[y][x + i] != "" and board[y][x + i] != letter:
                    return False
        if direction == "D":
            for i in range(len(word)):
                letter = word[i]
                if board[y + i][x] != "" and board[y + i][x] != letter:
                    return False

        # Check if playing word will result in any invalid words

        # Play word on board
        board_after = copy.deepcopy(board)
        for i in range(len(word)):
            letter = word[i]
            if direction == "A":
                if board_after[y][x + i] == "":
                    board_after[y][x + i] = letter
            if direction == "D":
                if board_after[y + i][x] == "":
                    board_after[y + i][x] = letter
        
        words = self.scan_board(board_after)
        
        for word in words:
            if word[0] not in DICTIONARY:
                return False
        
        return True

    def playable_squares(self, location, board):
        """
        Given a location on the board, returns a dictionary containing the furthest square in each direction that could possibly be reached with a move
        """
        limits = dict()
        x = location[0]
        y = location[1]
        
        # Horizontally
        if x == 7:
            limits["L"] = (0, y)
            limits["R"] = (14, y)
        if x < 7:
            limits["L"] = (0, y)
            i, n = x + 1, 0
            while n < 8 and i <= 14:
                if board[y][i] == "":
                    n += 1
                i += 1
            limits["R"] = (i - 2, y)
        if x > 7:
            limits["R"] = (14, y)
            i, n = x - 1, 0
            while n < 8 and i >= 0:
                if board[y][i] == "":
                    n += 1
                i -= 1
            limits["L"] = (i + 2, y)
        
        # Vertically
        if y == 7:
            limits["U"] = (x, 0)
            limits["D"] = (x, 14)
        if y < 7:
            limits["U"] = (x, 0)
            i, n = y + 1, 0
            while n < 8 and i <= 14:
                if board[i][x] == "":
                    n += 1
                i += 1
            limits["D"] = (x, i - 2)
        if y > 7:
            limits["D"] = (x, 14)
            i, n = y - 1, 0
            while n < 8 and i >= 0:
                if board[i][y] == "":
                    n += 1
                i -= 1
            limits["U"] = (x, i + 2)

        return limits

    def possible_moves(self, location, board, tiles):
        """
        Given a location on the board and list of tiles, returns all moves that can be played
        """  
        moves = []
        x = location[0]
        y = location[1]
        limits = self.playable_squares(location, board)
        xL = limits["L"][0]
        xR = limits["R"][0]
        yU = limits["U"][1]
        yD = limits["D"][1]
        words = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[]}
        for word in DICTIONARY:
            words[len(word)].append(word)

        # Horizontally
        # Starting square
        for i in range(xL, x + 1):
            # Word length
            for j in range(max(2, x - i + 1), 16 - i):
            # For each word of length, j, in the dictionary
                for word in words[j]:
                    if self.is_valid_move(board, word, location, "A"):
                        print(word)
        
        return moves

class ScrabbleAI():
    """
    Scrabble game player
    """
    def __init__(self, players=2):

        # Number of players
        self.players = players

class Move():
    """
    Represents a possible Scrabble move
    """
    def __init__(self, word, start, direction):

        self.word = word
        self.start = start
        self.direction = direction

    def print(self):
        """
        Prints move in user-friendly format
        """
        print("Word:\t\t" + self.word)
        print("Start:\t\t" + self.start)
        print("Direction:\t" + self.direction)

class Pattern():
    """
    """
    def __init__(self, pattern, start, direction):

        self.pattern = pattern
        self.start = start
        self.direction = direction

def is_word(word):
    """
    Returns True if word in dictionary, otherwise returns False
    """
    if word in DICTIONARY:
        return True
    else:
        return False

def possible_words(tiles):
    """
    Returns a dictionary of all possible words formed from a list of tiles, grouped by word length
    """
    words = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[]}
    for word in DICTIONARY:
        tiles_remaining = copy.deepcopy(tiles)
        for i in range(len(word)):
            letter = word[i]
            if letter in tiles_remaining:
                tiles_remaining.remove(letter)
                if i == len(word) - 1:
                    words[len(word)].append(word)
            else:
                if " " in tiles_remaining:
                    tiles_remaining.remove(" ")
                    if i == len(word) - 1:
                        words[len(word)].append(word)
                else:
                    break
    return words

def play_first_move(tiles):
    """
    Returns the word that will score the highest number of points on the first move, given a list of tiles
    """
    words = possible_words(tiles)
    max_score = 0
    # Starting square
    for i in range(1, 8):
        # Word length
        for j in range(max(2, 8 - i), 8):
            # For each word of length, j, in the dictionary
            for word in words[j]:
                score = 0
                tiles_remaining = copy.deepcopy(tiles)
                # For each letter in the word
                for k in range(len(word)):
                    letter = word[k]
                    if letter in tiles_remaining:
                        tiles_remaining.remove(letter)
                        score += SCORES[letter] * LETTER_MULTIPLIERS[7][i + k]
                    else:
                        tiles_remaining.remove(" ")
                score *= 2
                if score > max_score:
                    max_score = score
                    max_word = word
    
    return max_word, max_score

def play_second_move(board, tiles):
    """
    Returns the word that will score the highest number of points on the second move, given the board and a list of tiles
    """
    # for i in range(15):
    #     for j in range(15):
    #         if board[i][j] != "":
    #             for x in range(0, j):
    #                 for k in range(, 8)

def possible_moves_row(row, row_index, tiles, direction):
    """
    """
    patterns = []
    i = 0
    while i < 15:
        n = 0
        if row[i] == "":
            n += 1
        if i == 0 or row[i - 1] == "":
            j = i + 1
            while j < 15:
                if row[j] == "":
                    n += 1
                if n in range(1, 8):
                    if j == 14:
                        if direction == "A":
                            patterns.append([row[i:j + 1], (row_index, i), "A"])
                        if direction == "D":
                            patterns.append([row[i:j + 1], (i, row_index), "D"])
                    else:
                        if row[j + 1] == "":
                            if direction == "A":
                                patterns.append([row[i:j + 1], (row_index, i), "A"])
                            if direction == "D":
                                patterns.append([row[i:j + 1], (i, row_index), "D"])
                j += 1
        i += 1
    
    patterns_copy = []
    for i in range(len(patterns)):
        pattern = patterns[i][0]
        tmp = False
        for char in pattern:
            if char != "":
                tmp = True
                break
        if tmp == True:
            patterns_copy.append(patterns[i])

    patterns = patterns_copy

    moves = []
    for i in range(len(patterns)):
        pattern = patterns[i][0]
        location = patterns[i][1]
        direction = patterns[i][2]
        for word in DICTIONARY:
            if pattern_match(word, pattern, tiles):
                moves.append([word, location, direction])

    return moves

def pattern_match(word, pattern, tiles):
    """
    """
    if len(word) != len(pattern):
        return False

    tiles_remaining = copy.deepcopy(tiles)
    for i in range(len(word)):
        if word[i] != pattern[i]:
            if pattern[i] == "":
                if word[i] in tiles_remaining:
                    tiles_remaining.remove(word[i])
                else:
                    return False
            else:
                return False

    return True

def possible_moves(board, tiles):
    """
    """
    moves = []
    
    # Horizontally
    for i in range(15):
        moves_row = possible_moves_row(board[i][:], i, tiles, "A")
        for move in moves_row:
            moves.append(move)

    # Vertically
    for i in range(15):
        moves_column = possible_moves_row([row[i] for row in board], i, tiles, "D")
        for move in moves_column:
            moves.append(move)

    return moves

def scan_board(board):
    """
    Returns a list of all words on the board and the squares they occupy
    """
    words = []
    # Scan rows
    for i in range(15):
        word = ""
        location = []
        for j in range(15):
            letter = board[i][j]
            if letter == "":
                if len(word) > 1:
                    words.append((word, location))
                word = ""
                location = []
            else:
                word += letter
                location.append((j, i))
    
    # Scan columns
    for i in range(15):
        word = ""
        location = []
        for j in range(15):
            letter = board[j][i]
            if letter == "":
                if len(word) > 1:
                    words.append((word, location))
                word = ""
                location = []
            else:
                word += letter
                location.append((i, j))
    
    return words

def compare_boards(board_before, board_after):
    """
    Returns list of locations where tiles have been played on most recent turn
    """
    locations = []
    for i in range(15):
        for j in range(15):
            if board_before[i][j] != board_after[i][j]:
                locations.append((j, i))
    
    return locations

def new_words(board_before, board_after):
    """
    Returns list of all new words on board after move played and where they are located
    """
    words = []
    words_before = scan_board(board_before)
    words_after = scan_board(board_after)

    for word in words_after:
        if word in words_before:
            words_before.remove(word)
        else:
            words.append(word)

    return words

def score_word(word, board_before, board_after):
    """
    Returns number of points scored for a word
    """
    points = 0
    word_multiplier = 1
    locations = compare_boards(board_before, board_after)
    for i in range(len(word[0])):
        letter = word[0][i]
        x = word[1][i][0]
        y = word[1][i][1]
        if (x, y) in locations:
            points += SCORES[letter] * LETTER_MULTIPLIERS[y][x]
            word_multiplier *= WORD_MULTIPLIERS[y][x]
        else:
            points += SCORES[letter]
    points = points * word_multiplier

    return points

def score_move(board_before, board_after):
    """
    Returns number of points scored for a move
    """
    points = 0
    words = new_words(board_before, board_after)
    for word in words:
        points += score_word(word, board_before, board_after)

    return points

def play_word(board, word, start, direction):
    """
    Plays a word on board
    """
    board_after = copy.deepcopy(board)
    # Play word on board
    x = start[1]
    y = start[0]
    for i in range(len(word)):
        letter = word[i]
        if direction == "A":
            board_after[y][x + i] = letter
        if direction == "D":
            board_after[y + i][x] = letter

    return board_after

def max_move(board, tiles):
    """
    Given board and list of tiles, returns move that will score maximum number of points
    """
    moves = possible_moves(board, tiles)
    points = 0
    for i in range(len(moves)):
        word = moves[i][0]
        start = moves[i][1]
        direction = moves[i][2]
        score = score_move(board, play_word(board, word, start, direction))
        if score > points:
            max_move = Move(word, xy_to_letter_number(start), direction)
            points = score_move(board, play_word(board, word, start, direction)) 

    return max_move, points

def xy_to_letter_number(xy):
    """
    """
    x = xy[0]
    y = xy[1]
    letter_number = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"][x] + str(y + 1)

    return letter_number