import pytest
from project import stages, logo, word_list, choose_word, display_word, check_guess, update_stages

def test_stages_length():
    assert len(stages) == 7, "There should be 7 stages in the hangman game."

def test_logo():
    assert isinstance(logo, str), "Logo should be a string."

def test_word_list():
    assert len(word_list) > 0, "Word list should not be empty."
    assert all(isinstance(word, str) for word in word_list), "All words in the word list should be strings."

def test_word_list_content():
    for word in word_list:
        assert word.isalpha(), "Words in the word list should only contain alphabetic characters."

def test_choose_word():
    word = choose_word(word_list)
    assert word in word_list, "Chosen word should be from the word list."

def test_display_word():
    word = "hangman"
    guessed_letters = ["a", "n"]
    displayed = display_word(word, guessed_letters)
    assert displayed == "_ a n _ _ a n", "Displayed word should match the guessed letters."

def test_check_guess_correct():
    word = "hangman"
    guess = "a"
    result = check_guess(word, guess)
    assert result == True, "Guess should be correct."

def test_check_guess_incorrect():
    word = "hangman"
    guess = "z"
    result = check_guess(word, guess)
    assert result == False, "Guess should be incorrect."

def test_update_stages():
    initial_stage = stages[0]
    updated_stage = update_stages(1)
    assert updated_stage == stages[1], "Stage should update correctly after a wrong guess."
