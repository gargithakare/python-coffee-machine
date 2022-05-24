from resources import MENU
from resources import resources


def calculate_money(quarters, dimes, nickles, pennies):
    print("Please insert coins.")
    quarters = float(input("How many quarters? :"))
    dimes = float(input("How many dimes? :"))
    nickles = float(input("How many nickles? :"))
    pennies = float(input("How many pennies? :"))

    inserted_quarters = quarters * 0.25
    inserted_dimes = dimes * 0.10
    inserted_nickles = nickles * 0.05
    inserted_pennies = pennies * 0.01

    inserted_coins = inserted_quarters + inserted_dimes + inserted_nickles + inserted_pennies
    return inserted_coins

    # print(inserted_coins)


# quarters = 0
# dimes = 0
# nickles = 0
# pennies = 0
# cost_espresso = MENU["espresso"]["cost"]
# cost_latte = MENU["latte"]["cost"]
# cost_cappuccino = MENU["cappuccino"]["cost"]
# inserted_coins = 0
# return_change = 0
# money_collected = 0

coffee_machine = True

while coffee_machine:
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    cost_espresso = MENU["espresso"]["cost"]
    cost_latte = MENU["latte"]["cost"]
    cost_cappuccino = MENU["cappuccino"]["cost"]
    inserted_coins = 0
    return_change = 0
    money_collected = 0

    ask = input("What would you like to have? (espresso -> $1.5 /latte -> $2.5/cappuccino -> $3): ")

    # "To check resources type 'report'. To refill resources type 'refill' : ")

    if ask == "espresso":
        inserted_coins = calculate_money(quarters, dimes, nickles, pennies)
        return_change = inserted_coins - cost_espresso
        if return_change < 0:
            print("Sorry. Not enough money. Here is your money back. Come again!")
        else:
            money_collected = money_collected + (inserted_coins - return_change)
            return_change = round(return_change, 2)
            print(f"You get ${return_change} change back.")
            print("Enjoy your drink!")
    elif ask == "latte":
        inserted_coins = calculate_money(quarters, dimes, nickles, pennies)
        return_change = inserted_coins - cost_latte
        if return_change < 0:
            print("Sorry. Not enough money. Here is your money back. Come again!")
        else:
            money_collected = money_collected + (inserted_coins - return_change)
            return_change = round(return_change, 2)
            print(f"You get ${return_change} change back.")
            print("Enjoy your drink!")
    elif ask == "cappuccino":
        inserted_coins = calculate_money(quarters, dimes, nickles, pennies)
        return_change = inserted_coins - cost_cappuccino
        if return_change < 0:
            print("Sorry. Not enough money. Here is your money back. Come again!")
        else:
            money_collected = money_collected + (inserted_coins - return_change)
            return_change = round(return_change, 2)
            print(f"You get ${return_change} change back.")
            print("Enjoy your drink!")

    # resources
    if ask == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"] \
                or resources["milk"] < MENU["espresso"]["ingredients"]["milk"] \
                or resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry. Not enough resources.")
        else:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    elif ask == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"] \
                or resources["milk"] < MENU["latte"]["ingredients"]["milk"] \
                or resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry. Not enough resources.")
        else:
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]

    elif ask == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"] \
                or resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"] \
                or resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry. Not enough resources.")
        else:
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = money_collected

    if ask == "report":
        print(f"Water : {water} ml ")
        print(f"Milk : {milk} ml ")
        print(f"Coffee : {coffee} gm")

    refill_what = ""
    water_amount = 0
    milk_amount = 0
    coffee_amount = 0

    if ask == "refill":
        refill_what = input("What do you want to refill? (water/milk/coffee) :")
    if refill_what == "water":
        water_amount = int(input("How much water do you want to refill? (in ml/gm) :"))
        resources["water"] = resources["water"] + water_amount
        print("Resources after refill :")
        print(f"Water : {resources['water']} ml ")
        print(f"Milk : {milk} ml ")
        print(f"Coffee : {coffee} gm")
    if refill_what == "milk":
        milk_amount = int(input("How much milk do you want to refill? (in ml/gm) :"))
        resources["milk"] = resources["milk"] + milk_amount
        print("Resources after refill :")
        print(f"Water : {water} ml ")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee : {coffee} gm")
    if refill_what == "coffee":
        coffee_amount = int(input("How much coffee do you want to refill? (in ml/gm) :"))
        resources["coffee"] = resources["coffee"] + coffee_amount
        print("Resources after refill :")
        print(f"Water : {water} ml ")
        print(f"Milk : {milk} ml ")
        print(f"Coffee : {resources['coffee']} gm")
