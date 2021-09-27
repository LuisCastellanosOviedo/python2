from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with {highest_bid}")


while not bidding_finished:
    name = input("What is your name ?: ")
    price = int(input("What is your bid ?: $"))
    bids[name] = price
    should_continue = input("More bidders ? yes o no")
    if should_continue.lower() == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue.lower() == "yes":
        clear()
