import copy

TILES = list("AAAAAAAAABBCCDDDDEEEEEEEEEEEEFFGGHHIIIIIIIIIJKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYYZ")

with open("dictionary-raw.txt", "r") as file:
    words = file.read()
    words = words.split("\n")

output = []
for word in words:
    tiles_remaining = copy.deepcopy(TILES)
    blanks_used = 0
    if len(word) <= 15:
        for i in range(len(word)):
            letter = word[i].upper()
            if not letter.isalpha():
                break
            if letter in tiles_remaining:
                tiles_remaining.remove(letter)
            else:
                blanks_used += 1
                if blanks_used > 2:
                    break
            if i == len(word) - 1:
                output.append(word.upper())
            

with open("dictionary.txt", "w") as file:
    for i in range(len(output)):
        word = output[i]
        if i == len(output) - 1:
            file.write(word)
        else:
            file.write(word + "\n")            