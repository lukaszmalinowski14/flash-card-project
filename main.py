from tkinter import *
import pandas as pd
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- PLIST OF WORDS ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/slownik_EN_10k.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = original_data.to_dict(orient="records")

#########


def next_card():
    global current_card, flip_timer
   # window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    print(current_card)
    # flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Polish", fill="white")
    canvas.itemconfig(card_word, text=current_card["Polish"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flip_timer = window.after(3000, func=flip_card)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
flip_img = PhotoImage(file="images/flip.png")

canvas = Canvas(width=800, height=526,  highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(
    400, 150, text="English", font=("aRIEL", 40, 'italic'))
card_word = canvas.create_text(
    400, 263, text="word", font=("aRIEL", 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
unknown_button = Button(image=wrong, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

reveal_button = Button(highlightthickness=0, command=flip_card)
reveal_button.grid(row=2, column=1)
next_card()


window.mainloop()
