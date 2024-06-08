from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk  # Make sure to install the Pillow library for image handling
import random

class Achal:
    def __init__(self):
        self.user1 = 0
        self.computer = 0
        self.round_count = 0
        self.result_text = ""

        window = tk.Tk()
        window.geometry("650x620")
        window.title("Stone_Paper_Scissor")

        # Load the background image
        background_image = Image.open("images/kig.webp")
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = Label(window, image=background_photo)
        background_label.place(relwidth=1, relheight=1)

        Label1 = Label(window, text="Welcome to the 'Stone' 'Paper' 'Scissor' Game",bg="sky blue", fg="red", font="Arial 18")
        Label1.place(x=70, y=30)

        Label11 = Label(window, text="'5 Rounds to play'  You have Choices:",bg="sky blue", fg="green", font="arial 16")
        Label11.place(x=140, y=70)

        Label12 = Label(window, text="Stone:0",bg="sky blue", fg="green", font="arial 14")
        Label12.place(x=310, y=110)

        Label13 = Label(window, text="Paper:1",bg="sky blue",  fg="green", font="arial 14")
        Label13.place(x=310, y=140)

        Label14 = Label(window, text="Scissor:2",bg="sky blue",  fg="green", font="arial 14")
        Label14.place(x=310, y=170)
        
        Label15 = Label(window, text="Enter your choice:",bg="sky blue",fg="black", font="Arial 12")
        Label15.place(x=220, y=210)
        
        self.user_entry = Entry(window)
        self.user_entry.place(x=355, y=211)

        self.result_label = Label(window, height=20, width=50, fg="black")
        self.result_label.place(x=140, y=280)

        button = Button(window, text="Play", bg="purple", fg="yellow", font="Arial 10", command=self.play_round)
        button.place(x=330, y=245)

        window.mainloop()

    def play_round(self):
        try:
            user = int(self.user_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid input, please enter a valid choice.")
            return

        if user < 0 or user > 2:
            self.result_label.config(text="Invalid choice, please enter a valid choice.")
            return

        computer_choice = random.randint(0, 2)
        self.result_text += f"\nRound {self.round_count + 1}: You chose {user}, Computer chose {computer_choice}\n"

        if user == computer_choice:
            self.result_text += "It's a tie.\n"
        elif (user == 0 and computer_choice == 2) or (user == 1 and computer_choice == 0) or (user == 2 and computer_choice == 1):
            self.result_text += "You win.\n"
            self.user1 += 1
        else:
            self.result_text += "Computer wins.\n"
            self.computer += 1

        self.round_count += 1

        if self.round_count == 5:
            self.result_text += f"\nFinal Scores:\nUser: {self.user1}  Computer: {self.computer}\n"
            if self.computer > self.user1:
                self.result_text += f"Computer wins by {self.computer} points."
            elif self.user1 > self.computer:
                self.result_text += f"User wins by {self.user1} points."
            else:
                self.result_text += "The match is a tie between computer and user."

            self.result_label.config(text=self.result_text)
            self.round_count = 0
            self.user1 = 0
            self.computer = 0
            self.user_entry.delete(0, END)  # Clear the Entry widget for the next game
            self.result_text = ""
        else:
            self.result_label.config(text=self.result_text + "Enter your choice for the next round:")

obj = Achal()
