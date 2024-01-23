import random

print("Welcome to the zoo! Let's play hangman!")

# List of animals
animals_list = ["Lion", "Tiger", "Bear", "Elephant", "Giraffe", "Hippopotamus", "Zebra", "Kangaroo",
    "Panda", "Koala", "Gorilla", "Cheetah", "Penguin", "Dolphin", "Cobra", "Rhino",
    "Polar Bear", "Jaguar", "Leopard", "Ostrich", "Peacock", "Platypus", "Giraffe",
    "Penguin", "Dolphin", "Cobra", "Rhino", "Polar Bear", "Jaguar", "Leopard", "Ostrich",
    "Peacock", "Platypus", "Monkey", "Horse", "Dog", "Cat", "Bird", "Fish", "Snake",
    "Frog", "Spider", "Butterfly", "Eagle", "Koala", "Penguin", "Owl", "Raccoon",
    "Squirrel", "Hamster"]

# Select a random animal from the list
chosen_word = random.choice(animals_list).lower()  # Convert to lowercase
lives = 6

print(f"Hint: The solution is {chosen_word}.")

# Initialize display with underscores
display = ["_" for _ in chosen_word]
print(display)

# Hangman stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()  # Convert to lowercase

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
