print("🎨 COLOR MIXER 🎨")

color_mixers = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("white", "red"): "pink",
    ("red", "green"): "brown"
}

while True:
    color1 = input("\nEnter first color: ").lower().strip()
    color2 = input("Enter second color: ").lower().strip()

# strip function => Ex:- "red  " => "red"

    mix = None
    if (color1, color2) in color_mixers:
        mix = color_mixers[(color1, color2)]
    elif (color2, color1) in color_mixers:
        mix = color_mixers[(color2, color1)]

    if mix:
        print(f"\nWhen you mix {color1} and {color2},you get {mix}!")
    else:
        print("😭 Sorry, I don't know that color mix")

    if not input("\nMix more colors? (y/n): ").lower().strip().startswith("y"):
        print("👋GoodBye!")
        break
