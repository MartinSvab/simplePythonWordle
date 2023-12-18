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
    for letterInGuess in guess:
        if letterInGuess in word:
            for index, val in enumerate(word):
                if (val == letterInGuess):
                    correctlyGuessed[index] = letterInGuess
        else:
            print(letterInGuess + " is not in the word!")
    cls()
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


# Getting data from internet, starting game

data = startGame()

# main cycle

while True:
    printSpaces(2)
    word = random.choice(data)
    correctlyGuessed = []

    for letter in word:
        print("_", end=" ")
        correctlyGuessed.append("_")

    print("\nGuess!")

    while True:
        guess = getGuess()

        if guess == word:
            print("Correct!")
            printSpaces(3)
            break

        else:
            guessWrong(guess, word, correctlyGuessed)

        if "_" not in correctlyGuessed:
            print("\n\nYOU WIN")
