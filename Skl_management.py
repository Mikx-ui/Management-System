# Title:
# FINAL PROJECT: SCHOOL MANAGEMENT SYSTEM
# Beginner Level
# Instruction: Create a simple school management system
# -------------------------------

class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects
        self.grades = {subject: [] for subject in subjects}

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            self.grades[subject] = []

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
            return True 
        else:
            print(f"Subject '{subject}' is not available for {self.name}.")
            return False

    def average(self, subject):
        if subject in self.grades and self.grades[subject]:
            return sum(self.grades[subject]) / len(self.grades[subject])
        return 0

    def overall_average(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def passed(self):
        return self.overall_average() >= 50

    def summary(self):
        report = f"\n--- Report for {self.name} ---\n"
        report += f"Age: {self.age}\n"
        for subject, grades in self.grades.items():
            avg = self.average(subject)
            report += f"{subject}: Grades = {grades}, Average = {avg:.2f}\n"
        report += f"Overall Average: {self.overall_average():.2f}\n"
        report += "Status: Passed \n" if self.passed() else "Status: Failed \n"
        return report
students = {}

def add_student():
    name = input("Enter student name: ").strip().lower()
    age = int(input("Enter student age: "))
    num_subjects = int(input("How many subjects does the student take? "))
    subjects = []
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1}: ").strip()
        subjects.append(subject)
    students[name] = Student(name, age, subjects)
    print(f"Student {name} added successfully!")


def add_grades():
    name = input("Enter student name: ").strip().lower()
    if name in students:
        subject = input("Enter subject: ").strip()
        grade = float(input("Enter grade: "))
        if students[name].add_grade(subject, grade):
            print(f"Grade added for {name} in {subject}")
    else:
        print("Student not found.")

def view_report():
    name = input("Enter student name: ").strip().lower()
    if name in students:
        print(students[name].summary())
    else:
        print("Student not found.")

def view_all_students():
    if students:
        print("\nAll Students:")
        for name in students:
            print("-", name)
    else:
        print("No students added yet.")


def menu():
    print("Welcome to the Student Management System!")
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new student")
        print("2. Add grades to a student")
        print("3. View student report")
        print("4. View all students")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grades()
        elif choice == "3":
            view_report()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Exiting program. Cya!")
            break
        else:
            print("Hmmm, try again.")

menu()
