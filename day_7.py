
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |

=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |

=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |

=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |

=========
''', '''
  +---+
  |   |
  O   |
      |
      |

=========
''', '''
  +---+
  |   |
      |
      |
      |

=========
''']

end_of_game = False

word_list = ["aardvark", "baboon", "camel"]
choose_word = random.choice(word_list)
word_length = len(choose_word)
lives = 6

print(f"Pssst, the solution is {choose_word}.")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = choose_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in choose_word:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The word was: {choose_word}")

    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")
