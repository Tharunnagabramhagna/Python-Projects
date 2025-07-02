import random

print("🔤 GUESS THE WORD 🔤")
print("✨ Unscramble the letters to find a word! ✨")

words = ["python", "game", "computer", "learn", "fun"]

while True:
    original_word = random.choice(words)
    letters = list(original_word)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print(f"\n🔤 Scrambled word: {scrambled}")

    guess = input("🤔\n What's the word? ").lower().strip()

    if guess == original_word:
        print("🎉Correct! You win!🏆")
    else:
        print(f"Sorry, the word was: {original_word}")

    if not input("🔀 Play again? (yes/no): ").lower().strip().startswith("y"):
        print("Thanks for playing!👋")
        break
