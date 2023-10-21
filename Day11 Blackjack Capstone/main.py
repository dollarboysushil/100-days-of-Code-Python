import random
cards = ["A" , 2 , 3,4,5,6,7,8,9,10,"J","Q","K"]



player =[]
bot = []
def add_card_player():
    randomcard = random.choice(cards)
    player.append(randomcard)



def add_card_bot():
    randomcard = random.choice(cards)
    bot.append((randomcard))


add_card_player()
add_card_player()
add_card_bot()
add_card_bot()
print(f"Your Card is{player}")
print(f"Computer's first card is : {bot[1]}")

def sum_bot():
    sum_bot = 0
    for _ in bot:
        if _ == "A":
            sum_bot = sum_bot + 1
        elif _ == "J":
            sum_bot = sum_bot + 11
        elif _ == "Q":
            sum_bot  = sum_bot + 12
        elif _ == "K":
            sum_bot = sum_bot + 13
        else:
            sum_bot = sum_bot + _
    return sum_bot
def sum_player():
    sum_player = 0
    for _ in player:
        if _ == "A":
            sum_player = sum_player + 1

        elif _ == "J":
            sum_player = sum_player + 11
        elif _ == "Q":
            sum_player = sum_player + 12
        elif _ == "K":
            sum_player = sum_player + 13
        else:
            sum_player = sum_player + _
    return sum_player

print(f"Sum are {sum_player() , sum_bot()}")


def show():
    sumofbot = sum_bot()

    sumofplayer = sum_player()
    print(sumofplayer)
    print(sumofbot)

    if sumofplayer >=21 and sumofbot >= 21:
        print("Draw")
    elif sumofbot >= 21 and sumofplayer <21:
        print("Player Win")
    elif sumofplayer >= 21 and sumofbot <=21:
        print("Bot Win")
    elif sumofbot <21 and sumofplayer <21:
        if sumofbot > sumofplayer:
            print("Bot Wins")
        elif sumofplayer > sumofbot:
            print("Player Wins")

next  = True
while next:
    hit = input(f"Enter'y' or'n': ")
    if hit == "y":
        add_card_player()
        print(player)
        print(f"Sum are {sum_player(), sum_bot()}")
    elif hit == "n":
        show()
        next = False







