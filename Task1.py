

import random
def Sentenceslist(Numberofsentences, wordlist, templatelist):
    i = 0
    while i < Numberofsentences:
        if templatelist not in wordlist:
            print(templatelist)
        i += 1

Numberofsentences = random.randint(1,10)

wordlist = open("Wordlist.rtf", "r")
word = random.choice(wordlist.readlines())
wordlist.close()

templatelist = open("Templatelist.rtf", "r")
temp = random.choice(templatelist.readlines())
temp = temp.replace("_", word)
templatelist.close()

Sentenceslist(Numberofsentences, word, temp)



