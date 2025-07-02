import random
print("🎼 MUSIC RECOMMENDER 🎼")

genre = {

    "rock": ["AC/DC", "Queen", "DJ shankar"],
    "pop": ["taylor swift", "bobby singh", "gajini"],
    "hip-pop": ["yaswanth", "honey singh", "madhu raj"]
}
choice = input("\nWhat genre do you like? (rock/pop/hip-pop): ")

if choice not in genre:
    print("😭 sorry,I don't not that genre.")
else:
    print(f"Check out {random.choice(genre[choice])}!")
