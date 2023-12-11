import random

def get_user_choice():
    print("Enter your choice: rock, paper, scissors, lizard, or Spock")
    user_choice = input().lower()
    while user_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
        print("Invalid choice. Please enter rock, paper, scissors, lizard, or spock.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors", "lizard", "Spock"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or
        (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or
        (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or
        (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or
        (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock"))
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        print("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()
