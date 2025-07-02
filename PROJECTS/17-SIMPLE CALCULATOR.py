def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def multiple(x, y):
    return x*y


def divide(x, y):
    if y == 0:
        return "Error! Divison by zero is not allowed."
    return x/y


def main():
    print("\n===🧮 SIMPLE CALCULATOR 🧮===")
    print("Select operation: ")
    print("1.➕ Addition")
    print("2.➖ Subtraction")
    print("3.✖️ Multiplication")
    print("4.➗ Division")

    while True:
        choice = input("\nEnter a choice(1-4): ")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input.Please enter a number between 1 and 4")
        else:
            break
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number"))
    except ValueError:
        print("❌Error! Please enter valid numbers!")
        return
    if choice == "1":
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == "3":
        print(f"{num1} x {num2} = {multiple(num1, num2)}")
    elif choice == "4":
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    again = input(
        "\nDo you want to perform another calculation? (yes/no): ").lower().strip()
    if not again.startswith("y"):
        print("👋 GoodBye!")
        return
    else:
        main()

# Final step


call = main()
