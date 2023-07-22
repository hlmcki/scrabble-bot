from scrabble import *

# Prompt user for number of players
input_invalid = True
while input_invalid:
    players = input("Number of players: ")
    try:
        players = int(players)
        if players in [2, 3, 4]:
            input_invalid = False
        else:
            print("Number of players must be an integer between 2 and 4")
    except ValueError:
        print("Number of players must be an integer between 2 and 4")

# Prompt user for which player they are playing as
input_invalid = True
while input_invalid:
    player = input("Playing as Player: ")
    try:
        player = int(player)
        if player in range(1, players + 1):
            input_invalid = False
        else:
            if players == 2:
                print("Must play as Player 1 or 2")
            if players == 3:
                print("Must play as Player 1, 2 or 3")
            if players == 4:
                print("Must play as Player 1, 2, 3 or 4")
    except ValueError:
        if players == 2:
            print("Must play as Player 1 or 2")
        if players == 3:
            print("Must play as Player 1, 2 or 3")
        if players == 4:
            print("Must play as Player 1, 2, 3 or 4")       

# Create game
game = Scrabble(players=players)

# Run game
turn = 1
count = 1

while count < 4:
    # Print board
    game.print()

    # Print which player's turn it is
    print("\nTurn:\t\t\tPlayer", turn)

    # If it is the user's turn, prompt user for tiles and print AI suggestion
    if player == turn:
        input_invalid = True
        while input_invalid:
            input_invalid = False
            tiles = list((input("Tiles in hand:\t\t")).upper())

            # Check that the tiles only contain alphabetic characters
            for tile in tiles:
                if not tile.isalpha():
                    print("Invalid tiles - Tiles must contain only alphabetic characters")
                    input_invalid = True

            # Check that the user has provided between 1 and 7 tiles
            if len(tiles) < 1 or len(tiles) > 7:
                print("Invalid tiles - Number of tiles must be between 1 and 7")
                input_invalid = True

        # Print AI suggestion
        move = max_move(game.board, tiles)
        print("AI suggestion:\t\t" + move.word + ", " + move.start + ", " + move.direction + " (" + str(move.score) + " points" + ")")

    # Prompt user for word, start and direction
    input_invalid = True
    while input_invalid:
        input_invalid = False
        word = (input("Play word:\t\t")).upper()
        start = (input("Start:\t\t\t")).upper()
        direction = (input("Direction:\t\t")).upper()

        # Check inputs
        while True:

            # Check that word only contains alphabetic characters
            for letter in word:
                if not letter.isalpha():
                    print("Invalid word - Word must contain only alphabetic characters")
                    input_invalid = True
                    break

            # Check that word is between 2 and 15 letters long
            if len(word) < 2 or len(word) > 15:
                print("Invalid word - Word must be between 2 and 15 letters long")
                input_invalid = True
                break

            # Check that start is a valid square
            if start not in COORDINATES.keys():
                print("Invalid start - Start must be between A1 and O15")
                input_invalid = True
                break

            # Check that direction is either ACROSS (A) or DOWN (D)
            if direction not in ["A", "D"]:
                print("Invalid direction - Direction must be either ACROSS (A) or DOWN (D)")
                input_invalid = True
                break

            # Check that word will fit if played from start in direction
            if (COORDINATES[start][direction] + len(word) - 1) > 14:
                print("Invalid move - Word too long to be played in specified direction from start")
                input_invalid = True
                break

            break

    # Play word on board
    game.play_word(word, start, direction)

    # Update turn
    turn = (turn % players) + 1

    # Update count
    count += 1