# a program that lets the user play a virtual game of blackjack using randomized card values

import random

cards = ['Ace of Hearts','King of Hearts','Queen of Hearts',\
    'Jack of Hearts','Ten of Hearts','Nine of Hearts','Eight of Hearts',\
         'Seven of Hearts','Six of Hearts','Five of Hearts','Four of Hearts',\
         'Three of Hearts','Two of Hearts']

values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

num1 = random.randint(0,len(cards)-1)
card1 = cards[num1]
value1 = values[num1]

del cards[num1]
del values[num1]

num2 = random.randint(0,len(cards)-1)
card2 = cards[num2]
value2 = values[num2]

del cards[num2]
del values[num2]

points = value1 + value2

print("Your deal ("+ str(points) + "):")
print("- " + card1)
print("- " + card2)

while points < 21:
    hit = input("(H)it?")
    if hit.lower() == "h":
        num3 = random.randint(0,len(cards)-1)
        card3 = cards[num3]
        value3 = values[num3]

        points += value3

        print("Your deal ("+ str(points) + "):")
        print("- " + card3)

        del cards[num3]
        del values[num3]
        
    else:
        print("Sorry, you have to hit. >:)")
        

if points == 21:
    print("Blackjack!")
else:
    print("Bust!")
















