

import random
def Sentenceslist(Numberofsentences, wordlist, templatelist):
    i = 0
    tab = []
    while i < Numberofsentences:
        if templatelist not in tab:
            tab.append(templatelist)
            print(tab)
           # print(templatelist) // there will be repetition
        i += 1

Numberofsentences = random.randrange(1, 10)

wordlist = open("Wordlist.rtf", "r")
word = random.choices(wordlist.readlines())
wordlist.close()

templatelist = open("Templatelist.rtf", "r")
temp = random.choices(templatelist.readlines())
temp.extend(word)
templatelist.close()

Sentenceslist(Numberofsentences, word, temp)



