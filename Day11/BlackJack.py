import random
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8 ,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

user_cards = []
computer_cards = []
def blackjack(cards, card):
    gameover = False
    while not len(user_cards) == 2:
        random_keys = random.choice(cards)
        user_cards.append(random_keys)
    while not len(computer_cards) == 2:
        random_keys = random.choice(cards)
        computer_cards.append(random_keys)
    user_score = 0
    for element in user_cards:
        user_hand = card[element]
        user_score = user_score + user_hand
    computer_score = 0
    for element in computer_cards:
        computer_hand = card[element]
        computer_score = computer_score + computer_hand
    print(f"Your cards are: {user_cards}")
    print(f"Your score is: {user_score}")
    print(f"Dealer cards are: {computer_cards[0]}")
    if computer_score == 21 and user_score == 21:
        print("Dealer wins!")
        gameover = True
    if user_score == 21:
        print("You win!")
        gameover = True
    if computer_score == 21:
        print("Dealer wins!")
        gameover = True
    
    while gameover == False:
        if user_score > 21:
            print("You lose")
            gameover = True
            break
        ask = input("Do you want another card ? Type 'yes' or 'no'\n")
        if ask == "no":
            if computer_score < 17:
                computer_score = 0
                computer_cards.append(random_keys)
                for element in computer_cards:
                    computer_hand = card[element]
                    computer_score = computer_score + card[element]
                    if "A" in computer_cards and computer_score > 21:
                        computer_score = computer_score - 10
                print(f"Dealer cards are: {computer_cards}")
            if computer_score == 21 and user_score == 21:
                print("Dealer win!")
                gameover = True
                break
            if user_score == 21:
                print("BLACKJACK You win!")
                gameover = True
                break
            if computer_score == 21:
                print("BLACKJACK Dealer wins!")
                gameover = True
                break
            if computer_score > user_score and computer_score <= 21:
                print(f"Dealer has {computer_score} and you have {user_score}.\n Dealer wins!")
            if user_score > computer_score and user_score <= 21:
                print(f"You have {user_score} and the dealer has {computer_score}.\n You wins!")
            if user_score == computer_score:
                print(f"You both have {user_score}.\n It's a draw!")               
                gameover = True
            if computer_score > 21 and user_score > 21:
                print("DRAW")
            if user_score > 21:
                print("You lose")
            if computer_score > 21:
                print("You win")

        if ask == "yes":    
            user_score = 0
            user_cards.append(random_keys)
            for element in user_cards:
                user_hand = card[element]
                user_score = user_score + card[element]
                if "A" in user_cards and user_score > 21:
                    user_score = user_score - 10
            print(f"Your cards are: {user_cards}")
            print(f"Your score is: {user_score}")
blackjack(cards, card)





