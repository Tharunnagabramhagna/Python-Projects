import random
first_parts = ["Cisco", "Oliver", "Tony", "Wally", "Barry", "Iris", "Catlin"]
last_parts = ["west", "allen", "queen", "stark", "ramon", "snow", "thawne"]

print("✨FANTASY NAME GENERATOR✨")

count = int(input("\nHow many names do you want? "))

for i in range(count):
    first_name = random.choice(first_parts)
    last_name = random.choice(last_parts)
    print(f"{first_name}{last_name}")
