from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- GENERATE PASSWORD ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    # Randomize Letters Numbers and Symbols from the Lists
    randomLetter = ''

    for i in range(random.randint(6, 10)):
        randomLetter += random.choice(letters)

    randomNumber = ''

    for i in range(random.randint(3, 5)):
        randomNumber += random.choice(numbers)

    randomSymbols = ''

    for i in range(random.randint(3, 5)):
        randomSymbols += random.choice(symbols)

    # Combine Letters Symbols and Numbers and then Randomize them
    password = randomSymbols + randomNumber + randomLetter
    random_password = list(password)
    random.shuffle(random_password)
    pw = "".join(random_password)
    password_entry.insert(0, f"{pw}")

    copy = messagebox.askokcancel(title=f"Copy password to clipboard", message=f"Do you want to copy the "
                                                                               f"password to your clipboard ?")
    if copy:
        pyperclip.copy(f"{pw}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    json_data = {
        website_entry.get(): {
            "email": em_user_entry.get(),
            "password": password_entry.get(),
        }
    }
    if len(website_entry.get()) < 1 or len(password_entry.get()) < 1 or len(em_user_entry.get()) < 1:
        messagebox.showwarning(title="Warning", message="Please, do not leave any of the fields empty.")
    else:
        correct = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"These are the details you entered"
                                                                                 f"\nEmail:{em_user_entry.get()}\n"
                                                                                 f"Password:{password_entry.get()}")
        if correct:
            try:
                # --------- Updating with new data --------- #
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(json_data)

            # --------- If it's the first time importing data, ignore the above --------- #
            except json.decoder.JSONDecodeError:
                json_data = {
                    website_entry.get(): {
                        "email": em_user_entry.get(),
                        "password": password_entry.get(),
                    }
                }
                with open("data.json", "w") as data_file:
                    json.dump(json_data, data_file, indent=4)

            # --------- Saving the new data after the update --------- #
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="black")

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="black")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:", bg="black", fg="white", font=("Arial", 12))
website_text.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

em_user_text = Label(text="Email/Username:", bg="black", fg="white", font=("Arial", 12))
em_user_text.grid(column=0, row=2)

em_user_entry = Entry(width=35)
em_user_entry.grid(column=1, row=2, columnspan=2)

password_text = Label(text="Password:", bg="black", fg="white", font=("Arial", 12))
password_text.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", activeforeground="green", command=generate)
generate_password.grid(column=2, row=3)


add_button = Button(text="Add", activeforeground="green", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()