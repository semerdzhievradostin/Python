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
    random_letter = ''

    for i in range(random.randint(6, 10)):
        random_letter += random.choice(letters)

    random_number = ''

    for i in range(random.randint(3, 5)):
        random_number += random.choice(numbers)

    random_symbols = ''

    for i in range(random.randint(3, 5)):
        random_symbols += random.choice(symbols)

    # Combine Letters Symbols and Numbers and then Randomize them
    password = random_symbols + random_number + random_letter
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
            # --------- If data.json doesn't exist, create and add the data ------ #
            except FileNotFoundError:
                json_data = {
                    website_entry.get(): {
                        "email": em_user_entry.get(),
                        "password": password_entry.get(),
                    }
                }
                with open("data.json", "w") as data_file:
                    json.dump(json_data, data_file, indent=4)
            # ------- If data.json already exists, but it's empty add the data ---- #
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


# ---------------------------- SEARCH FUNCTION ------------------------------- #

def search():
    try:
        website = website_entry.get()
        with open("data.json") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="Username and Password", message=f"Email: {email}\n Password:{password}")
            else:
                messagebox.showinfo(title="Username and Password", message="No credentials found for the website")
    except FileNotFoundError:
        messagebox.showinfo(title="Username and Password", message="File with credentials not found")


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

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", activeforeground="green", command=generate)
generate_password.grid(column=2, row=3)

search_button = Button(text="Search", activeforeground="green", command=search)
search_button.grid(column=3, row=1)

add_button = Button(text="Add", activeforeground="green", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
