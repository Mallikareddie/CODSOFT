import random

def user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def rules(userchoice, computerchoice):
    if userchoice == computerchoice:
        return "It's a tie!"
    elif (userchoice == 'rock' and computerchoice == 'scissors') or (userchoice == 'scissors' and computerchoice == 'paper') or (userchoice == 'paper' and computerchoice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def game():
    user_score = 0
    computer_score = 0
    
    while True:
        userchoice = user_choice()
        computerchoice = computer_choice()
        
        print(f"You chose: {userchoice}")
        print(f"Computer chose: {computerchoice}")
        
        result = rules(userchoice, computerchoice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

game()


