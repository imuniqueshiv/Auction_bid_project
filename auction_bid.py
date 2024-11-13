from logo import logo

print("Welcome to Auction Table!")
print(logo)


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    # Loop through all bidders in the bidding dictionary
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True

# Continue bidding until there are no more bidders
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What's your bid?:$ "))
    bids[name] = price

    should_continue = (input("Any other bidders? Type 'y' for yes and 'n' for no: \n")).lower()
    if should_continue == "n":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "y":
        print("\n" * 30)  # Clear the screen to keep the bidders' information private
