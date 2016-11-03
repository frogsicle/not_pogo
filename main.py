#!/usr/bin/env python

from helpers import MarkovChain
FILE = "assets/t1.txt"
NUM=20
import os
import random
import time
from builtins import input

def main():
    mc = initialize(FILE)
    score = 0
    max_q = 10
    quotes = range(max_q)
    for iquote in quotes:
        right_or_not = present_questions(iquote, score, max_q, mc)
        if right_or_not:
            score += 1
    end_screen(score, max_q)

def end_screen(score, max_q):
    os.system("clear")
    print("Congratulations! You got {}% right".format(score / max_q * 100))
    print("""
     /    \\
    ||    ||
     <>  <>
        |
       ___
    """)

def get_quote(mc):
    status = random.choice([0, 1])
    if status == 1:
        quote = get_actual(NUM, FILE)
    else:
        quote = get_generated(NUM, mc)

    quote = list(quote)
    quote = "".join(quote)
    return quote, status

def present_questions(iquote, score, max_q, mc):
    os.system("clear")
    print("Quote {} of {}. \t Current score {}".format(iquote, max_q, score))
    print("Enter 'T' if you think a politician really said this, and 'F' if you think it's bogus\n")
    quote, veracity = get_quote(mc)
    print("".join(quote))
    answer = input()
    ret = interpret_answer(answer, veracity)
    for i in range(4):
        print('.')
        time.sleep(0.2)
    if ret:
        print('Correct.')
    else:
        print('Wrong.')
    print('\n press any key to continue' )
    input()
#    time.sleep(2)
    return ret

def interpret_answer(answer, veracity):
    if answer in ['T', 't', 'Y', 'y'] and veracity == 1:
        ret = True
    elif answer in ['F', 'f', 'N', 'n'] and veracity == 0:
        ret = True
    else:
        ret = False
    return ret

def a_quote(text = "somebody may have said this", veracity = True):
    return(text)


def initialize(file):
    with open(file,'r') as infile:
        txt = infile.read()

    mc = MarkovChain(corpus=txt, separator=" ")
    return mc

def get_actual(num_words, txtfile, separator=" "):
    with open(txtfile, 'r') as infile:
        fulltext = infile.read().split(separator)
        mx = len(fulltext) -1 -num_words
        start = random.randint(0,mx)
        res = separator.join(fulltext[start:start+num_words])
        yield res


def get_generated(num_words, mc, separator=" "):
    #iterator
    res = "".join(mc.printSth(maxItems=num_words))
    yield res

if __name__ == "__main__":
    main()



