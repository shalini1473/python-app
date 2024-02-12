import random

def game():
    choices = ['snake', 'water', 'gun']
    computer_choice = random.choice(choices)
    
    print("Welcome to Snake-Water-Gun Game!")
    print("Choices: Snake, Water, Gun")
    
    user_choice = input("Enter your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please choose again.")
        return

    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'snake':
        if computer_choice == 'water':
            print("You win! Snake drinks water.")
        else:
            print("You lose! Gun kills snake.")
    elif user_choice == 'water':
        if computer_choice == 'gun':
            print("You win! Water douses gun.")
        else:
            print("You lose! Snake drinks water.")
    else:  # user_choice == 'gun'
        if computer_choice == 'snake':
            print("You win! Gun kills snake.")
        else:
            print("You lose! Water douses gun.")

if __name__ == "__main__":
    while True:
        game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break
