from tkinter import *
import pandas
import random

#------------------ CONSTANTS ---------------------#
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "Italian"
words_to_learn = []
current_card = {}

#------------------ GET WORDS ---------------------#
try:
    #Read data
    data = pandas.read_csv(f"data/{LANGUAGE}_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(f"data/{LANGUAGE.lower()}_words.csv")
    words_to_learn = data.to_dict(orient="records")
else:
    #Convert to list/dictionaries
    words_to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(language_on_card, text=LANGUAGE, fill="black")
    canvas.itemconfig(word_on_card, text=current_card[LANGUAGE], fill="black")
    canvas.itemconfig(card_canvas, image=front_img)
    timer = window.after(3000, func=flip_card)


def known_word():
    words_to_learn.remove(current_card)

    foreign_words = [dictionary[LANGUAGE] for dictionary in words_to_learn]
    english_words = [dictionary["English"] for dictionary in words_to_learn]

    # save words that still need learning
    data_dict = {
        LANGUAGE: foreign_words,
        "English": english_words
    }

    export_data = pandas.DataFrame(data_dict)
    export_data.to_csv(f"data/{LANGUAGE}_words_to_learn.csv", index=False)

    next_card()


def flip_card():
    canvas.itemconfig(language_on_card, text="English", fill="white")
    canvas.itemconfig(word_on_card, text=current_card["English"], fill="white")
    canvas.itemconfig(card_canvas, image=back_img)

#------------------ UI SETUP ---------------------#
window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

# Canvas/Image setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
card_canvas = canvas.create_image(400, 263, image=front_img)
language_on_card = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_on_card = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Back Image
back_img = PhotoImage(file="images/card_back.png")

#X Button
x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=next_card, bd=0)
x_button.grid(column=0, row=1)

#Check Button
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=known_word, bd=0)
check_button.grid(column=1, row=1)


next_card()

window.mainloop()

