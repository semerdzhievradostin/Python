print("Welcome to the rollercoaster")
number = int(input("What is your height? "))
bill = 0

if number >= 120:
    print("Let's ride... ")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Ticket is $5")
    elif age <= 18:
        bill = 7
        print("Ticket is $7")
    else:
        bill = 18
        print("Ticket is $18")
    photo = input("Do you want a photo? Y or N\n")
    if photo == "Y":
        bill = bill + 3
    print(f"Ticket is ${bill}")
else:
    print("Ugh, come next year... ")