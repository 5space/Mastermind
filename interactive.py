from tkinter import *
import random

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]


def get_hint(code, attempt, choices):
    correct = sum(1 for i in range(len(code)) if code[i] == attempt[i])
    wrong = sum(min(code.count(n), attempt.count(n)) for n in choices) - correct
    return correct, wrong


root = Tk()
root.title("Mastermind Game")
root.geometry("640x640+0+0")

heading = Label(root,
                text="WELCOME TO THE MASTERMIND GAME BY JASON AND HOLDEN",
                font=("arial", 20, "bold"),
                fg="steelblue").pack()

label1 = Label(root,
               text="Enter your color guesses: ",
               font=("arial", 20, "bold"),
               fg="black").pack()

guess1 = StringVar()
guess2 = StringVar()
guess3 = StringVar()
guess4 = StringVar()

m1 = OptionMenu(root, guess1, *colors)
m1.config(width=20)
m1.pack()
m2 = OptionMenu(root, guess2, *colors)
m2.config(width=20)
m2.pack()
m3 = OptionMenu(root, guess3, *colors)
m3.config(width=20)
m3.pack()
m4 = OptionMenu(root, guess4, *colors)
m4.config(width=20)
m4.pack()

generatedCode = [random.choice(colors), random.choice(colors), random.choice(colors), random.choice(colors)]
moves = 0

label2 = Label(root,
               text="Correct position: 0, Wrong position: 0",
               font=("arial", 15, "bold"),
               fg="black")
label2.pack()
label3 = Label(root,
               text="Turn number: " + str(moves),
               font=("arial", 15, "bold"),
               fg="black")
label3.pack()


def get_feedback():
    global moves
    guessed = [guess1.get(), guess2.get(), guess3.get(), guess4.get()]
    hint = get_hint(generatedCode, guessed, colors)
    label2.config(text=f"Correct position: {hint[0]}, Wrong position: {hint[1]}")

    moves += 1
    label3.config(text="Turn number: " + str(moves))


submit = Button(root, text="Submit", width=30, height=5, bg="lightblue", command=get_feedback).pack()

root.mainloop()
