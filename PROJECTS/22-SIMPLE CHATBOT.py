import random
import time


def chatbot():
    greetings = ["Hello there! 👋🏻", "Hi friend! 😊",
                 "Hey! Nice to meet you! 🎉", "Howdy! 😃"]
    farewells = ["GoodBye! 👋", "See you later! 🚀",
                 "Bye bye! 😊", "Until next time! ✨"]
    jokes = [
        "😄 Why don't eggs tell each other secrets? Because they might crack up!",
        "🐱 Why was the cat sitting on the computer? It wanted to keep an eye on the mouse!",
        "📚 Why did the student eat his homework? Because the teacher said it was a piece of cake!",
        "🚀 Why don't astronauts get hungry after being blasted into space? Because they had a big launch!"]
    facts = [
        "🌍 Earth is the only known planet that supports life.",
        "🧠 Your brain uses about 20 percentage of your body's energy.",
        "🦋 Butterflies can taste with their feet.",
        "💧 Water covers about 71 percentage of the Earth's surface."]
    colors = [
        "🔴 Red", "🟠 Orange", "🟡 Yellow", "🟢 Green", "🔵 Blue", "🟣 Purple", "⚫ Black"]
    seasons = ["🌸 Spring", "☀️ Summer", "🍂 Autumn", "❄️ Winter"]
    weather_types = ["🌧️ Rainy", "☀️ Sunny",
                     "⛅ Partly Cloudy", "🌩️ Thunderstorm"]
    sports = ["⚽ Soccer", "🏀 Basketball", "🎾 Tennis", "🏏 Cricket", "🥊 Boxing"]
    marvel_movies = [
        "🦸‍♂️ Iron Man (2008)",
        "🛡️ Captain America: The Winter Soldier (2014)",
        "🕷️ Spider-Man: No Way Home (2021)",
        "🟣 Avengers: Endgame (2019)"]

    bot_name = "Chat Buddy"

    print(f"🤖 {bot_name} is starting up", end="", flush=True)

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)

    print(f"""
          \n🤖 Welcome to {bot_name}! 🤖
          
          I can chat about:
          🎯 'joke' - Hear a funny joke
          🧠 'fact' - Learn something new
          🌈 'color' - My favorite color
          👋 'bye' - End our chat """)
    chatting = True
    user_name = input("\nWhat's your name: ").lower().strip()
    print(f"🤖 {bot_name}: Nice to meet you, {user_name}! How can I help you today?")

    while chatting:
        user_input = input("😊 You: ").strip()

        if user_input in ["hi", "hello", "hey", "howdy"]:
            print(f"🤖 {bot_name}: {random.choice(greetings)}")

        elif "joke" in user_input:
            print(f"🤖 {bot_name}: {random.choice(jokes)}")

        elif "fact" in user_input:
            print(f"🤖 {bot_name}: {random.choice(facts)}")

        elif "season" in user_input:
            print(f"🤖 {bot_name}: {random.choice(seasons)}")

        elif "weather" in user_input:
            print(f"🤖 {bot_name}: {random.choice(weather_types)}")

        elif "sports" in user_input:
            print(f"🤖 {bot_name}: {random.choice(sports)} is my favorite sports")

        elif "marvel" in user_input:
            print(
                f"🤖 {bot_name}: {random.choice(marvel_movies)} is my favorite Marvel movie")

        elif "color" in user_input:
            print(
                f"🤖 {bot_name}: My favorite color is {random.choice(colors)}! What's yours?")
            color = input("😊 You: ").strip()
            print(f"🤖 {bot_name}: {color} is a great color! 🎨")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print(f"🤖 {bot_name}: {random.choice(farewells)}")
            print(f"🤖 {bot_name}: It was fun chatting with you, {user_name}")
            chatting = False

        else:
            responses = ["That's intersecting! Tell me more.😊",
                         "I'm not sure I understand. Can you try again?🥺",
                         "Hmm, let's talk about something else.Try asking for a joke or fact!✨",
                         "Beep boop! My robot brain is procrssing that...🤔"]

            print(f"🤖 {bot_name}: {random.choice(responses)}")

    print("Thanks for chatting 👋", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)

    chat_again = input(
        "\nDo you want to chat again? (yes/no): ").lower().strip()
    if chat_again.startswith("y"):
        chatbot
    else:
        print("Thanks for chatting,👋GoodBye!", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)

# Final call


call = chatbot()
