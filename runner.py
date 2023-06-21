from scrabble import *

# Prompt user for number of players
players = int(input("Number of players: "))

# Create game and AI agent
game = Scrabble(players=players)
ai = ScrabbleAI()

# Run game
count = 0
while count < 10:
    game.print()
    print("Turn:          Player", game.turn)
    print("Score:        ", str(game.scores[game.turn]), "points")
    print("Hand:         ", game.hands[game.turn])
    points_max = 100
    word_max = "FOOBAR"
    start_max = "H8"
    direction_max = "D"
    print("AI suggestion: " + "(" + str(points_max) + " points) " + word_max + ", " + start_max + ", " + direction_max)
    word = input("Word:          ")
    start = (input("Start:         "))
    direction = input("Direction:     ")
    game.play_word(word, start, direction)
    game.draw_tiles()
    count += 1