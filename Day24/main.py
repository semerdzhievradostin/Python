
with open("Input/Letters/starting_letter.txt") as letter:
    letter = str(letter.read())


with open("Input/Names/invited_names.txt") as name:
    name = name.readlines()

for person in name:
    receiver_name = str(person.replace("\n", " "))
    path = str(f"Output/ReadyToSend/letter_for_{receiver_name}.txt")
    with open(path, mode="w") as letter_to:
        receiver = letter.replace("[name]", receiver_name)
        letter_to.write(receiver)


