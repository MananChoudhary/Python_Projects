import random
from art import logo


def main():

    print(logo+'\n')

    user_game_mode_choice=input("\nEnter which mode of difficulty you want to play in : Easy or Hard:   ")
    guessed_numbers=list()
    

    game=True

    chosen_number=random.randint(1,100)
   
    if user_game_mode_choice.lower()=='easy':
        total_guesses=8
    elif user_game_mode_choice.lower()=='hard':
        total_guesses=6
    else:
        print("Invalid Choice. Defaulting to easy!")
        total_guesses=8

        
    print(f"The total number of guesses you have is {total_guesses}")

    def criteria_check(user_input, chosen_number, guessed_numbers, final_guesses):

        if user_input in guessed_numbers:
            print("You have already guessed this number. Please choose another number.")  
            return final_guesses  

        elif user_input>chosen_number:
            print("Too High")
            
            total_guesses=final_guesses-1
            print(f"The chances you have left is {total_guesses}")
            return total_guesses

        elif user_input<chosen_number:
            print("Too Low")
            total_guesses=final_guesses-1
            print(f"The chances you have left is {total_guesses}")
            return total_guesses
        
        elif user_input==chosen_number:
            print("Your Guess is Correct")
            return final_guesses
            

    while game:
        user_input=int(input("Please Enter Your Guess: \n"))
        
        total_guesses = criteria_check(user_input=user_input,chosen_number=chosen_number,guessed_numbers=guessed_numbers,final_guesses=total_guesses)
        if user_input not in guessed_numbers:
            guessed_numbers.append(user_input)
        
        print(f"You have guessed these numbers already: {guessed_numbers}")

        if user_input==chosen_number:
            print(f"The right number was : {chosen_number}")        
            break
        if total_guesses==0:
            print("You lost the game!")
            print(f"The right number was : {chosen_number}")
            break

main()

while input("Do you wanna play again? Type yes or no:  ")=='yes':
    main()
