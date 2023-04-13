MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def is_resource_sufficient(order_ingredient):
    '''return true if order can be made and false when order cannot be made'''
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def process_coin():
    '''returns the total calculated from inserted coins'''
    print("Please insert coin.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.5
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received , drink_cost):
    """return true if payment is successfull and false if money is insufficient."""
    if money_received >= drink_cost:
        change =round( money_received - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit 
        profit += drink_cost 
        return True
        

    else:
        print("Transaction failed Not enough money.")
        return False


def make_coffee(drink_name , order_ingredients):
    """deduct the used ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is Your {drink_name}")




# TODO print all resources
is_on = True
while is_on:
    choice = input("What would you like? (expresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water ; {resources['water']} ml")
        print(f"Milk ; {resources['milk']} ml")
        print(f"Coffee; {resources['coffee']} g")
        print(f"Money ; {profit} $")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment , drink["cost"]):
                make_coffee(choice , drink["ingredients"])


        
        



