import random
import time


def display_welcome():
    print("\n===ROCK PAPER SCISSORS===")
    print("🪨 📄 ✂️")
    print("\nRules:")
    print("- Rock crashes Scissors")
    print("- Scisscors cuts Paper")
    print("- Paper covers Rock")
    print("- First to win 3 rounds is the Champion!🏆")
    print("\n--------------------------")


def get_user_choice():
    while True:
        print("\nMake your choice:")
        print("1. Rock 🪨")
        print("2. Paper 📄")
        print("3. Scissors ✂️")
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in range(1, 4):
                return choice
            else:
                print("Error! Please enter a number between 1 and 3")
        except ValueError:
            print("Please enter a valid number.")


def get_computer_choice():
    return random.randint(1, 3)


def convert_choice_to_text(choice):
    options = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
    return options[choice]


def determine_winner(user_choice, computer_choice):
    # "tie" case
    if user_choice == computer_choice:
        return "tie"
    # user wins cases
    elif ((user_choice == 1 and computer_choice == 3) or
          (user_choice == 2 and computer_choice == 1) or
          (user_choice == 3 and computer_choice == 2)):
        return "user"
    else:
        return "computer"


def display_round_result(user_choice, computer_choice, result):

    user_text = convert_choice_to_text(user_choice)
    computer_text = convert_choice_to_text(computer_choice)

    print(f"\nYou choose: {user_text}")
    print("Computer is choosing", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(f"\nComputer choose: {computer_text}")

    if result == "tie":
        print("It's a tie! 🤝")
    elif result == "user":
        print("You won this round! 🎉")
    else:
        print("Computer wins this round! 💻")


def play_game():
    """Main game function."""

    display_welcome()

    user_score = 0
    computer_score = 0
    target_score = 3
    round_num = 1

    while user_score < target_score and computer_score < target_score:
        print(f"\n=== Round {round_num} ===")
        print(f"Score: You {user_score} - {computer_score} Computer")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_round_result(user_choice, computer_choice, result)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        round_num += 1

    print("\n===GAME OVER===")
    print(f"Final Score: You {user_score} - {computer_score} Computer")

    if user_score > computer_score:
        print("🎉Congratulations! You are the champion! 🎉")
    else:
        print("😭 Better luck next time! The computer wins this game.")

    play_again = input(
        "\nDo you want to play again? (yes/no): ").lower().strip()
    if play_again.startswith("y"):
        play_game
    else:
        print("Thanks for playing! 👋")


# Final step
Final_call = play_game()
