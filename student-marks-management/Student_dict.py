#QUESTION 5

def newstudent():
    a = input("Enter name of new student: ")
    b = int(input("Enter marks of the student: "))
    student_manual[a] = b
    print("Student added successfully!!")

def update_marks():
    c = input("Enter student name: ")
    if c in student_manual:
        d = int(input("Enter new marks: "))
        student_manual[c] = d
        print("Marks updated successfully!!")
    else:
        print("Students doesn't exist!!")

def search_student():
    x = input("Enter student name to search: ")
    if x in student_manual:
        print("Student found!!")
        print(x, ":", student_manual[x])
    else:
        print("Student not found!!")

def display():
    print("Student Information")
    for i in student_manual:
        print(i, ":", student_manual[i])

student_manual = {}
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM ====")
    print("A - Add a student")
    print("B - Update Marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    key = input("Enter your choice: ")
    if (key == "A" or key == "a"):
        newstudent()

    elif (key == "B" or key == "b"):
        update_marks()

    elif (key == "C" or key == "c"):
        search_student()

    elif (key == "D" or key == "d"):
        display()

    else:
        print("INVALID KEY!!")