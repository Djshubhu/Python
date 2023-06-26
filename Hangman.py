import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():

    word = get_valid_word(words)
    word_lettrs = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_lettrs) > 0:

        print('You have used this letters : ', ' '.join(used_letters))
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current Word : ', ' '.join(word_list))

        user_letters = input('Guess a letter: ').upper()
        Guess = len(used_letters)
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_lettrs:
                word_lettrs.remove(user_letters)

        elif user_letters in used_letters:
            print('You have alreday used the character. Please try again...')
        else:
            print('Invalid Character .Please try again.')
    if True:
        print(
            f'Congratulation You have Find it Word Correctly .The Word is {word} in Guess {Guess} ')


print(' #### Welcome To Hangman Game #### ')
hangman()
