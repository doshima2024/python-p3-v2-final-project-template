# Daniel's Lower School Administration CLI Tool

This CLI application, designed by Daniel Oshima, is meant to allow a lower school's administrator and teachers to 
manage rosters of students, assign them to teachers, and keep track of their grades. It establishes a one to many relationship between Teacher and Students, and allows the administrator and teacher users to do nine actions altogether, which are
oulined below.

## Requirements

Running this program will require you to have Python installed on your machine and fork and clone it from Github.
After this, you will need to cd into the directory: python-p3-v2-final-project-template/lib and run the command:
python cli.py
If using vscode to view the database backend, make sure to hit the refresh button after you've made a change to the database in order to see it reflected!

## Explanation for use

From there, you will be provided on screen with a menu, which will guide you through the processes (numbered functions of the program) as outlined below. 

## cli.py file

In my cli.py file, one can find the functions to execute the main functions of the application, which call
on the ORM methods and properties outlined in the classes Student.py and Teacher.py, namely:
    0. Exit the program
    1. Add a new teacher to the database
    2. Add a new student to the database, and assign them to a teacher, along with an inital grade
    3. Remove or delete a teacher from the database
    4. Remove or delete a student from the database
    5. Read and view all teachers in the databsse
    6. Read and view all students in the database
    7. Read and view students of a specific teacher
    8. Read and view the teacher of a specific student
    9. Update and assign a new grade to a student

Underneath these functions is a main function which allows for the operation and interactivity of the CLI for the user, and underneath that is the function which enables the printing of the CLI menu visible to the user.

## Student.py file

There is a Student class defined in the file Student.py which includes __init__ and __repr__ special methods along with ORM class and instance methods for the following operations: 

    1. Creating and dropping tables for the Students class
    2. Creating a new instance (row) of the Student class
    3. Deleting an instance of Student
    4. Reading or selecting all students
    5. Selecting and reading the Teacher of a Student
    6. Selecting a student by ID
    7. Updating a student's grade

## Teacher.py file

There is a Teacher class defined in the file Teacher.py which includes __init__ and __repr__ special methods along with ORM class and instance methods for the following operations: 

    1. Creating and dropping tables for the Teachers class
    2. Creating a new instance (row) of the Teacher class
    3. Deleting an instance of Teacher
    4. Reading or selecting all teachera
    5. Selecting and reading the students of a teacher
    6. Selecting a teacher by ID
    
## helpers.py file

There is a helpers.py file which holds three helper functions, each used for validation. One is used for name validation to ensure the name entered is not empty. Grade validation is used to ensure that the grade entered is either "A", "B", "C", "D" or "F". And there is an ID validation to ensure the the ID entered is an integer.
