import random
import sys
from termcolor import colored
with open('words.txt', 'r') as f:
    words = f.read().split()

class Game:
    def __init__(self, words):
        self.possWords = words
        self.target = random.choice(words)
        self.numGuesses = 1
    def nextWord(self):
        self.numGuesses -= 1
        word = input().strip().lower()
        while (not (word in self.possWords)) and len(word) == 5:
            word = input().strip().lower()
        if word == self.target:
            print(colored(word, '\u001b[32m'))
        else:
            rightList = []
            for i in range(5):
                if word[i] == self.target[i]:
                    rightList.append('\u001b[32m')
                elif word[i] in self.target:
                    rightList.append('\u001b[33m')
                else:
                    rightList.append('\u001b[31m')
            print(rightList[0]+word[0]+rightList[1]+word[1]+rightList[2]+word[2]+rightList[3]+word[3]+rightList[4]+word[4])
        if self.numGuesses > 0:
            self.nextWord()


def main():
    while True:
        game = Game(words)
        game.nextWord()
        print('\n')

main()