"""Calculates the total marks and percentage of a student based on the marks obtained in different subjects."""

import time


while True:

    no_of_students = int(input("Enter the number of students: "))
    marks = []
    names = []
    subjects = []

    for student in range(1, no_of_students + 1):
        print()
        print("-"*60)
        name = input(f"Enter the name of Student {student}: ")
        if name.strip() == "":
            print("Invalid input. Please enter a valid name.")
            name = input(f"Enter the name of Student {student}: ")
        names.append(name)

        print()
        No_Of_Subjects = int(input(f"Enter the number of subjects for Student {student}: "))
        if type(No_Of_Subjects) != int or No_Of_Subjects <= 0:
            print("Invalid input. Please enter a positive integer for the number of subjects.")
            No_Of_Subjects = int(input(f"Enter the number of subjects for Student {student}: "))
        subjects.append(No_Of_Subjects)

        student_marks = []
        for subject in range(1, No_Of_Subjects + 1):
            print("")
            mark = float(input(f"Enter marks for Subject {subject}: "))
            student_marks.append(mark)
        total_marks = sum(student_marks)
        marks.append(total_marks)

    #Student Report
    
    print()
    print("-"*60)
    print("Calculating the report...")
    for i in range(21):
        bar = "█" * i + "-" * (20 - i)
        print(f"\r[{bar}] {i * 5}%", end="", flush=True)
        time.sleep(0.1)
    print("\r✅ Report generated successfully!          \n")   
    print()
    print("="*60)
    print("Student Marks and Percentage Report".center(60))
    print("="*60)

    for student in range(no_of_students):
            percentage = (marks[student] / subjects[student])
            Cgpa = percentage / 10

            if Cgpa >= 9:
                grade = "A+"
            elif Cgpa >= 8:
                grade = "A"
            elif Cgpa >= 7:
                grade = "B"
            elif Cgpa >= 6:
                grade = "C"
            elif Cgpa >= 5:
                grade = "D"
            else:
                grade = "F"
        
            print(f"Student name  : {names[student]}")
            print(f"Total Marks   : {marks[student]:.2f} / {subjects[student]*100:.2f}")
            print(f"Percentage    : {percentage:.2f}%")
            print(f"CGPA          : {Cgpa:.2f}")
            print(f"Grade         : {grade}")
            print("-"*60)
            print()

    # Ask to continue
    choice = input("\nDo you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        print("\nExiting the Marks Calculator. Goodbye!.....")
        print()
        print("Thank you for using the Marks Calculator!")
        print("-"*60)
        break