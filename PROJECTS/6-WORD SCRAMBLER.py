import random

print("👾WORD SCRAMBLER👾")

while True:
    word = input("\nEnter a Word to scramble(or 'quit'): ")
    if word.lower() == 'quit':
        print("👋 Good Bye")
        break

    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled word: {"".join(letters)}")


# everyone => ["e","v","e","r","y","o","n","e"]
# shuffle => ["e","e","y",""v","r","e","o","n"] => join => eeyvreon
