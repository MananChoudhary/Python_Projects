from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

x=Menu()
a=CoffeeMaker()
b=MoneyMachine()



machine_on= True
while machine_on:
    user_input=input("What do you want "+ f"{x.get_items()}?: ")
    if user_input.lower()=='off':
        machine_on=False
        break

    if user_input.lower()=='report':
        a.report()
        b.report()
        continue

    drink=x.find_drink(user_input)
    if drink is None:
        continue
    resource_check=a.is_resource_sufficient(drink)
    if resource_check:
        payment_finalization=b.make_payment(drink.cost)
        if payment_finalization:
            a.make_coffee(drink)
       
            
    
    


    

