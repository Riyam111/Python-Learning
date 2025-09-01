import math
import random
def jumble_word(word):
    word_letters=list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def guess_movie():
    characters=["ironman","elsa","moana","harry"]
    original=random.choice(characters)
    jumbled=jumble_word(original)
    print("guess the movie name",jumbled)
    guess=input("your guess: ")
    if guess.lower()==original.lower():
        print("correct")
    else:
        print("oops! wrong guess", original)

guess_movie()