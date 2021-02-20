class CoffeeMachine:
    water: int
    milk: int
    coffee: int
    chocolate: int
    money: float

    def __init__(self, water, milk, coffee, chocolate, money=0):

        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.chocolate = chocolate
        self.money = money
        print(f"Building a new machine... With {self.water} ml of water, {self.milk} ml of milk, {self.coffee} gr of "
              f"coffee and {self.chocolate}gr of chocolate....money {self.money}")

    def print_report(self):

        print("Report:")
        print(f"Water: {self.water}")
        print(f"Milk: {self.milk}")
        print(f"Coffee: {self.coffee}")
        print(f"Chocolate: {self.chocolate}")
        print(f"Money: {self.money}")

    def make_coffee(self, **ingredients):
        self.water -= ingredients["water"]
        self.milk -= ingredients["milk"]
        self.coffee -= ingredients["coffee"]
        self.chocolate -= ingredients["chocolate"]

    def have_coffee_resources(self, coffee_name, **resources):
        """Have resources for coffee"""
        
        if coffee_name == "chocolate" and self.milk >= resources["milk"] and self.chocolate >= resources["chocolate"]:
            return True
        elif coffee_name == "espresso" and self.water >= resources["water"] and self.coffee >= resources["coffee"]:
            return True
        elif coffee_name == "cappuccino" \
                or coffee_name == "latte"\
                and self.water >= resources["water"] \
                and self.coffee >= resources["coffee"] \
                and self.milk >= resources["milk"]:
            return True
        else:
            return False

        

