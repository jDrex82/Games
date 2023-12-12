
import random


def encounter_smaug():
    print("\nWhile journeying through the Lonely Mountain, you encounter the mighty dragon Smaug.")
    print("Smaug is intrigued by your presence. What do you do?")
    
    choice = input("Enter 'talk' to engage in conversation, 'hide' to avoid detection, or 'attack' to confront Smaug: ").strip().lower()

    if choice == "talk":
        print("\nYou manage to engage Smaug in conversation, learning valuable information about his weaknesses.")
        print("With this knowledge, you continue your quest.")
    elif choice == "hide":
        print("\nYou successfully hide from Smaug. The dragon moves on, and you continue your journey.")
    elif choice == "attack":
        print("\nYour attempt to attack Smaug fails miserably. The dragon unleashes its fury, and your journey ends here.")
    else:
        print("Invalid choice. Please enter 'talk', 'hide', or 'attack'.")
        encounter_smaug()


def reach_the_shire():
    print("\nAfter a long and adventurous journey, you finally reach the peaceful land of the Shire.")
    print("You are welcomed by the hobbits. What do you want to do in the Shire?")

    choice = input("Enter 'rest' to take a break and enjoy the Shire's hospitality, or 'continue' to embark on a new quest: ").strip().lower()

    if choice == "rest":
        print("\nYou take a well-deserved rest in the Shire, enjoying the simple pleasures of hobbit life.")
        print("Congratulations on completing your epic adventure!")
    elif choice == "continue":
        print("\nYour thirst for adventure is unquenchable. You bid farewell to the Shire and set out on a new quest.")
        print("The journey continues...")
    else:
        print("Invalid choice. Please enter 'rest' or 'continue'.")
        reach_the_shire()


def start_game():
    print("Welcome to the Hobbit Adventure Game!")
    print("You find yourself in a dark cave. In the depths, you encounter Gollum.")
    print("To escape with the precious ring, you must answer three riddles correctly.")

    riddles = generate_riddles()
    correct_answers = play_riddles(riddles)

    if correct_answers == 3:
        print("Congratulations! You've defeated Gollum and obtained the precious ring.")
        ring_choice()
    else:
        print("Gollum has outsmarted you. The journey ends here.")


def generate_riddles():
    riddles = [
        "The more you take, the more you leave behind. What am I?",
        "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
        "The person who makes it, sells it. The person who buys it never uses it. What is it?",
        "What has keys but can't open locks?",
        "I'm tall when I'm young, and I'm short when I'm old. What am I?",
        "The more you have of it, the less you see. What is it?",
        "I'm not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
        "The person who invented it doesn't want it. The person who bought it doesn't need it. The person who needs it doesn't know it. What is it?",
        "What comes once in a minute, twice in a moment, but never in a thousand years?",
        "The more fragile, the more useful it is. What is it?",
        "What has a heart that doesn't beat?",
        "I can be cracked, made, told, and played. What am I?",
        "What has one eye but can't see?",
        "I fly without wings. I cry without eyes. Wherever I go, darkness follows me. What am I?",
        "The more you take, the more you leave behind. What am I?",
        "I'm not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
        "What has a bed but never sleeps, and can run but never walks?",
        "The more you take, the more you leave behind. What am I?",
        "I'm tall when I'm young, and I'm short when I'm old. What am I?",
        "I have keys but open no locks. I have space but no room. You can enter, but you can't go inside. What am I?",
        "What has a head, a tail, is brown, and has no legs?",
        "I'm always in front of you, but can never be seen. What am I?",
        "The more you take, the more you leave behind. What am I?",
        "I can be cracked, made, told, and played. What am I?",
        "I'm tall when I'm young, and I'm short when I'm old. What am I?",
        # Add more riddles as needed
    ]
    random.shuffle(riddles)
    return riddles[:3]


def play_riddles(riddles):
    correct_answers = 0

    for i in range(3):
        print(f"\nRiddle {i + 1}: {riddles[i]}")
        user_answer = input("Your answer: ").strip().lower()

        if check_answer(riddles[i], user_answer):
            print("Correct! You're one step closer to escaping.")
            correct_answers += 1
        else:
            print("Incorrect! Gollum is cunning.")
            break  # End the game if one riddle is answered incorrectly

    return correct_answers


def check_answer(riddle, user_answer):
    answers = {
        "the more you take, the more you leave behind. what am i?": "footsteps",
        "i speak without a mouth and hear without ears. i have no body, but i come alive with the wind. what am i?": "echo",
        "the person who makes it, sells it. the person who buys it never uses it. what is it?": "coffin",
        "what has keys but can't open locks?": "piano",
        "i'm tall when i'm young, and i'm short when i'm old. what am i?": "candle",
        "the more you have of it, the less you see. what is it?": "darkness",
        "i'm not alive, but i grow; i don't have lungs, but i need air; i don't have a mouth, but water kills me. what am i?": "fire",
        "the person who invented it doesn't want it. the person who bought it doesn't need it. the person who needs it doesn't know it. what is it?": "coffin",
        "what comes once in a minute, twice in a moment, but never in a thousand years?": "letter 'm'",
        "the more fragile, the more useful it is. what is it?": "an egg",
        "what has a heart that doesn't beat?": "artichoke",
        "i can be cracked, made, told, and played. what am i?": "a joke",
        "what has one eye but can't see?": "a needle",
        "i fly without wings. i cry without eyes. wherever i go, darkness follows me. what am i?": "a cloud",
        "i'm not alive, but i can grow; i don't have lungs, but i need air; i don't have a mouth, but water kills me. what am i?": "a flame",
        "what has a bed but never sleeps, and can run but never walks?": "a river",
        "i have keys but open no locks. i have space but no room. you can enter, but you can't go inside. what am i?": "a keyboard",
        "what has a head, a tail, is brown, and has no legs?": "a penny",
        "i'm always in front of you, but can never be seen. what am i?": "the future",
        "i can be cracked, made, told, and played. what am i?": "a riddle",
        "i'm tall when i'm young, and i'm short when i'm old. what am i?": "a candle",
        # Add more answers as needed
    }

    return user_answer == answers.get(riddle.lower(), "").lower()


def ring_choice():
    print("\nYou've obtained the precious ring. Now, you face a choice.")
    print("Do you want to put the ring on and exit the cave?")
    
    choice = input("Enter 'yes' or 'no': ").strip().lower()

    if choice == "yes":
        print("\nYou put on the ring and vanish. The power of the ring is yours, but its consequences are yet unknown.")
        print("Congratulations on completing the Hobbit Adventure Game!")
    elif choice == "no":
        print("\nYou choose not to put on the ring. Gollum captures you. The journey ends here.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        ring_choice()


def start_game():
    print("Welcome to the Hobbit Adventure Game!")
    print("You find yourself in a dark cave. In the depths, you encounter Gollum.")
    print("To escape with the precious ring, you must answer three riddles correctly.")

    riddles = generate_riddles()
    correct_answers = play_riddles(riddles)

    if correct_answers == 3:
        print("Congratulations! You've defeated Gollum and obtained the precious ring.")
        ring_choice()
        print("\nYour journey continues...")
        encounter_smaug()
        reach_the_shire()
    else:
        print("Gollum has outsmarted you. The journey ends here.")


def main():
    # Start the game
    start_game()

if __name__ == "__main__":
    main()
