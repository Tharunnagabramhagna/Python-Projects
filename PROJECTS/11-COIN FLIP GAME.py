import random
print("🎮 COIN FLIP GAME 🎮")
print("✨Guess heads or tails!✨")

while True:
    guess = input("\nEnter your guess(heads/tails): ").lower().strip()

    if guess != "heads" and guess != "tails":
        print("Please enter heads or tails")
        continue

    flip = random.choice(["heads", "tails"])
    print(f"\n 🪙 coin shows {flip}")

    if flip == guess:
        print("🎉 You guessed correctly! You won! 🏆")
    else:
        print("😢 Sorry,wrong guess. Try again! 🍀")

    again = input(" 🔀 Play again? (yes/no): ").lower().strip()

    if not again.startswith("y"):
        print("Thanks for playing!👋")
        break
