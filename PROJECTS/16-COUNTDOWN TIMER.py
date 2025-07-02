import time

print("===⏲️ COUNTDOWN TIMER ⏲️===")
print("✨Count down from your choosen seconds!✨")

while True:
    try:
        seconds = int(input("\n🤔 Enter seconds to countdown from: "))

        if seconds <= 0:
            print("❌Please enter a positive number")
            continue

        print(f"\n⌛ Starting countdown from {seconds} seconds")

        for i in range(seconds, 0, -1):
            print(f"⌚ {i} seconds remaining...")
            time.sleep(1)

        print("\n🎉COUNTDOWN COMPLETE🎉")

        if not input("\n🔀 Start another countdown? (yes/no): ").lower().strip().startswith("y"):
            print("👋 GoodBye!")
            break

    except ValueError:
        print("❌That's not a valid number")
