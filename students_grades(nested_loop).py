#Example for Nested-loop(calculating Studetns grade)
num_students = int(input("Enter the number of students: ")) # prompt user to enter the number of students

i = 1 #"i" is for current students
while i <= num_students:
    total_grade = 0
    num_subjects = int(input(f"Enter the number of subjects for a student {i}: "))  #prompt users to enter the number of subjects

    for j in range(1, num_subjects + 1):  # "j" is for the number of subjects
        grade = float(input(f"Enter the subject {j} grade for the student {i}: "))  # promt users to enter the grade for the studetns
        total_grade += grade

    average_grade = total_grade / num_subjects
    print(f"Average grade for the student {i}: {average_grade:.2f}")
    i += 1
