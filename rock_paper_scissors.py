import random

Values=["Rock","Paper","Scissors"]



while True:
    Computers_Choice = random.choice(Values)
    ##User
    User_Choice=input("Enter Your Choice :(Rock , Paper , Scissors) \n")
    print(f"\nYou chose {User_Choice}, computer chose {Computers_Choice}.\n")
    if Computers_Choice == User_Choice:
        print('TIE')
    elif User_Choice == 'Rock' and Computers_Choice =='Scissors':
        print('You win')
    elif User_Choice == 'Paper' and Computers_Choice =='Scissors':
        print('Computer wins')
    elif User_Choice=='Rock' and Computers_Choice=='Paper':
        print('Computer wins')
    elif User_Choice=='Scissors' and Computers_Choice=='Rock':
        print('You win')
    play_again=input("Do you want to play?(y/n)")
    if play_again.lower() != "y":
        break
