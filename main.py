#!/usr/bin/env python

from helpers import MarkovChain
import random
FILE = "assets/t1.txt"


def main():
    mc = initialize(FILE)
    #for i in get_actual(20, FILE):
    #    print(i)



def initialize(file):
    with open(file,'r') as infile:
        txt = infile.read()

    mc = MarkovChain(corpus=txt, separator=" ")
    return mc

def get_actual(num_words, txtfile, separator=" "):
    with open(txtfile, 'r') as infile:
        fulltext = infile.read().split(separator)
        mx = len(fulltext) -1 -num_words
        while(1):
            start = random.randint(0,mx)
            res = " ".join(fulltext[start:start+num_words])
            yield res
    # iterator
    pass

def get_generated(num_words, mc):
    #iterator
    pass

if __name__ == "__main__":
    main()


