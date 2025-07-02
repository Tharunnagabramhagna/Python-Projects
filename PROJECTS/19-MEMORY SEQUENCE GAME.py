import random
import time
import os


def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


print("===🧠 MEMORY SEQUENCE GAME 🧠===")
print("✨ Remember the sequence and type it back! ✨")
print("Rules:")
print("- Watch as numbers appear one by one")
print("- After the sequence is shown, type it back in order")
print("- Each round adds one more number to remember")
print("- How far can you go? 🏆\n")

input("Press Enter to start...")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))

    clear_screen()
    print(f"\n=== Round{current_round} ===")
    print(f"Remember this sequence of {len(sequence)} numbers:")

    for number in sequence:
        time.sleep(0.5)
        print(f"\n{number}")
        time.sleep(0.5)
        clear_screen()

    print("\nNow repeat the sequence by typing each number, seperated by spaces:")
    player_answer = input("> ")

    # "3,6,1" => ["3","6","1"] => [3,6,1] (this is done by try block)

    try:
        player_sequence = [int(num) for num in player_answer.split()]
    except ValueError:
        print("❌Please enter numbers only!")
        game_over = True
        continue

    if player_sequence == sequence:
        print(f"🎉 Correct! You remerbered all {len(sequence)} numbers!")
        current_round += 1
        time.sleep(2)
    else:
        print(f"😭 Game over! You remerbered all {current_round - 1} numbers!")
        print(
            f"The correct sequence was: {" ".join(str(num) for num in sequence)}")
        game_over = True

    if game_over:
        play_again = input("\nPlay again? (yes/no): ").lower().strip()
        if play_again.startswith("y"):
            sequence = []
            current_round = 1
            game_over = False
        else:
            print("Thanks for playing! 👋")
