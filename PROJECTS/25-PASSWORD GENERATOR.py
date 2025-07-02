import random
import string
import time


def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special):
    chars = ""

    if use_lowercase:
        chars += string.ascii_lowercase
        # chars = "abcdefghijklmnopqrstuvwxyz"
    if use_uppercase:
        chars += string.ascii_uppercase
        # chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ"
    if use_numbers:
        chars += string.digits
        # chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789"
    if use_special:
        chars += string.punctuation
        # chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789!@#$%&"

    #  Handling the edge case
    if not chars:
        print("\n🚨 Oops! No character types selected. Using lowercase letters by default!")
        chars = string.ascii_lowercase

    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password
    # E.g. password:- "aG12#4@"


def check_password_strength(password):
    score = min(len(password) / 16, 1.0)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    variety = (has_lower + has_upper + has_digit + has_special) / 4.0

    final_score = (score * 0.6) + (variety * 0.4)

    if final_score >= 0.8:
        return "🔥 ULTRA STRONG 🔥"
    elif final_score >= 0.6:
        return "💪 STRONG 💪"
    elif final_score >= 0.4:
        return "👍 DECENT 👍"
    else:
        return "😬 NEEDS IMPROVEMENT 😬"


def get_yes_no_input(question):
    while True:
        response = input(question + "(y/n): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("❌ Error! Please enter 'yes' or 'no'")


def main():
    print("\n🌟===== 🔐 PASSWORD GENERATOR 🔐 =====🌟")
    print("✨ Create super strong snd secure passwords with ease! ✨")

    while True:
        try:
            length = int(input("\n📏 Enter password length (8-30): "))
            if length in range(8, 31):
                break
            else:
                print("⚠️ Error! Please enter a number between 8 and 30")
        except ValueError:
            print("❌ Oops! Please enter a valid number")

    print("\n🎮 Let's customize your password! 🎮")

    use_lowercase = get_yes_no_input("🔡 Include lowercase letters (a-z)? ")
    use_uppercase = get_yes_no_input("🔠 Include uppercase letters (A-Z)? ")
    use_numbers = get_yes_no_input("🔢 Include numbers (0-9)? ")
    use_special = get_yes_no_input("🔣 Include special characters (!@#$%)? ")

    print("\n🔮 Generating your magical password 🔮", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    password = generate_password(
        length, use_lowercase, use_uppercase, use_numbers, use_special)

    print("\n\n🎁 ===== YOUR NEW PASSWORD ===== 🎁")
    print(f"🔑 {password}")
    print(f"💪 Strength: {check_password_strength(password)}")

    print("\n📝===== PASSWORD TIPS =====📝")
    print("🚫 Never use the same password for multiple accounts")
    print("🗄️ Consider using a password manager")
    print("🔀 Change important passwords every few months")
    print("🛡️ Even strong passwords need to be kept secret!")

    if get_yes_no_input("\nWould you like to create another amazing password? "):
        main()
    else:
        print("\n🎉Thank you for using the Super Fun Password Generator! Stay secure!🛡️")

# Final part


call = main()
