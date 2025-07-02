print("🔤 VOWELS COUNTER 🔤")

# advanced syntax

while True:
    text = input("\nEnter some text(or'quit'): ")
    if text.lower() == "quit":
        print("👋Good Bye")
        break
    vowels = sum(1 for char in text.lower() if char in "aeiou")
    print(f"That text has {vowels} vowels")

# simple syntax

while True:
    text = input("\nEnter some text(or'quit'): ")
    if text.lower() == "quit":
        print("👋Good Bye")
        break
    vowels_counter = 0
    for letter in text.lower():
        if letter in ["a", "e", "i", "o", "u"]:
            vowels_counter += 1
    print(f"That text has {vowels_counter} vowels")
