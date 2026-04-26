import math
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
    "money": 0
}

turn_machine_on=True

def check_resources(user_input,resources,MENU):
    for i in (MENU[user_input]['ingredients']):
        if resources[i]< MENU[user_input]['ingredients'][i]:
            print(f"There is not enough {i} to prepare {user_input}")
            return False      
    return True
        
def process_coins():
    coin_quarter=int(input('Enter no of quarters you want to put: '))
    coin_dimes=int(input('Enter no of dimes you want to put: '))
    coin_nickles=int(input('Enter no of nickles you want to put: '))
    coin_pennies=int(input('Enter no of pennies you want to put: '))

    amount_added= (0.25*coin_quarter)+(0.10*coin_dimes)+(0.05*coin_nickles)+(0.01*coin_pennies)
    return amount_added

def check_transaction(user_amount,user_input,resources):
    if user_amount<MENU[user_input]['cost']:
        print("Sorry that's not enough money. Money refunded")
        return False

    elif user_amount>=MENU[user_input]['cost']:
        residual_amount=user_amount-(MENU[user_input]['cost'])
        print(f"Here is ${round(residual_amount,2)} dollars in change.")
        for i in MENU[user_input]['ingredients']:
            resources[i]=resources[i]-MENU[user_input]['ingredients'][i]
        
        resources['money']+=MENU[user_input]['cost']


        return True
    


while turn_machine_on:
    user_input=input("What would you like? (espresso/latte/cappuccino): ")
    if user_input.lower()=="off":
        turn_machine_on=False
    
    else:
        if user_input.lower()=="report":
            for key, value in resources.items():
                print(f"{key}: {value}")
            continue

        result=check_resources(user_input,resources,MENU)

        if result is not True:
            continue

        else:
            resultant_amount=process_coins()
            transaction= check_transaction(resultant_amount,user_input,resources)

            if transaction is True:
                print(f"Here is your {user_input}.Enjoy")
            else:
                turn_machine_on=False




        

        


            



