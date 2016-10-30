import os
import random

def main():
    score = 0
    max_q = 10
    quotes = range(max_q)
    for quote in quotes:
        right_or_not = present_questions(quote, score, max_q)
        if right_or_not:
            score += 1
    end_screen(score, max_q)

def end_screen(score, max_q):
    os.system("clear")
    print("Congratulations! You can tell the difference politicians\n and computers {}% of the time".format(score / max_q * 100))

def get_actual():
    return a_quote()

def get_generated():
    return a_quote().replace('may have', 'may not have')

def get_quote():
    status = random.choice([0, 1])
    if status == 1:
        quote = get_actual()
    else:
        quote = get_generated()
    return quote, status

def present_questions(quote, score, max_q):
    os.system("clear")
    print("Quote {} of {}. \t Current score {}".format(quote, max_q, score))
    print("Enter 'T' if you think a politician really said this, and 'F' if you think it's bogus\n")
    quote, veracity = get_quote()
    print('"' + quote + '"\n')
    answer = input()
    ret = interpret_answer(answer, veracity)
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

if __name__ == "__main__":
    main()