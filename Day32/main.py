import smtplib
import credentialsconfig
from datetime import date
import random
import pandas
import json
import os

todays_date = date.today()
year = todays_date.year
month = todays_date.month
day = todays_date.day



birthdays = pandas.read_csv("birthdays.csv")
birthdays_list = pandas.DataFrame(birthdays)
frame = birthdays_list.to_dict(orient="index")
df = todays_date.year in birthdays_list['year'].unique()
with open("data.json", "w") as data_file:
    json.dump(frame, data_file, indent=4)

happy_birthday = ""
birthday_email = ""

def check_birthdays():
    global happy_birthday, birthday_email
    with open("data.json") as birthday_file:
        data = json.load(birthday_file)
        for name in data:
            if data[name]["year"] == year and data[name]["month"] == month and data[name]["day"] == day:
                happy_birthday = data[name]["name"]
                birthday_email = data[name]["email"]
                birthday_letter = random.choice(os.listdir("letters"))

                with open(f"letters/{birthday_letter}") as letter:
                    letter = str(letter.read())

                with open(f"letters/{birthday_letter}", mode="w") as letter_to:
                    receiver = letter.replace("[NAME]", happy_birthday)
                    happy_birthday_to = letter_to.write(receiver)
                    print(happy_birthday_to)
                    connection = smtplib.SMTP(host='smtp.gmail.com')
                    connection.starttls()
                    connection.login(credentialsconfig.my_email, credentialsconfig.password)
                    connection.sendmail(credentialsconfig.my_email, birthday_email,
                                        msg=f"Subject:Happy Birthday\n\n " f"{happy_birthday_to}")
                    connection.close()


check_birthdays()




