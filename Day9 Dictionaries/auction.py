

def get_parameter():
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    database["name"] = name
    database["bid"] = int(bid)

database = {}

next_player = True

while next_player == True:
    get_parameter()
    other_bidder = input("Are there any other bidders? Type yer or no:")
    if other_bidder == "yes":
        pass


    elif other_bidder == "no":
        next_player = False


def highest_bid():
    highest_bid = 0
    winner = ""
    for bidder in database:
        if bidder == "bid":  # Check if the key is 'bid'
            amount = int(database[bidder])  # Convert the bid amount to an integer
            if amount > highest_bid:
                highest_bid = amount
                winner = database["name"]  # Get the name associated with the winning bid

    print(f"Winner is {winner} with a bid of ${highest_bid}")


highest_bid()