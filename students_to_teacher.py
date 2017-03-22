# Python Script for Student becomes Teacher Project.

# Student Dictionaries storing  variables values of "name", "homework", "quizzes" and "tests".
# Dictionary of Student 1
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

# Dictionary of Student 2
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

# Dictionary of Student 3
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# List students containing all 3 student Dictionaries.
students = [lloyd, alice, tyler]

# Function to calculate and return the average of numbers of list.
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

# Function to calculate and return sum of weighted average of homework, quizzes and test keys.
def get_average(student):
    homework = average(student["homework"]) * 0.10
    quizzes = average(student["quizzes"]) * 0.30
    tests = average(student["tests"]) * 0.60
    return homework + quizzes + tests

# Function to calculate and return grade achieved by student depending upon its score.
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Function to calculate and return the average of all scores for all students.
def class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

# Prints the class average to the console.
print("Average of whole class = ",class_average(students))
# Prints the letter grade corresponding to class average.
print("Letter Grade for whole class = ",get_letter_grade(class_average(students)))