from coffeeMachine import CoffeeMachine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
            "chocolate": 0,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "chocolate": 0,
        },
        "cost": 20,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "chocolate": 0,

        },
        "cost": 25,
    },
    "chocolate": {
        "ingredients": {
            "water": 0,
            "milk": 150,
            "coffee": 0,
            "chocolate": 60,
        },
        "cost": 25,

    }
}

resources = {
    "water": 200,
    "milk": 2000,
    "coffee": 1000,
    "chocolate": 400,
    "money": 100
}


def choose_drink(drink_name: str):
    if coffee_machine.have_coffee_resources(drink_name,
                                            water=MENU[drink_name]["ingredients"]["water"],
                                            milk=MENU[drink_name]["ingredients"]["milk"],
                                            coffee=MENU[drink_name]["ingredients"]["coffee"],
                                            chocolate=MENU[drink_name]["ingredients"]["chocolate"]):

        coffee_machine.money += MENU[drink_name]["cost"]
        print(f"making {drink_name}...")

        coffee_machine.make_coffee(water=MENU[drink_name]["ingredients"]["water"],
                                   milk=MENU[drink_name]["ingredients"]["milk"],
                                   coffee=MENU[drink_name]["ingredients"]["coffee"],
                                   chocolate=MENU[drink_name]["ingredients"]["chocolate"], )
    else:
        print(f"I am sorry, I have not enough resources to make {drink_name}")


def make_transaction(drink_cost, money):
    if money == drink_cost:
        return True
    elif money > drink_cost:

        change = money - drink_cost
        print(f"Money change {change}")
        return True

    else:
        return False


def are_enough_change_to_refund(money, coffee_machine_money):
    if money > coffee_machine_money:
        print(f"I have enough change to refund... {money} refunded")
        return False
    else:
        return True


if __name__ == "__main__":
    """ Making a coffee machine object"""
    coffee_machine = CoffeeMachine(water=resources['water'],
                                   milk=resources['milk'],
                                   coffee=resources['coffee'],
                                   chocolate=resources['chocolate'],
                                   money=resources['money'])

    is_on = True  # coffee machine is ON

    while is_on:
        _drink_name = input("What would you like (espresso/latte/cappuccino/chocolate: ")

        if _drink_name == "espresso":
            _money = int(input(f"Insert {MENU[_drink_name]['cost']}: "))
            _cost_drink = int(MENU[_drink_name]['cost'])
            if make_transaction(_cost_drink, _money) and are_enough_change_to_refund(_money, coffee_machine.money):

                choose_drink(_drink_name)
            else:
                print(f"Sorry that's not enough money... {_money} refunded")

        elif _drink_name == "latte":
            _money = int(input(f"Insert {MENU[_drink_name]['cost']}: "))
            _cost_drink = int(MENU[_drink_name]['cost'])
            if make_transaction(_cost_drink, _money) and are_enough_change_to_refund(_money, coffee_machine.money):

                choose_drink(_drink_name)
            else:
                print(f"Sorry that's not enough money... {_money} refunded")

        elif _drink_name == "cappuccino":
            _money = int(input(f"Insert {MENU[_drink_name]['cost']}: "))
            _cost_drink = int(MENU[_drink_name]['cost'])
            if make_transaction(_cost_drink, _money) and are_enough_change_to_refund(_money, coffee_machine.money):

                choose_drink(_drink_name)
            else:
                print(f"Sorry that's not enough money... {_money} refunded")
        elif _drink_name == "chocolate":
            _money = int(input(f"Insert {MENU[_drink_name]['cost']}: "))
            _cost_drink = int(MENU[_drink_name]['cost'])
            if make_transaction(_cost_drink, _money) and are_enough_change_to_refund(_money, coffee_machine.money):

                choose_drink(_drink_name)
            else:
                print(f"Sorry that's not enough money... {_money} refunded")
        elif _drink_name == "report":
            coffee_machine.print_report()

        elif _drink_name == "off":
            is_on = False
        else:
            print("Invalid option!")
