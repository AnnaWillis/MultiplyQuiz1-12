__author__ = 'Anna'
import random


print("Hello, operators!")
print("I will ask you a 1-12 multiplication problem. If you get it right, I will say, 'Correct!'")


while True:

    factor1 = random.randint(1, 12)
    factor2 = random.randint(1, 12)

    guess = ""
    while guess=="":
        guess = input("What is %d times %d?" % (factor1 , factor2))
        if guess=="":
            print("That is not a number, silly! Try again and do your best!")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a number. Otherwise, the Ghost of Unanswered Multiplication Problems will haunt you.")
            guess = ""



    #print(guess)
    product = factor1 * factor2
    if guess ==  product:
        print("Correct!")
    else:
        print("Sorry, the correct answer is %d" % (product))









