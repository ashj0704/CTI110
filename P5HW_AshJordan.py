# Jordan Ash

# 4/28/2024

# P5HW

# A program that creates math quizzes

import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    guesses = 0
    while True:
        user_answer = int(input(f"Enter answer. {num1} + {num2}= "))
        guesses += 1
        if user_answer == correct_answer:
            print(f"Congratulations!!!! Your answer is correct.")
            break
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

def subtract_numbers():
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2
    guesses = 0
    while True:
        user_answer = int(input(f"Enter answer. {num1} - {num2}= "))
        guesses += 1
        if user_answer == correct_answer:
            print(f"Congratulations!!!! Your answer is correct.")
            break
        else:
            print("Incorrect! Try again.")

def main():
    while True:
        print("MAIN MENU")
        print("\n----------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print()
        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            add_numbers()
        elif choice == '2':
            subtract_numbers()
        elif choice == '3':
            print("Thank you for playing...Bye!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
