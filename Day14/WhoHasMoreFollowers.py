from art import logo, vs
from gamedata import data
import random
import os
print(logo)
lives = 1
points = 0
def person1(data):
    global person1_followers
    random_index = random.randrange(len(data)-1)
    person_name = data[random_index]["name"]
    person_description = data[random_index]["description"]
    person_country = data[random_index]["country"]
    person1_followers = data[random_index]["follower_count"]
    print(f"{person_name}, a {person_description} from {person_country}")

def person2(data):
    global person2_followers
    random_index = random.randrange(len(data)-1)
    person_name = data[random_index]["name"]
    person_description = data[random_index]["description"]
    person_country = data[random_index]["country"]
    person2_followers = data[random_index]["follower_count"]
    print(f"{person_name}, a {person_description} from {person_country}")

def versus(person1, person2):
    print("Comapre A:"), person1(data)
    print(vs)
    print("Against B:"), person2(data)

versus(person1, person2)

while lives >= 1:
    ask = input("Who has more followers? Type 'A' or 'B': ")
    if ask == "A" and person1_followers > person2_followers:
        points += 1
        print(f"You're right, you have {points} points."), versus(person1, person2)
    elif ask =="B" and person2_followers > person1_followers:
        points += 1
        print(f"You're right, you have {points} points."), versus(person1, person2)
    else:
        lives -= 1
        print("Nope, you lose.")
        