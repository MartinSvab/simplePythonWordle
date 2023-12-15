from urllib.request import urlopen
import random


def getDataFromWeb(url):
    response = urlopen(url)
    return response.read().decode('utf-8').splitlines()


data = getDataFromWeb('https://www.mit.edu/~ecprice/wordlist.10000')


def guessWrong(guess, word, correctlyGuessed):
    for letterInGuess in guess:
        if letterInGuess in word:
            for index, val in enumerate(word):
                if(val == letterInGuess):
                    correctlyGuessed[index] = letterInGuess
        else:
            print(letterInGuess + " is not in the word!")
    for letter in correctlyGuessed: print(letter, end=" ")


def getGuess(data):
    while(True):
        guess = input()
        if guess in data:
            return guess
        else: print("This word is not in the list. Try again")





while(True):
    word = random.choice(data)
    correctlyGuessed = []

    for letter in word:
        print("_", end=" ")
        correctlyGuessed.append("_")

    print("\nGuess!")

    while(True):
        guess = getGuess(data)

        if(guess == word):
            print("Correct!")
            break

        else: guessWrong(guess, word, correctlyGuessed)

        if "_" not in correctlyGuessed:
            print("\n\nYOU WIN")
