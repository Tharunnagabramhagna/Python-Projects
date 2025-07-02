import random
import time


def display_welcome():
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO ULTIMATE QUIZ CHALLENGE! 🎮".center(50))
    print("=" * 50)
    print("""\n📜 Instructions:
- Choose a quiz category
- Answer multiple-choice questions
- Each correct answer is worth 10 points
- See your final score at the end
- Have fun and learn something new!
""")


def display_categories():
    print("""\n🗃️  Quiz Categories:
1. 🌍 General Knowledge
2. 🎬 Movies and TV Shows
3. 🔬 Science and Nature
4. 🎮 Video Games
5. 🎲 Random Mix (questions for all categories)      
""")


def get_user_choice():
    while True:
        try:
            choice = int(input("\nSelect a category (1-5): "))
            if choice in range(1, 6):
                return choice
            else:
                print("⚠️ Oops! Please enter a number between 1 and 5")
        except ValueError:
            print("❌ Error! Please enter a valid number")


def load_question():
    general_knowledge_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Who is known as the father of computers?",
            "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
            "answer": "A"
        },
        {
            "question": "Which country hosted the 2020 Summer Olympics?",
            "options": ["A. China", "B. Japan", "C. Brazil", "D. UK"],
            "answer": "B"}
    ]
    movies_and_tv_shows = [
        {
            "question": "Who played the character of Iron Man in the Marvel Cinematic Universe?",
            "options": ["Chris Evans", "Robert Downey Jr.", "Chris Hemsworth", "Mark Ruffalo"],
            "answer": "Robert Downey Jr."
        },
        {
            "question": "Which TV show features a chemistry teacher who turns to making meth?",
            "options": ["The Wire", "Breaking Bad", "Ozark", "Narcos"],
            "answer": "Breaking Bad"
        },
        {
            "question": "What is the name of the coffee shop in the sitcom 'Friends'?",
            "options": ["Cafe Nervosa", "Central Perk", "Daily Grind", "Coffee Spot"],
            "answer": "Central Perk"
        },
        {
            "question": "In the movie 'Inception', what object does Cobb use as his totem?",
            "options": ["A coin", "A spinning top", "A chess piece", "A die"],
            "answer": "A spinning top"
        },
        {
            "question": "Which film series is known for the line: 'May the Force be with you'?",
            "options": ["Star Trek", "Star Wars", "Guardians of the Galaxy", "The Matrix"],
            "answer": "Star Wars"}
    ]
    science_and_nature = [
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A) Au", "B) Ag", "C) Gd", "D) Go"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Mercury"],
            "answer": "B"
        },
        {
            "question": "What gas do plants absorb from the atmosphere for photosynthesis?",
            "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
            "answer": "C"
        },
        {
            "question": "How many bones are there in the adult human body?",
            "options": ["A) 206", "B) 201", "C) 210", "D) 215"],
            "answer": "A"
        },
        {
            "question": "Which vitamin is produced when the human body is exposed to sunlight?",
            "options": ["A) Vitamin A", "B) Vitamin B12", "C) Vitamin C", "D) Vitamin D"],
            "answer": "D"}
    ]
    video_games = [
        {
            "question": "Which company developed the game 'The Legend of Zelda'?",
            "options": ["A. Sony", "B. Microsoft", "C. Nintendo", "D. Sega"],
            "answer": "C"
        },
        {
            "question": "In which game do players compete in a battle royale on an island called 'Erangel'?",
            "options": ["A. Fortnite", "B. Apex Legends", "C. Call of Duty: Warzone", "D. PUBG"],
            "answer": "D"
        },
        {
            "question": "Which character is known as the mascot of the Sega video game company?",
            "options": ["A. Mario", "B. Sonic", "C. Donkey Kong", "D. Crash Bandicoot"],
            "answer": "B"
        },
        {
            "question": "What is the name of the fictional city where 'Grand Theft Auto: Vice City' takes place?",
            "options": ["A. Liberty City", "B. San Andreas", "C. Vice City", "D. Los Santos"],
            "answer": "C"
        },
        {
            "question": "Which game series features the 'Assassins' and the 'Templars'?",
            "options": ["A. Assassin's Creed", "B. Dark Souls", "C. God of War", "D. Far Cry"],
            "answer": "A"}
    ]

    return {
        1: {"name": "General Knowledge", "questions": general_knowledge_questions},
        2: {"name": "Movies and TV Shows", "questions": movies_and_tv_shows},
        3: {"name": "Science and Nature", "questions": science_and_nature},
        4: {"name": "Video Games", "questions": video_games},
        5: {"name": "Random Mix", "questions": general_knowledge_questions + movies_and_tv_shows
            + science_and_nature + video_games}}


def run_quiz(category_data):
    category_name = category_data["name"]
    questions = category_data["questions"]
    random.shuffle(questions)
    print(f"\n🎯 Starting the {category_name} quiz! 🎯")
    print("Answer each question by typing the letter of your choice (A, B, C, or D).")

    score = 0
    correct_answers = 0

    for i, q in enumerate(questions):
        print(f"\n------- Question {i+1}/{len(questions)} -------")
        print(f"❓ {q["question"]}")

        for option in q["options"]:
            print(option)

        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").upper()
            if user_answer not in ["A", "B", "C", "D"]:
                print("❌Please enter A,B,C or D.")
            else:
                break

        correct = user_answer == q["answer"]
        if correct:
            score += 10
            correct_answers += 1
            print("✅ Correct answer! +10 points")
        else:
            print(f"❌Wrong answer! The correct answer is {q["answer"]}")

        if i < len(questions) - 1:
            print("\nNext question coming up", end="", flush=True)
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(1.5)

    print("\n\n" + "=" * 50)
    print("📊 QUIZ RESULTS 📊".center(50))
    print("=" * 50)
    print(f"Category: {category_name}")
    print(f"Correct answers: {correct_answers} / {len(questions)}")
    print(f"Total Score: {score} points")

    percentage = (score / (len(questions) * 10)) * 100

    if percentage == 100:
        print("\n🏆 PERFECT SCORE! You're a quiz master! 🏆")
    elif percentage >= 80:
        print("\n🌟 EXCELLENT! You really know your stuff!")
    elif percentage >= 60:
        print("\n😊 GOOD JOB! You've got decent knowledge!")
    elif percentage >= 40:
        print("\n🤔 NOT BAD! There's room for improvement!")
    else:
        print("\n📚 KEEP LEARNING! Practice makes everybody perfect!")

    return score


def main():
    display_welcome()
    total_score = 0
    play_again = True

    while play_again:
        display_categories()

        category_choice = get_user_choice()
        all_categories = load_question()
        score = run_quiz(all_categories[category_choice])
        total_score += score
        try:
            again = input("\nPlay another round? (yes/no): ").lower().strip()

            if again in ["y", "yes"]:
                return again
            elif again in ["n", "no"]:
                print(
                    f"\n🎉 Thanks for playing! Your total score from all rounds: {total_score} points 🎉")
                break
            else:
                print("⚠️ Oops! Please type 'yes' or 'no'")

        except ValueError:
            print("❌ Error! Please enter a valid input.")


# Final Part

call = main()
