# Menu Driven Script to accept the script name from user and run it.
print("Available Scripts :")
print("1. Enter 1 for Student becomes Teacher.")
print("2. Enter 2 for Battleship.")
print("3. Enter 3 for Exam Statistics.")

choice = int(input("Enter the script number you want to run : "))

if choice==1 :
    #Imports students_to_teacher.py
    print("\nRunning students_to_teacher.py\n")
    import students_to_teacher
elif choice==2 :
    # Imports battleship.py
    print("\nRunning battleship.py\n")
    import battleship
elif choice==3 :
    # Imports exam_stats.py
    print("\nRunning exam_stats.py\n")
    import exam_stats