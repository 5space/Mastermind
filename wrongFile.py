#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


root = Tk()
root.title("Mastermind Game")
root.geometry("640x640+0+0")

heading = Label(root, text="WELCOME TO THE MASTERMIND GAME BY JASON AND HOLDEN", font=("arial",20,"bold"), fg="steelblue").pack()

label1 = Label(root, text="Enter your color guesses: ", font=("arial",20,"bold"),fg="black").place(x=10, y=200)

guess1 = StringVar()
guess2 = StringVar()
guess3 = StringVar()
guess4 = StringVar()

entry_box = Entry(root, textvariable=guess1, width=25, bg="lightgreen").place(x=280,y=210)
entry_box = Entry(root, textvariable=guess2, width=25, bg="lightgreen").place(x=280,y=230)
entry_box = Entry(root, textvariable=guess3, width=25, bg="lightgreen").place(x=280,y=250)
entry_box = Entry(root, textvariable=guess4, width=25, bg="lightgreen").place(x=280,y=270)


def do_it():
    print("Your guesses were: " + guess1.get(), guess2.get(), guess3.get(), guess4.get())
    
printGuesses = Button(root, text="Print your guesses", width=30, height=5, bg="lightblue", command=do_it).place(x=250, y=300)


root.mainloop()


# In[3]:


#generating the code 
import random
list  = ["Red","Orange","Yellow","Green","Blue","Violet"]
#print("random.choice() to select random item from list - ", random.choice(list))
#print("\nrandom.choice() to select random item from list - ", random.choice(list))


computerGeneratedCode = [random.choice(list),random.choice(list),random.choice(list),random.choice(list)]
print(computerGeneratedCode)


# In[4]:



guessCode = ["red", "red", "red", "red"]
computerGeneratedCode = ["red", "green", "violet", "yellow"]

def describe(aList):
    correctWithPos = 0 #Number of colors right where the position matches as well 
    for i in range(0,4):
        if guessCode[i] == computerGeneratedCode[i]:
            correctWithPos = correctWithPos + 1
    print(correctWithPos)
    
    
    
    correctWithoutPos = 0 #Number of colors right where the position doesn't matter
    for i in range(0,4):
        for k in range (0,4):
            if guessCode[i] == computerGeneratedCode[k]:
                correctWithoutPos = correctWithoutPos + 1
                
    print(correctWithoutPos) 
    
                
    repeatedGuess = 0 #Number of repeated colors in the list guessCode
    for i in range(0,4):
        for k in range (0,4):
            if guessCode[i] == guessCode[k]:
                repeatedGuess = repeatedGuess + 1
                
    repeatedGuess = repeatedGuess - 4 #since each color matches itself once, for a total of 4 times
    if repeatedGuess==0:
        actualRepeatedGuess=0
    elif repeatedGuess==2:
        actualRepeatedGuess=1
    elif repeatedGuess==4:
        actualRepeatedGuess=2
    elif repeatedGuess==6:
        actualRepeatedGuess=2
    elif repeatedGuess==12:
        actualRepeatedGuess=3
        
    print("The number of repeated colors in the guess code is " + str(actualRepeatedGuess))
   
    
    repeatedComputer = 0 #Number of repeated colors in the list guessCode
    for i in range(0,4):
        for k in range (0,4):
            if computerGeneratedCode[i] == computerGeneratedCode[k]:
                repeatedComputer = repeatedComputer + 1
    
    repeatedComputer = repeatedComputer - 4 #since each color matches itself once, for a total of 4 times
    
    if repeatedComputer==0:
        actualRepeatedComputer=0
    elif repeatedComputer==2:
        actualRepeatedComputer=1
    elif repeatedComputer==4:
        actualRepeatedComputer = 2
    elif repeatedComputer==6:
        actualRepeatedComputer=2
    elif repeatedComputer==12:
        actualRepeatedComputer=3
    
    print("The number of repeated colors in the computer code is " + str(actualRepeatedComputer))
      
    actualCorrectWithoutPos = correctWithoutPos - actualRepeatedGuess - actualRepeatedComputer
    
    print(actualCorrectWithoutPos)
    
describe(guessCode)


# In[5]:


#Dennis's suggestions 

P = ["12398", "5", "4", "4"]
C = ["5", "3", "0", "4"]

right=0
rightPos=0

for x in P:
    if x in C:
        right=right+1
        
