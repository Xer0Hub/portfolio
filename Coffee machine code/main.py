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
#PERSISTENT DICTIONARY
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#MONEY VAULT
cash_till = {"money": 0}

def coin_calc():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    cash_till["money"] += int(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)
    return int(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)


def coffee_maker():
    make_coffee = True
    print("\n" * 3)

    main_menu = input("Good morning. Would you like an espresso(1), a latte(2) or a cappuccino(3)? \n").lower().strip()
    #USER NOW ENTERS THE MAKING CYCLE
    while make_coffee:
        #MAINTANENCE OPTIONS
        if main_menu == "report":
            for key, value in resources.items():
                print(f"{key}: {value}")
            for key, value in cash_till.items():
                print(f"{key}: ${value}")
            make_coffee = False
            coffee_maker()

        #1 HANDLES ESPRESSO
        if main_menu == "espresso" or main_menu == "1":
            double_check = input(f"Espresso is {MENU["espresso"]["cost"]}, would you like to continue? Y or N: ").upper()
            if double_check == "Y":
                coin_input = coin_calc()
                #MONEY JUDGMENT PHASE
                if coin_input >= MENU["espresso"]["cost"]:
                    #Check if there's enough resources.
                    if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
                        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                    else:
                        print("Not enough water please refill.")
                        make_coffee = False
                        coffee_maker()

                    if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                    else:
                        print(f"Not enough coffee please refill.")
                        make_coffee = False
                        coffee_maker()

                    #EVALUATE CHANGE AND SERVE COFFEE
                    if coin_input - MENU["espresso"]["cost"] != 0:
                        change = coin_input - MENU["espresso"]["cost"]
                        rounded_change = (round(change, 2))
                        print(f"Your change is {rounded_change}")
                    print("Here's your espresso ☕️, enjoy!")
                    make_coffee = False
                    coffee_maker()
                else:
                    print(f"Insufficient funds, you inserted {coin_input}. You need {MENU["espresso"]["cost"]}")
            else:
                make_coffee = False
                coffee_maker()

        #2 HANDLES LATTE
        if main_menu == "latte" or main_menu == "2":
            double_check = input(f"latte is {MENU["latte"]["cost"]}, would you like to continue? Y or N: ").upper()
            if double_check == "Y":
                coin_input = coin_calc()
                # MONEY JUDGMENT PHASE
                if coin_input >= MENU["latte"]["cost"]:
                    #CHECK IF THERE'S ENOUGH RESOURCES
                    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
                        resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    else:
                        print("Not enough water, please refill.")
                        make_coffee = False
                        coffee_maker()

                    if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    else:
                        print("Not enough milk, please refill.")
                        make_coffee = False
                        coffee_maker()

                    if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                    else:
                        print("Not enough coffee, please refill.")
                        make_coffee = False
                        coffee_maker()
                    #EVALUATE CHANGE AND SERVE COFFEE
                    if coin_input - MENU["latte"]["cost"] != 0:
                        change = coin_input - MENU["latte"]["cost"]
                        rounded_change = (round(change, 2))
                        print(f"Your change is {rounded_change}")
                    print("Here's your latte ☕️, enjoy!")
                    make_coffee = False
                    coffee_maker()
                else:
                    print(f"Insufficient funds, you inserted {coin_input}. You need {MENU["latte"]["cost"]}")
            else:
                make_coffee = False
                coffee_maker()

        if main_menu == "cappuccino" or main_menu == "3":
            double_check = input(f"Cappuccino is {MENU["cappuccino"]["cost"]}, would you like to continue? Y or N: ").upper()
            if double_check == "Y":
                coin_input = coin_calc()
                # MONEY JUDGMENT PHASE
                if coin_input >= MENU["cappuccino"]["cost"]:
                    # CHECK IF THERE'S ENOUGH RESOURCES
                    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
                        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    else:
                        print("Not enough water, please refill.")
                        make_coffee = False
                        coffee_maker()

                    if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                    else:
                        print("Not enough milk, please refill.")
                        make_coffee = False
                        coffee_maker()

                    if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    else:
                        print("Not enough coffee, please refill.")
                        make_coffee = False
                        coffee_maker()

                    #EVALUATE CHANGE AND SERVE COFFEE
                    if coin_input - MENU["latte"]["cost"] != 0:
                        change = coin_input - MENU["cappuccino"]["cost"]
                        rounded_change = (round(change, 2))
                        print(f"Your change is {rounded_change}")
                    print("Here's your latte ☕️, enjoy!")
                    make_coffee = False
                    coffee_maker()


                #THIEVES ARE HANDLED HERE (FIX THIS FOR EVERY OPTION)
                else:
                    print(f"Insufficient funds, you inserted {coin_input}. You need {MENU["cappuccino"]["cost"]}")

            else:
                make_coffee = False
                coffee_maker()


coffee_maker()
