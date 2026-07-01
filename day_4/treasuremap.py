

#Treasure map Game
line = "Welcome to Treasure Island. Your mission is to find the treasure."
print(line)

line1=["*","*","*"]
line2=["*","*","*"]
line3=["*","*","*"]

map = [line1, line2, line3]
position = input("Where do you want to put the treasure? ")
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")



#find treasure game
guess1=input("guess the position of the treasure: ")
guess1_letter = guess1[0].lower()
guess1_number = int(guess1[1]) - 1
if guess1_letter == letter and guess1_number == number_index:
    print("You found the treasure!")
else:
    print("Sorry, you didn't find the treasure. TRY AGAIN!")
