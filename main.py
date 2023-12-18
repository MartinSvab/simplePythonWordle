from urllib.request import urlopen
import random
import os
import time
import json


# Other functions
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def startGame():
    print("Fetching words...")
    data = getDataFromWeb('https://random-word-api.herokuapp.com/all?lang=en')
    data.pop(0)
    data.pop(len(data) - 1)
    print("Words fetched successfully!\nStarting game!")
    time.sleep(0.5)
    cls()
    return data


# Functions used in main cycle

def guessWrong(guess, word, correctlyGuessed):
    cls()
    for letterInGuess in guess:
        if letterInGuess in word:
            for index, val in enumerate(word):
                if (val == letterInGuess):
                    correctlyGuessed[index] = letterInGuess
        else:
            print(letterInGuess + " is not in the word!")
    printSpaces(2)
    for letter in correctlyGuessed: print(letter, end=" ")


def getGuess():
    while (True):
        guess = input()
        if guess in data:
            return guess
        else:
            printSpaces(2)
            print("This word is not in the list. Try again")


def getDataFromWeb(url):
    response = urlopen(url)
    return response.read().decode('utf-8').split("\",\"")


def printSpaces(numberOfSpaces):
    for i in range(numberOfSpaces):
        print(" ")


def endGame(word):
    cls()
    print("Congrats! The word was " + word + "!")
    printSpaces(1)
    print("It took you " + str(guesses) + " guesses!")
    printSpaces(3)
    findInDictionary(word)
    printSpaces(3)
    print("Would you like to play again?")
    if input("Press any key to play again, type exit to quit").lower() == "exit":
        return False
    else:
        return True

def findInDictionary(word):
    dictionary = getDataFromWeb("https://api.dictionaryapi.dev/api/v2/entries/en/hello")

    if isinstance(dictionary, list) and dictionary:
        search_string = "abreacted"

        try:
            index = [entry.get("word", "").lower() for entry in dictionary].index(search_string.lower())
            print(f"Index of '{search_string}': {index}")
        except ValueError:
            print(f"'{search_string}' not found in the list.")
    else:
        print("Invalid or empty data returned by the API.")


# Getting data from internet, starting game

data = startGame()

# main cycle

while True:
    word = random.choice(data)
    correctlyGuessed = []
    guesses = 0

    for letter in word:
        print("_", end=" ")
        correctlyGuessed.append("_")

    print("\nGuess!")

    while True:
        guess = getGuess(guesses)
        guesses + 1

        if guess == word:
            break
        else:
            guessWrong(guess, word, correctlyGuessed)

        if "_" not in correctlyGuessed:
            break

    if not endGame(word): break
    cls()