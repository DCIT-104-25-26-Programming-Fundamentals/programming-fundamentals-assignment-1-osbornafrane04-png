def add_student():
    name = input("Student name: ")
    student_id = input("Student ID: ")
    num_scores = int(input("How many scores? "))
    
    scores = []
    for i in range(num_scores):
        score = float(input("Enter score " + str(i + 1) + ": "))
        scores.append(score)
    
    # Simple dictionary structure
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    
    students.append(student)
    print('Student "' + name + '" added successfully.')

# --- 2. DISPLAY ALL STUDENTS ---
def display_all_students():
    if len(students) == 0:
        print("No students recorded yet.")
    else:
        print("--------------------------------------------------")
        print("Name | ID | Scores | Average")
        print("--------------------------------------------------")
        for student in students:
            # Simple average: sum / count
            total = sum(student["scores"])
            count = len(student["scores"])
            avg = round(total / count, 2)
            
            print(student["name"] + " | " + str(student["id"]) + " | " + str(student["scores"]) + " | " + str(avg))
        print("--------------------------------------------------")

# --- 3. CALCULATE AVERAGE ---
def calculate_average():
    search_id = input("Enter student ID: ")
    
    for student in students:
        if str(student["id"]) == search_id:
            total = sum(student["scores"])
            count = len(student["scores"])
            avg = round(total / count, 2)
            
            print(student["name"] + "'s average score: " + str(avg))
            return  # Exit function once found
            
    print("Student ID not found!")

# --- 4. MAIN MENU LOOP ---
while True:
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU   ")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_all_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")