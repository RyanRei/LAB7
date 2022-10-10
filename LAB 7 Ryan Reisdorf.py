#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PART 1
import random
def nouns():
    fileOpen=open('nouns.txt','r')
    Lyst=[]
    for line in fileOpen:
        words=line.split()
        Lyst.append(words)
    fileOpen.close()
    return tuple (random.choice(Lyst))

def verbs():
    fileOpen=open('nouns.txt','r')
    Lyst=[]
    for line in fileOpen:
        words=line.split()
        Lyst.append(words)
    fileOpen.close()
    return tuple (random.choice(Lyst))

def articles():
    fileOpen=open('nouns.txt','r')
    Lyst=[]
    for line in fileOpen:
        words=line.split()
        Lyst.append(words)
    fileOpen.close()
    return tuple (random.choice(Lyst))

def prepositions():
    fileOpen=open('nouns.txt','r')
    Lyst=[]
    for line in fileOpen:
        words=line.split()
        Lyst.append(words)
    fileOpen.close()
    return tuple (random.choice(Lyst))

def main():
    sentence=articles+noun+verb+prepositions
    print(sentence)
if __name__=='__main__':
    main()


# In[ ]:


#PART 2
import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours",
                "you":"I", "your":"my", "yours":"mine"} 

def reply(sentence):
    """Implements two different reply strategies."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords) 

def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    count=0
    Lyst=[]
    while True:
        sentence = input("\n>> ")
        Lyst.append(sentence)
        if count%2:
            print('Earlier you said that',random.choice(Lyst))
        elif sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))
        count+=1


# In[ ]:


#PART 3
import string
inFile=input("Enter the input file name: ")
openInFile=open(inFile,'r')
words=[]
for line in openInFile:
    for word in line.split():
        words.append(word.lower())
words.sort()        
dictionary={}
for word in words:
    number=dictionary.get(word, None)
    if number== None:
        dictionary[word]=1
    else:dictionary[word]=number+1


maximum=max(dictionary.values())
for key in dictionary:
    if dictionary[key]==maximum:
        print(dictionary,key)
        break

