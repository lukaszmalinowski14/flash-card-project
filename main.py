from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


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
canvas.create_text(400, 150, text="Title", font=("aRIEL", 40, 'italic'))
canvas.create_text(400, 263, text="word", font=("aRIEL", 60, 'bold'))
canvas.grid(column=0, row=0)

# # LABELS
# website_label = Label(text="Website:")
# website_label.grid(column=0, row=1)

# email_label = Label(text="Email/Username:")
# email_label.grid(column=0, row=2)

# password_label = Label(text="Password:")
# password_label.grid(column=0, row=3)

# # ENTRY
# website_entry = Entry(width=21)
# website_entry.grid(column=1, row=1)
# website_entry.focus()

# email_entry = Entry(width=35)
# email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "lukaszmalinowski14@gmail.com")

# password_entry = Entry(width=21)
# password_entry.grid(column=1, row=3)

# BUTTONSs
# password_gen_button = Button(text="Generate Password", command=get_password)
# password_gen_button.grid(column=2, row=3)

# add_button = Button(text="Add", width=29, command=save)
# add_button.grid(column=1, row=4, columnspan=2)

# search_button = Button(text="Search", command=find_password, width=13)
# search_button.grid(column=2, row=1)


window.mainloop()
