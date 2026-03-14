#Minks Quiz Game In Python.
#Base code.
import random
import time
from quiz import quiz
score = 0
high_score = 0

#High score code.
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except:
    high_score = 0
def play_game():
    global score
    global high_score

# Difficulty code.
    while True:
        print("\nChoose difficulty:")
        print("1 Easy (15 seconds)")
        print("2 Medium (10 seconds)")
        print("3 Hard (5 seconds)")
        diff = input("Select difficulty (1-3): ")
        if diff == "1":
            time_limit = 15
            break
        elif diff == "2":
            time_limit = 10
            break
        elif diff == "3":
            time_limit = 5
            break
        else:
            print("Invalid input!")
    score = 0

#Content code.
    questions = list(quiz.keys())
    random.shuffle(questions)
    for question in questions:
        print("\n------------------")
        print(question)
        for option in quiz[question]["options"]:
            print(option)
        start_time = time.time()
        while True:
            guess = input("Enter your guess (A, B, C, D): ").upper()
            if guess in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Please enter A, B, C, or D.")

#Time notifier code.
        end_time = time.time()
        time_taken = end_time - start_time
        correct_answer = quiz[question]["answer"]
        if time_taken > time_limit:
            print("Too slow!")

#Check for answer code.
            print(f"Correct answer: {correct_answer}")
        elif guess == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print(f"Correct answer: {correct_answer}")

#Result code.
    print("\n-----------------------")
    print("         RESULTS         ")
    print("-------------------------")
    final_score = int(score / len(questions) * 100)
    print(f"Your score: {final_score}%")
    if final_score > high_score:
        print("New High Score!")
        high_score = final_score
        with open("highscore.txt", "w") as file:
            file.write(str(high_score))
    return final_score

#Menu code.
running = True
while running:
    print("\n===== MENU =====")
    print("1 Start Game")
    print("2 View Score")
    print("3 View High Score")
    print("4 Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        while True:
            score = play_game()
            while True:
                replay = input("\nPlay again? (y/n): ").lower()
                if replay in ["y", "n"]:
                    break
                else:
                    print("Please type y or n.")
            if replay == "n":
                break
    elif choice == "2":
        print(f"Current score: {score}")
    elif choice == "3":
        print(f"High score: {high_score}")
    elif choice == "4":
        print("Thanks for playing!")
        running = False
    else:
        print("Invalid option.")