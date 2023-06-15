from scrabble import *

# Prompt user for number of players
players = int(input("Number of players: "))

# Create game and AI agent
game = Scrabble(players=players)
ai = ScrabbleAI()

# Run game
count = 0
while count < 3:
    game.print()
    print("Turn:      Player", game.turn)
    print("Hand:     ", game.hands[game.turn])
    word = input("Word:      ")
    start = (input("Start:     "))
    direction = input("Direction: ")
    game.play_word(word, start, direction)
    game.draw_tiles()
    count += 1