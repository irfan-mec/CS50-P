# Hangman Game
# Video url : https://youtube.com/404-not-found-error

## Description
This is a simple Hangman game implemented in Python. The game randomly selects a word from a predefined list of movie titles, and the player has to guess the word one letter at a time. The game provides visual feedback on the progress and the number of incorrect guesses.

## Method of Playing
1. Run the script to start the game.
2. The game will display a series of underscores representing the letters in the word.
3. Guess a letter by typing it and pressing Enter.
4. If the letter is in the word, it will be revealed in the correct position(s).
5. If the letter is not in the word, you lose a life and a part of the hangman is drawn.
6. The game continues until you guess the word or run out of lives.

## Concepts Used
- **Python Basics**: Variables, loops, conditionals, and functions.
- **String Manipulation**: Handling and modifying strings to display the word and guessed letters.
- **Lists**: Managing the list of words and the stages of the hangman drawing.
- **Random Module**: Selecting a random word from the list.
- **User Input**: Capturing and processing user input.
- **ASCII Art**: Creating visual stages of the hangman.

## Requirements
- Python 3.x

## Running the Game
To run the game, execute the following command in your terminal:

```bash
python hangman.py
