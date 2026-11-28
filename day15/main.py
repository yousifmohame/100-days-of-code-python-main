# =============== Day 15 ===============
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

money = {
    "value": 0,
}

def check_resources(w, m, c):
    if w > resources["water"]:
        return False
    elif m > resources["milk"]:
        return False
    elif c > resources["coffee"]:
        return False
    else:
        return True

def Process_coins():
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    return (quarters * 0.25 + dimes * 0.10 +  nickles * 0.05 + pennies * 0.01) 

def make_process(w, m, c):
    resources["water"] -= w
    resources["milk"] -= m
    resources['coffee'] -= c

def make_report():
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money['value']}"

def Check_transaction(price, offical_price, user_choice):
    if offical_price > price :
        print("Sorry that's not enough money. Money refunded.​")
    elif offical_price == price :
        money["value"] += offical_price
        print(make_report())
        make_process(user_choice["water"], user_choice.get("milk", 0), user_choice["coffee"])  
        print(make_report())
    elif offical_price < price :
        change = price - offical_price
        money["value"] += offical_price
        print(f"Here is ${change} dollars in change")
        print(make_report())
        make_process(user_choice["water"], user_choice.get("milk", 0), user_choice["coffee"])
        print(make_report())

power_off = True

while power_off :
    ask_user = input("​What would you like? (espresso/latte/cappuccino):​ ").lower()
    
    if ask_user in MENU:
        user_choice = MENU[ask_user]
        user_choice_resource = user_choice["ingredients"]
        if check_resources(user_choice_resource["water"], user_choice_resource.get("milk", 0), user_choice_resource["coffee"]) == True :
            print("insert coins:")
            price = Process_coins()
            Check_transaction(price, user_choice["cost"], user_choice_resource)
        else:
            print("not enough resources")

    elif ask_user == "off":
        power_off = False
    else :
        print("wrong choice!")
