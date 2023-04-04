from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# --------------------  READ DATA -------------------- #

words = pandas.read_csv("data/french_words.csv")
df = pandas.DataFrame(words)
dictionary_words = df.to_dict(orient="records")
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

messagebox.showinfo(title="French to English", message="Press the green button if you know the word, \n"
                                                       "if you don't wait 3 seconds\n"
                                                       "for translation, then press the red button")

# --------------------  UI PART 1 -------------------- #

flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
flashcard = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = flashcard.create_image(400, 263, image=flashcard_front)
language = flashcard.create_text(400, 150, text="Language", font=("Arial", 30, "italic"))
word = flashcard.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
flashcard.grid(column=0, row=0, columnspan=2)
english_word = ""


# -------------------- GREEN BUTTON  ------------------- #
# DELETE THE WORD IF USER KNOWS IT , REFRESH THE LIST #
def green_button():
    global english_word
    global flip_timer
    global df
    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary_words)
    french_word = current_card["French"]
    english_word = current_card["English"]
    flashcard.itemconfig(image, image=flashcard_front)
    flashcard.itemconfig(language, text="French", fill="black")
    flashcard.itemconfig(word, text=f"{french_word}", fill="black")
    df = df[df["French"].str.contains(french_word) == False]
    df.to_csv("data/french_words.csv", encoding='utf-8', index=False)
    flip_timer = window.after(3000, func=translation)


# -------------------- LEFT BUTTON ------------------- #
# SAME AS RIGHT BUTTON BUT DOES NOT DELETE WORD #
def red_button():
    global english_word
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary_words)
    french_word = current_card["French"]
    english_word = current_card["English"]
    flashcard.itemconfig(image, image=flashcard_front)
    flashcard.itemconfig(language, text="French", fill="black")
    flashcard.itemconfig(word, text=f"{french_word}", fill="black")
    flip_timer = window.after(3000, func=translation)


# --------------------  FLIPS THE CARD TO SHOW TRANSLATED WORD  -------------------- #

def translation():
    flashcard.itemconfig(image, image=flashcard_back)
    flashcard.itemconfig(language, text=f"English", fill="white")
    flashcard.itemconfig(word, text=english_word, fill="white")


flip_timer = window.after(3000, func=translation)

# --------------------  UI PART 2 -------------------- #
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
right_button = Button(height=50, width=50, image=right, highlightthickness=0, command=green_button)
right_button.grid(column=0, row=2)

wrong_button = Button(height=50, width=50, image=wrong, highlightthickness=0, command=red_button)
wrong_button.grid(column=1, row=2)

window.mainloop()
