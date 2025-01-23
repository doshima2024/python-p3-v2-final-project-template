# lib/helpers.py

def name_validation(prompt):
    while True:
        name = input(prompt)
        if name:
            return name
        print("Name cannot be empty, please provide a valid input")

def grade_validation(prompt):
    while True:
        grade = input(prompt).upper()
        if grade in ["A", "B", "C", "D", "F"]:
            return grade
        print ("Invalid grade, please enter a letter between A & F")

def teacher_id_validation(prompt):
    while True:
        teacher_id = input(prompt)
        try:
            teacher_id = int(teacher_id)
            return teacher_id
        except ValueError:
            print("Invalid input, please enter a number")


def exit_program():
    print("Goodbye!")
    exit()
