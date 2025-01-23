# lib/cli.py
from database import CURSOR, CONNECTION
from models.Student import Student
from models.Teacher import Teacher

from helpers import (
    exit_program,
    name_validation,
    grade_validation,
    teacher_id_validation
)

def add_teacher():
    name = name_validation("Enter teacher name: ")
    years_experience = input ("Enter years experience: ")
    teacher = Teacher(name, years_experience)
    teacher.create()
    print(f"You have successfully added teacher {name}")

def add_student():
    name = name_validation("Enter student name: ")
    grade = grade_validation("Enter student grade: ")
    teacher_id = teacher_id_validation("Enter teacher ID: ")
    student = Student(name, grade, teacher_id)
    student.create()
    print(f"You have successfully added student {name}")

def delete_teacher():
    teacher_id = teacher_id_validation("Enter the ID of the teacher you'd like to delete: ")
    teacher = Teacher.select_by_id(teacher_id)
    if teacher:
        teacher.delete()
        print(f"Teacher with ID: {teacher_id} deleted.")
    else:
        print(f"No teacher found with ID: {teacher_id} found")

def delete_student():
    student_id = teacher_id_validation("Enter the ID of the student you'd like to delete: ")
    student = Student.select_by_id(student_id)
    if student:
        student.delete()
        print(f"Student with ID: {student_id} deleted.")
    else:
        print(f"No student found with ID: {student_id} ")
    
def all_teachers():
    teachers = Teacher.get_all()
    if teachers:
        print(f"All teachers:")
        for teacher in teachers:
            print(f"Name: {teacher.name}, Experience: {teacher.years_experience} years, Teacher ID: {teacher.id}" )
    else:
        print("No teachers available in roster")

def all_students():
    students = Student.get_all()
    if students:
        print(f"All teachers:")
        for student in students:
            print(f"Name: {student.name}, Current Grade: {student.grade}, Student ID: {student.id}" )
    else:
        print("No students currently enrolled")

def view_students_by_teacher():
    teacher_id = input("Please enter the teacher's ID: ")
    teacher = Teacher.select_by_id(teacher_id)
    if teacher:
        print(f"Students of {teacher.name}:")
        students = teacher.students_of_teacher
        if students:
            for student in students:
                print(f"{student.name}, Grade: {student.grade}, Student ID: {student.id}")
        else: 
                print(f"There are no students assigned to {teacher.name}")
    else:
        print("Teacher with this ID not found.")
        

def view_teacher_of_student():
    student_id = input("Please enter the student's ID: ")
    student = Student.select_by_id(student_id)
    if student:
        teacher = student.teacher_of_student
        if teacher:
            print(f"{student.name}'s teacher is {teacher.name}, with {teacher.years_experience} years of experience.")
        else: 
            print(f"There is no teacher assigned to {student.name}")
    else:
        print(f"No student with this ID found")

def assign_new_grade():
    student_id = input("Please enter the student's ID: ")
    student = Student.select_by_id(student_id)
    if student:
        grade = grade_validation("Please enter the updated Grade (A, B, C, D or F): ")
        student.grade = grade
        student.update_grade()
        print(f"Student {student.name}'s grade has been updated to {student.grade}")
    else:
        print(f"No student found with this ID, please try again")




def main():
    Teacher.create_table()
    Student.create_table()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_teacher()
        elif choice == "2":
            add_student()
        elif choice == "3":
            delete_teacher()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            all_teachers()
        elif choice == "6":
            all_students()
        elif choice == "7":
            assign_new_grade()
        elif choice == "8":
            view_students_by_teacher()
        elif choice == "9":
            view_teacher_of_student()

        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add A New Teacher")
    print("2. Add A New Student")
    print("3. Delete A Teacher")
    print("4. Delete A Student")
    print("5. View All Teachers")
    print("6. View All Students")
    print("7. Assign Grade")
    print("8. View Students Of A Teacher")
    print("9. View Teacher of a Student")

if __name__ == "__main__":
    main()
