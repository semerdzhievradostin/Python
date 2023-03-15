import sys

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

ordering = True


def resource_check():
    for key in resources:
        espresso = menu.get('espresso', {}).get('ingredients', {}).get(key)
        latte = menu.get('latte', {}).get('ingredients', {}).get(key)
        cappuccino = menu.get('cappuccino', {}).get('ingredients', {}).get(key)
        if resources[key] < espresso and ask == "espresso":
            print(f"Sorry, not enough {key} for espresso")
            ordering = False
            return True
        elif resources[key] < latte and ask == "latte":
            print(f"Sorry, not enough {key} for latte")
            ordering = False
            return True
        elif resources[key] < cappuccino and ask == "cappuccino":
            print(f"Sorry, not enough {key} for cappuccino")
            ordering = False
            return True
        else:
            return False


payment = 0


def pay():
    global payment
    print("Please insert coins:")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))

    sum_quarters = 0.25 * quarters
    sum_dimes = 0.10 * dimes
    sum_nickels = 0.05 * nickels
    sum_pennies = 0.01 * pennies
    payment = sum_quarters + sum_dimes + sum_nickels + sum_pennies


gross_sales = 0


def order():
    global gross_sales
    espresso_cost = menu.get('espresso', {}).get("cost")
    latte_cost = menu.get('latte', {}).get("cost")
    cappuccino_cost = menu.get('cappuccino', {}).get("cost")
    if ask == "off":
        sys.exit("Coffee Machine is off")
    if ask == "report":
        print(f"Gross Sales: ${gross_sales}")
        for key in resources:
            print(key, resources[key])
    elif ask == "espresso":
        if resource_check():
            sys.exit("Come back Soon")
        else:
            pay()
            if payment > float(espresso_cost):
                change = payment - float(espresso_cost)
                gross_sales += espresso_cost
                resource_adj_e()
                print(f"Here is the ${round(change, 2)} in change. \n Here is your espresso.Enjoy!")
            else:
                print("The payment is not enough")
    elif ask == "latte":
        if resource_check():
            sys.exit("Come back Soon")
        else:
            pay()
            if payment > latte_cost:
                change = payment - latte_cost
                gross_sales += latte_cost
                resource_adj_l()
                print(f"Here is the ${round(change, 2)}in change. \n Here is your latte.Enjoy!")
            else:
                print(f"The payment is not enough, returning {pay()}")
    elif ask == "cappuccino":
        if resource_check():
            sys.exit("Come back Soon")
        else:
            pay()
            if payment > cappuccino_cost:
                change = payment - cappuccino_cost
                gross_sales += cappuccino_cost
                resource_adj_c()
                print(f"Here is the ${round(change, 2)} in change. \n Here is your latte.Enjoy!")
            else:
                print(f"The payment is not enough, returning {pay()}")


def resource_adj_e():
    for key in resources:
        espresso = menu.get('espresso', {}).get('ingredients', {}).get(key)
        resources[key] = resources[key] - espresso


def resource_adj_l():
    for key in resources:
        latte = menu.get('latte', {}).get('ingredients', {}).get(key)
        resources[key] = resources[key] - latte


def resource_adj_c():
    for key in resources:
        cappuccino = menu.get('cappuccino', {}).get('ingredients', {}).get(key)
        resources[key] = resources[key] - cappuccino


ordering = True


while ordering:
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    order()
