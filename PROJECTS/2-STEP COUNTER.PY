# print("🏃daily steps counter🏃")            #my version was wrong output for the user
# x=int(input("\nEnter your goal: "))
# y=int(input("\nEnter your steps: "))

# if (y==1000):
#     print("Congratulations your have achieved your goal")
# elif (y<1000):
#     print("You need 500 more steps to reach the goal")
# else:
#     print("You have exceeded your goal with 200 more steps")

print("🏃 STEP COUNTER 🏃")

daily_goal = int(input("\n 🤷 What is your daily step goal? "))

current_steps = int(input("🤔 How many steps have you taken today? "))

remaining = daily_goal-current_steps

if remaining > 0:
    print(f"💪You have {remaining} more steps to reach your goal")
else:
    print(
        f"🎉Congratulations! You've exceeded your goal with {-remaining} more steps")
