from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()
my_money_machine = MoneyMachine()
drink_choice = input("what would you like? (espresso/latte/cappuccino/): ").lower()
my_coffee_maker = CoffeeMaker()
if drink_choice == 'off':
    is_off = True
elif drink_choice == 'report':
    my_coffee_maker.report()
else:
    if drink_choice in my_menu.get_items():
        item = my_menu.find_drink(drink_choice)
        if my_coffee_maker.is_resource_sufficient(item):
            if my_money_machine.make_payment(item.cost):
                my_coffee_maker.make_coffee(item)
                my_money_machine.report()
        else:
            print("not sufficient")
    else:
        print("try again")
