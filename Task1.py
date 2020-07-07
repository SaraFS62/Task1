
#Sentenceslist(List of String)
#from docx import Document

import random
def Sentenceslist(Numberofsentences, wordlist, templatelist):
    wordlist = open("Wordlist.rtf", "r")
    templatelist = open("templatelist.rtf", "r")
    Numberofsentences = [1,2,3]
    print(random.choices(Numberofsentences) + random.choices(templatelist.readlines()) + random.choices(wordlist.readlines()))

Sentenceslist(" ", "wordlist.rtf", "templatelist.rtf")



