# Jordan Ash

# 4/14/2024

# PWHW1

# The program is to display a letter grade for the calculated average.

# Pseudocode for Score Analysis

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):
    
    score = int(input(f"Enter score #{i + 1}: "))
    
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = int(input("Enter a valid score: "))
    
    scores.append(score)

lowest_score = min(scores)

modified_scores = scores.copy()
modified_scores.remove(lowest_score)

average = sum(modified_scores) / len(modified_scores)

if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("\n--------------Results---------------")
print(f"Lowest score : {lowest_score:.1f}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade : {letter_grade}")
print("\n---------------------------------------")