for i in range(0,4):
    if P[i] == C[i]:
        rightPos = rightPos + 1
    

        #print("Player index is " + str(P.index(x)))
        #print("Computer index is " + str(C.index(x)))
        #if P.index(x)==C.index(x):
            #print(P.index(x))
            #rightPos = rightPos+1
    

#Count the number of duplicates in P
duplicates=0
duplicates1=0
for x in P:
    if x in C:
        a = P.count(x) - 1
        duplicates1 = duplicates1 + a #We only care about the duplicates which are found in the computer code
        #because those alter the numebr of "total guesses right "
if duplicates1==0:
    duplicates=0
elif duplicates1==2:
    duplicates=1
elif duplicates1==4:
    duplicates=2
elif duplicates1==6:
    duplicates=2
elif duplicates1==12:
    duplicates=3
print("The number of important duplicates in the guess code is " + str(duplicates))
    
right = right - duplicates
print("The number of total guesses right is " + str(right))
print("The number of guesses right in the right position is " + str(rightPos))
print("The number of guesses right in the wrong position is " + str(right-rightPos))


# In[6]:


def getFeedback(C, P):

    right=0
    rightPos=0

    for x in P:
        if x in C:
            right=right+1

    for i in range(0,4):
        if P[i] == C[i]:
            rightPos = rightPos + 1


            #print("Player index is " + str(P.index(x)))
            #print("Computer index is " + str(C.index(x)))
            #if P.index(x)==C.index(x):
                #print(P.index(x))
                #rightPos = rightPos+1


    #Count the number of duplicates in P
    duplicates=0
    duplicates1=0
    for x in P:
        if x in C:
            a = P.count(x) - 1
            duplicates1 = duplicates1 + a #We only care about the duplicates which are found in the computer code
            #because those alter the numebr of "total guesses right "
    if duplicates1==0:
        duplicates=0
    elif duplicates1==2:
        duplicates=1
    elif duplicates1==4:
        duplicates=2
    elif duplicates1==6:
        duplicates=2
    elif duplicates1==12:
        duplicates=3
    print("The number of important duplicates in the guess code is " + str(duplicates))

    right = right - duplicates
    print("The number of total guesses right is " + str(right))
    print("The number of guesses right in the right position is " + str(rightPos))
    print("The number of guesses right in the wrong position is " + str(right-rightPos))
    
getFeedback(["blue", "blue", "green", "red"],["1","2","3","green"])


# In[ ]:


root = Tk()
root.title("Mastermind Game")
root.geometry("640x640+0+0")

heading = Label(root, text="WELCOME TO THE MASTERMIND GAME BY JASON AND HOLDEN", font=("arial",20,"bold"), fg="steelblue").pack()

label1 = Label(root, text="Enter your color guesses: ", font=("arial",20,"bold"),fg="black").place(x=10, y=200)

guess1 = StringVar()
guess2 = StringVar()
guess3 = StringVar()
guess4 = StringVar()

entry_box = Entry(root, textvariable=guess1, width=25, bg="lightgreen").place(x=280,y=210)
entry_box = Entry(root, textvariable=guess2, width=25, bg="lightgreen").place(x=280,y=230)
entry_box = Entry(root, textvariable=guess3, width=25, bg="lightgreen").place(x=280,y=250)
entry_box = Entry(root, textvariable=guess4, width=25, bg="lightgreen").place(x=280,y=270)


def print_it():
    print("Your guesses were: " + guess1.get(), guess2.get(), guess3.get(), guess4.get())
    
printGuesses = Button(root, text="Print your guesses", width=30, height=5, bg="lightblue", command=print_it).place(x=250, y=300)


#generating the code -----------------------------------------------------------------------------------
import random
colorList  = ["Red","Orange","Yellow","Green","Blue","Violet"]


generatedCode = [random.choice(list),random.choice(list),random.choice(list),random.choice(list)]
#Computer generated random list

print(generatedCode)
#generating the code ------------------------------------------------------------------------------------

label1 = Label(root, text="The computer generated code is " + str(generatedCode), font=("arial",15,"bold"),fg="black").place(x=10, y=500)

D=[str(guess1),str(guess2),str(guess3),str(guess4)]

def getFeedback1():
    P=generatedCode
    getFeedback(D,generatedCode)

print(generatedCode)
print(D)

feedback = Button(root, text="Get feedback", width=30, height=5, bg="lightblue", command=getFeedback1).place(x=250, y=400)

root.mainloop()


# In[ ]:




