from replit import clear
import logo


def highestBid(bidder_list):
    max_bid = 0
    for bidder in bidder_list:
        amount = bidder_list[bidder]
        if amount > max_bid:
            max_bid = amount
            winner = bidder
    print(f"The Winner of this auction is {winner} with a bid of ${max_bid}")


print(logo.logo)
print("Welcome to the secret auction program !")
flag = True

bidders = {}

while flag:
    name = input("What's your name :: ")
    bid = int(input("What's your bid :: $"))
    bidders[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if choice == 'yes':
        clear()
    else:
        flag = False

highestBid(bidders)
