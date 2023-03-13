import os
name = input("What's your name ?\n")
bid = input("What's your bid ? \n $")

auction = {}

    

def bidding(name, bid):
    bidder = {
        name: bid
        
    }
    auction[name] = bid
bidding(name, bid)

auction_off = False
choice1 = "no"
while auction_off == False:
     ask = input("Are there any more bidders ? Type yes or no ?")
     if ask == "no":
         auction_off = True
         winner = max(auction)
         print(f"The winner is {winner} with a bid of ${auction[winner]}")
     else:
         os.system('cls')
         name = input("What's your name ?\n")
         bid = input("What's your bid ? \n $")
         bidding(name, bid)