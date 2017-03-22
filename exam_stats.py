# Python Script for Exam Statistics Project.

# List Grades as given in Codecademy.
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50]


# Function to print all grades one ny one on separate line.
def print_grades(grades):
    for grade in grades:
        print(grade)

# Function to calculate and return Sum of all the grades in grades list.
def grades_sum(grades):
    sum_of_grades = 0
    for grade in grades:
        sum_of_grades += grade
    return sum_of_grades

# Function to calculate and return Average of all grades in grades list.
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

# Function to calculate and return Variance of grades in grades list.
def grade_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= float(len(scores))
    return variance

# Function to calculate and return Standard Deviation of grades in grades list.
def grade_standard_deviation(variance):
    return variance ** 0.5

# Variable to store variance of grades.
variance = grade_variance(grades)

# Statement to print grades in grades list line by line.
print("Grades :")
print_grades(grades)
# Statement to print sum of grades in grades list.
print("Sum of Grades = ",grades_sum(grades))
# Statement to print average of grades in grades list.
print("Average of Grades = ",grades_average(grades))
# Statement to print variance of grades in grades list.
print("Variance of Grades = ",grade_variance(grades))
# Statement to print standard deviation of grades in grades list.
print("Standard Deviation of Grades = ",grade_standard_deviation(variance))