import random

print("🧑‍🍳 RANDOM RECIPE GENERATOR 🧑‍🍳")

flavours = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]
methods = ["baked", "grilled", "stir-fried", "roasted", "sauteed"]
proteins = ["chicken", "tofu", "paneer", "eggs", "fish"]
veggies = ["brocoli", "carrots", "spinach", "bell peppers", "mushroom"]
carbs = ["ice", "pasta", "potatoes", "quinoa", "bread"]

while True:
    flavour = random.choice(flavours)
    method = random.choice(methods)
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)

    print(
        f"\nYour random recipe: {flavour} {method} {protein} with {veggie} and {carb}")

    if not input("\nGenerate another recipe? (y/n): ").lower().strip().startswith("y"):
        print("👋 GoodBye!")
        break
