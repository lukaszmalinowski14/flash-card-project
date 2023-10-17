from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- PLIST OF WORDS ------------------------------- #

data = pd.read_csv("slownik_EN_10k.csv")
data_dict = data.to_dict(orient="records")

#########


def next_card():
    global data_dict
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")


canvas = Canvas(width=800, height=526,  highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(
    400, 150, text="English", font=("aRIEL", 40, 'italic'))
card_word = canvas.create_text(
    400, 263, text="word", font=("aRIEL", 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
unknown_button = Button(image=wrong, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)
next_card()

window.mainloop()
