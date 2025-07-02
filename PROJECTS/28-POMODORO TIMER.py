import time
import os
import platform


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def format_time(seconds):
    # format(30) ==> 00:30
    # format(75) ==> 01:15
    # format(0) ==> 00:00
    minutes = seconds // 60
    seconds_remainder = seconds % 60
    return f"{minutes:02d} : {seconds_remainder:02d}"


def countdown(seconds, label):
    for remaining in range(seconds, 0, -1):
        clear_screen()
        print(f"\n⏱️ {label} ⏱️")
        print(f"\n⌛ Time remaining: {format_time(remaining)}")

        if label == "Work Session":
            print("\n🧠 Focus on your task! 💪")
        elif "Break" in label:
            print("\n☕ Take a breath 😚", end="", flush=True)
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)

        time.sleep(1)

    clear_screen()
    print(f"\n✅ {label} completed!")

    if platform.system() == "Windows":
        import winsound
        # hertz , duration
        winsound.Beep(1000, 500)
    else:
        print("🔔")


def pomodoro_timer():
    try:
        clear_screen()
        print("\n===== 🍅Pomodoro Timer 🍅 =====")

        # Default settings
        work_minutes = 25
        short_break_minutes = 5
        long_break_minutes = 15
        cycles = 4

        while True:
            customize = input(
                "\nUse default settings (25min work, 5min short break, 15min long break)? (yes/no): ").lower().strip()
            if customize in ["yes", "y"]:
                break
            elif customize.startswith("n"):
                while True:
                    try:
                        work_minutes = int(
                            input("\nEnter work session length (minutes): "))
                        short_break_minutes = int(
                            input("\nEnter short break length (minutes): "))
                        long_break_minutes = int(
                            input("\nEnter long break length (minutes): "))
                        cycles = int(
                            input("\nEnter number of cycles before a long break: "))
                        if work_minutes <= 0 or short_break_minutes <= 0 or long_break_minutes <= 0 or cycles <= 0:
                            print(
                                "\n⚠️ All values must be positive numbers. Please try again.")
                            continue
                        break
                    except ValueError:
                        print(
                            "\n❌ Invalid input! Please enter numberic values only. 🔢")
                break
            else:
                print("❌Please enter 'yes' or 'no'")
                continue
        time.sleep(2)

        clear_screen()
        print(f"""\n🚀 Starting Pomodoro Timer with:
    • {work_minutes} minute work sesssions
    • {short_break_minutes} minute short breaks
    • {long_break_minutes} minute long break after {cycles} cycles
    • Press Ctrcl + C at any time to exit""")
        input("\nPress Enter to begin...")

        # Convert minutes to seconds
        work_seconds = work_minutes * 60
        short_break_seconds = short_break_minutes * 60
        long_break_seconds = long_break_minutes * 60

        completed_cycles = 0

        while True:
            countdown(work_seconds, "Work Session")
            completed_cycles += 1

            if completed_cycles % cycles == 0:
                input("\nTime for a long break! Press Enter to start your break...")
                countdown(long_break_seconds, "Long Break")
                input(
                    "\nLong break complete! Press Enter to start the next work session...")
            else:
                input("\nTime for a Short break! Press Enter to start your break...")
                countdown(short_break_seconds, "Short Break")
                input(
                    "\nShort break complete! Press Enter to start the next work session...")
    except KeyboardInterrupt:
        clear_screen()
        print("\n😊 Thanks for using the Pomodoro Timer.GoodBye! 👋",
              end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)


# Final Part
call = pomodoro_timer()
