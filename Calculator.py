logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2



dict_collection={'+': add, '-': subtract,'*': multiply,'/': divide}



def actual_calculation():
    try:

        user_first_input=int(input("Enter your first number: \n"))
    except:
        print("This is not a number. Please try again!")
        return actual_calculation()
    
    temp_value=user_first_input

    while True:
        try:
            operation=input("Choose your operation +,-,*,/ \n")
            user_second_input=int(input("Enter your second number \n"))
            function_used=dict_collection[operation]
            overall_result=function_used(temp_value,user_second_input)
        except:
            print("Wrong value or operant provided")
            continue

        print(f"{temp_value} {operation} {user_second_input} = {overall_result}")

        want_continue=input(f"Type 'y' to continue calculating with {overall_result} or type 'n' to start a new calculation. You can stop by typing 's'  \n").lower()
        if want_continue=='y':
            temp_value=overall_result
            continue
        elif want_continue=='n':
            return actual_calculation()
        elif want_continue=='s':
            print("Ending the program!")
            return
        else:
            print("Invalid Input")

print(logo+'\n')
actual_calculation()











