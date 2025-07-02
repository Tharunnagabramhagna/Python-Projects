print("📃CHARACTER TYPE CHECKER 📃")

text = input("\nEnter a single  character: ")

if text.isalpha():
    print("This is a letter.")
elif text.isdigit():
    print("This is a number.")
else:
    print("This is a special character.")

 # in elif case we can use isnumberic() instead of isdigit()
