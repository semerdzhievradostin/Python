# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first = name1.lower() + name2.lower()
second = name2.lower() + name1.lower()
firstname = first.count('t') + first.count('u') + first.count('r')  + first.count('e')
secondname = second.count('l')  + second.count('o')  + second.count('v')  + second.count('e')
score = str(firstname) + str(secondname)
lovescore = int(score)

if lovescore <= 10 or lovescore >= 90:
    print(f"Your score is {lovescore} you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")
