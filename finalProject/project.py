stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r'''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''

word_list = [
    "alien", "amadeus", "amelie", "avatar", "avengers", "babel", "batman", "beloved",
    "benjamin", "big", "blow", "brave", "burn", "casablanca", "castaway", "catwoman",
    "chaplin", "cinderella", "clueless", "cobra", "colossus", "commando", "contact",
    "creed", "cube", "cyborg", "daredevil", "deadpool", "deliverance", "diamonds",
    "district", "django", "dracula", "dredd", "drive", "elf", "encanto", "eraser",
    "exodus", "fargo", "frozen", "gladiator", "gravity", "grease", "heat", "her",
    "hitch", "hollywood", "hook", "hugo", "inception", "independence", "interstellar",
    "jaws", "joker", "jurassic", "kickboxer", "kramer", "labyrinth", "legend", "leon",
    "logan", "lucy", "madagascar", "maleficent", "matrix", "memento", "mermaid", "metropolis",
    "moonlight", "napoleon", "notorious", "oceans", "panic", "patterson", "philadelphia",
    "predator", "prometheus", "pulp", "raging", "rambo", "rango", "rebecca", "revenant",
    "robocop", "rocky", "rushmore", "scarface", "serpico", "shrek", "sideways", "speed",
    "superman", "terminator", "thor", "titanic", "topgun", "transformers", "tremors",
    "twister", "unforgiven", "up", "vertigo","whiplash","zodiac"
]


import random



lives = 6

print(logo)

chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"It was {chosen_word}! YOU LOSE.")

    if "_" not in display:
        game_over = True
        print("YOU WIN.")

    print(stages[lives])
