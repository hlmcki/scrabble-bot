import copy
import time

BLANK = "."

BOARD_BLANK = [[BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK]
              ]

MULTIPLIERS_WORD =  [[3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3],
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

MULTIPLIERS_LETTER = [[1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
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
    def __init__(self, players, board=copy.deepcopy(BOARD_BLANK)):
        
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
                if self.board[i][j] == BLANK:
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

class Move():
    """
    Scrabble move representation
    """
    def __init__(self, word, start, direction, score=-1):

        self.word = word
        self.start = start
        self.direction = direction
        self.score = score

    def print(self):
        """
        Prints move in user-friendly format
        """
        print("Word:\t\t" + self.word)
        print("Start:\t\t" + self.start)
        print("Direction:\t" + self.direction)
        print("Score:\t\t" + str(self.score))

def possible_moves_row(row, row_index, tiles, direction):
    """
    Returns a list of possible moves for a row or column
    """
    patterns = []
    for i in range(15):
            for j in range(i, 15):
                    pattern = row[i:j + 1]
                    # Pattern is only valid if it is has blanks before and after it
                    if (i == 0 or row[i - 1] == BLANK) and (j == 14 or row[j + 1] == BLANK):
                            count_blanks = 0
                            count_letters = 0
                            for character in pattern:
                                    if character == BLANK:
                                            count_blanks += 1
                                    else:
                                            count_letters += 1
                            # Pattern is only valid if it has between 1 and 7 blanks and at least 1 letter
                            if count_blanks in range(1, 8) and count_letters > 0:
                                    if direction == "A":
                                        patterns.append(Move("".join(pattern), xy_to_letter_number((i, row_index)), direction))
                                    if direction == "D":
                                        patterns.append(Move("".join(pattern), xy_to_letter_number((row_index, i)), direction))

    for pattern in patterns:
        pattern.print()
    start = time.time()
    moves = []
    for pattern in patterns:
        for word in DICTIONARY:
            if len(pattern.word) == len(word):
                tiles_remaining = copy.deepcopy(tiles)
                for i in range(len(word)):
                    if word[i] != pattern.word[i]:
                        if pattern.word[i] == BLANK:
                            if word[i] in tiles_remaining:
                                tiles_remaining.remove(word[i])
                                if i == len(word) - 1:
                                    moves.append(Move(word, pattern.start, pattern.direction))
                            else:
                                break
                        else:
                            break
    print(time.time() - start)
    
    return moves
    

def possible_moves(board, tiles):
    """
    Returns a list of all possible moves
    """
    moves = []
    
    # Horizontally
    for i in range(15):
        row = ""
        for character in board[i][:]:
            row += character
        moves_row = possible_moves_row(row, i, tiles, "A")
        for move in moves_row:
            moves.append(move)

    # Vertically
    for i in range(15):
        column = ""
        for character in [row[i] for row in board]:
            column += character
        moves_column = possible_moves_row(column, i, tiles, "D")
        for move in moves_column:
            moves.append(move)

    # Discard any moves that form non-words with existing tiles on board
    moves_invalid = []
    for move in moves:
        words_new = new_words(board, play_word(board, move.word, move.start, move.direction))
        for word in words_new:
            if word[0] not in DICTIONARY:
                moves_invalid.append(move)
                break
    for move in moves_invalid:
        moves.remove(move)

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
            if letter == BLANK:
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
            if letter == BLANK:
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
            points += SCORES[letter] * MULTIPLIERS_LETTER[y][x]
            word_multiplier *= MULTIPLIERS_WORD[y][x]
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
    A = COORDINATES[start]["A"]
    D = COORDINATES[start]["D"]
    for i in range(len(word)):
        letter = word[i]
        if direction == "A":
            board_after[D][A + i] = letter
        if direction == "D":
            board_after[D + i][A] = letter

    return board_after

def max_move(board, tiles):
    """
    Given board and list of tiles, returns move that will score maximum number of points
    """
    if board == BOARD_BLANK:
        max_move = max_first_move(tiles)
    else:
        moves = possible_moves(board, tiles)
        max_score = 0
        for move in moves:
            move.score = score_move(board, play_word(board, move.word, move.start, move.direction))
            if move.score > max_score:
                max_move = move
                max_score = move.score

    return max_move

def xy_to_letter_number(xy):
    """
    Converts an (x, y) coordinate pair to a letter number coordinate, e.g. converts (0, 0) to A1
    """
    x = xy[0]
    y = xy[1]
    letter_number = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"][x] + str(y + 1)

    return letter_number

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

def max_first_move(tiles):
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
                        score += SCORES[letter] * MULTIPLIERS_LETTER[7][i + k]
                    else:
                        tiles_remaining.remove(" ")
                score *= 2
                if score > max_score:
                    max_word = Move(word, "H" + str(i + 1), "D", score)
                    max_score = max_word.score
    
    return max_word