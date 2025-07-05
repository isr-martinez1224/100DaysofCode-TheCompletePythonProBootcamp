from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

def program():
    on = True
    while on:
        make_coffee = False
        choice = input(f"What would you like? ({menu.get_items()}): ")

        if choice.lower() == "report":
            coffee_maker.report()
            money_machine.report()
            make_coffee = False
        elif choice.lower() == "off":
            on = False
            make_coffee = False
        else:
            item = menu.find_drink(choice.lower())
            if item is None:
                make_coffee = False
            else:
                make_coffee = coffee_maker.is_resource_sufficient(item)
                if make_coffee:
                    make_coffee = money_machine.make_payment(item.cost)
                    if make_coffee:
                        coffee_maker.make_coffee(item)

program()