from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()
is_on = True
while is_on:
    options = menu.get_items()
    ask = input(f"What would you like? {options} ")
    if ask == "off":
        is_on = False
    elif ask == "report":
        money.report()
        coffee.report()
    else:
        drink = menu.find_drink(ask)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)

