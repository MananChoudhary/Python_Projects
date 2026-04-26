import random
import game_data,art


list_data= game_data.data

chosen_items=[]



def user_input():
    while True:
        try:
            user_choice = input("Please enter your answer: Higher or Lower. Type A or B: ").strip().lower()

            if user_choice not in ("a", "b"):
                raise ValueError("Input must be A or B")

            return user_choice

        except ValueError:
            print("Wrong value entered. Please type it again")

            


def pick_data():
    index = random.randrange(len(list_data))
    chosen = list_data.pop(index)
    return chosen

def comparision_chart(user_choice,comp1,comp2,final_score):
    if user_choice=='a' and comp1['follower_count']<comp2['follower_count']:
        print('\n Wrong Guess! \n')
        print(f'Your score is {final_score}')
        
        return False, comp1, comp2, final_score
    
    elif user_choice=='b' and comp1['follower_count']>comp2['follower_count']:
        print('\n Wrong Guess! \n')
        print(f'Your score is {final_score}')
        
        return False, comp1, comp2, final_score

        
    elif user_choice=='a' and comp1['follower_count']>comp2['follower_count']:
        final_score+=1
        comp1=comp2
        comp2=pick_data()
        return True, comp1, comp2, final_score

    
    elif user_choice=='b' and comp1['follower_count']<comp2['follower_count']:
        final_score+=1
        comp1=comp2
        comp2=pick_data()
        return True, comp1, comp2, final_score
    
    return True, comp1, comp2, final_score



final_score=0

game=True
print(art.logo+'\n')


comp1= pick_data()
comp2=pick_data()


while game:
    print(f'{comp1['name']} who is from {comp1['country']} and the profession is {comp1['description']}\n')
    print(f'{art.vs}')
    print(f'{comp2['name']} who is from {comp2['country']} and the profession is {comp2['description']}\n')
    user_choice_current=user_input()

    game, comp1, comp2, final_score=comparision_chart(user_choice_current,comp1,comp2,final_score)


    



