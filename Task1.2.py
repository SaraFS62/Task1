#Task1.2
#Numberofsentences = 3

import random

for Numberofsentences in range(2):
    Wordlist = ["Ali", "Ahmed"]
    Templatelist = random.choice(Wordlist)
    Templatelist2 = random.choice(Wordlist)

if Templatelist != Templatelist2:
    print("Who is " + Templatelist + "?" + " I am " + Templatelist2 + ". " + "Where is " +Templatelist + "?")

