import student_db  # Import the functions from the student_db.py program

def show_menu():
    print("\nStudent Manager")
    print("1. View All Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def handle_view_students():
    students = student_db.view_students()
    if students:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
    else:
        print("No students found or error occurred.")

def handle_add_student():
    try:
        name = input("Enter student name: ")
        if not name:
            raise ValueError("Name cannot be empty.")
        
        age = int(input("Enter student age: "))
        if age <= 0:
            raise ValueError("Age must be a positive number.")
        
        grade = input("Enter student grade: ")
        if not grade:
            raise ValueError("Grade cannot be empty.")
        
        student_db.add_student(name, age, grade)
    except ValueError as e:
        print(f"Input Error: {e}")

def handle_update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
        
        name = input("Enter new name: ")
        if not name:
            raise ValueError("Name cannot be empty.")
        
        age = int(input("Enter new age: "))
        if age <= 0:
            raise ValueError("Age must be a positive number.")
        
        grade = input("Enter new grade: ")
        if not grade:
            raise ValueError("Grade cannot be empty.")
        
        student_db.update_student(student_id, name, age, grade)
    except ValueError as e:
        print(f"Input Error: {e}")

def handle_delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        student_db.delete_student(student_id)
    except ValueError:
        print("Invalid ID. Please enter a valid number.")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                handle_view_students()
            elif choice == 2:
                handle_add_student()
            elif choice == 3:
                handle_update_student()
            elif choice == 4:
                handle_delete_student()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
