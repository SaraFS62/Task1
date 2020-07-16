
import random
def Sentenceslist(Numberofsentences, wordlist, templatelist):
    lis = []
    x = min(Numberofsentences, len(wordlist) * len(templatelist))
    while x > len(lis): #none reptition sentences
        word = random.choice(wordlist)
        word = word.replace("\n", "")
        temp = random.choice(templatelist)
        temp = temp.replace("_", word)
        temp = temp.replace("\n", "")

        #print(temp)
        lis.append(temp)

        lis = list(dict.fromkeys(lis))

    return lis

Numberofsentences = 20

wordlist = open("Wordlist.rtf", "r")

templatelist = open("Templatelist.rtf", "r")

print(Sentenceslist(Numberofsentences, wordlist.readlines(), templatelist.readlines()))

wordlist.close()
templatelist.close()


