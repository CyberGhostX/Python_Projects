#!/usr/bin/python3
#!bin/python3

import random

def printout(string):
    for char in string:
        l = len(char)
        new_str = ""
        for i in range(l):
            if i%2 == 0:
                new_str+=char[i]
            else:
                new_str+="_"
        return new_str

def answer(word):
    for w in word:
        chance = 5
        print(f"You will get {chance} chance to beat me")
        name = input("Enter your name : ")
        while chance > 0:
            guess = input("Enter your guess : ")
            if w == guess:
                return f"Congratulations {name}, you beat me"
            else:
                chance-=1
                if chance == 0:
                    return f"{chance} chance remaining, you lost {name}\nbetter luck next time\ncorrect answer is {w}"
                else:
                    print(f"Wrong, chance remaining {chance}")
        
def main(filename):
    with open(filename,"r") as file:
        lines = file.read().splitlines()
        word = [random.choice(lines)]
        print(f"This word you have to guess : {printout(word)}")
        return (answer(word))

print(main("word_list.txt"))