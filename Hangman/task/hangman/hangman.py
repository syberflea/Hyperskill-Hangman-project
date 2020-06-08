from random import choice
from string import ascii_lowercase

languages = ['python', 'java', 'kotlin', 'javascript']
language = choice(languages)
answer = list("-" * len(language))
history = set()
letters = set(language)
guess_letters = set(language)
guessed_letters = set()


def run():
    tries = 8
    print("H A N G M A N")
    while tries > 0:
        if guess_letters == guessed_letters:
            print("You guessed the word!")
            break

        print("")
        print(''.join(answer))
        char = input("Input a letter: ")

        if char in guess_letters and char not in guessed_letters:
            guessed_letters.add(char)
            history.add(char)
        elif len(char) > 1:
            print("You should input a single letter")
        elif char not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif char in history:
            # tries -= 1
            print("You already typed this letter ")
        else:
            tries -= 1
            history.add(char)
            print("No such letter in the word")

        for i in range(len(language)):
            if char == language[i]:
                answer[i] = char

        if '-' not in answer:
            print("You survived!")
            break
    else:
        if tries == 0:
            print("You are hanged!")


while True:
    menu_item = input('Type "play" to play the game, "exit" to quit:')
    if menu_item == "play":
        run()
    elif menu_item == "exit":
        break
