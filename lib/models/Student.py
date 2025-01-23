from database import CONNECTION, CURSOR




class Student:
    def __init__(self, name, grade, teacher_id):
        self.id = None
        self.name = name
        self.grade = grade
        self.teacher_id = teacher_id

    def __repr__(self):
        return f"My name is {self.name} and I am in grade {self.grade}"

# creating a table for students
    
    @classmethod
    def create_table(cls):
        
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                grade INTEGER,
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers(id)
            );
        """)
       
        CONNECTION.commit()

# dropping a table for students:

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS students;")
        CONNECTION.commit()

# creating a new instance (row) of the Student class (students table) and getting the newly auto generated ID from the instance

    def create(self):
        try:
            CURSOR.execute("INSERT INTO students (name, grade, teacher_id) VALUES (?, ?, ?)", [self.name, self.grade, self.teacher_id])
            CONNECTION.commit()
            self.id = CURSOR.execute("SELECT * FROM students ORDER BY id DESC LIMIT 1").fetchone()[0]
            return self
        except Exception as e:
            print(f"error adding student {e}")

# Deleting a student

    def delete(self):
        CURSOR.execute("DELETE from students WHERE id = ?", [self.id])
        CONNECTION.commit()

#reading or SELECTING all students
    @classmethod
    def get_all(cls):
        students = []
        rows = CURSOR.execute("SELECT * FROM students;").fetchall()
        for row in rows:
            student = cls(name=row[1], grade=row[2], teacher_id=row[3])
            student.id = row[0]
            students.append(student)
        return students
    
#Reading the student's teacher:

    @property
    def teacher_of_student(self):
        from models.Teacher import Teacher
        row = CURSOR.execute("SELECT * FROM teachers WHERE id = ?", [self.teacher_id]).fetchone()
        teacher = Teacher(name=row[1], years_experience=row[2])
        teacher.id = row[0]
        return teacher
    
#SELECT ... WHERE id ...

    @classmethod
    def select_by_id(cls, student_id):
        row = CURSOR.execute("SELECT * FROM students WHERE id = ?", [student_id]).fetchone()
        if row:
            student = cls(name=row[1], grade=row[2], teacher_id=row[3])
            student.id = row[0]
            return student
        return None
    
# Update student's grade

    def update_grade(self):
        CURSOR.execute("UPDATE students SET grade = ? WHERE id = ?", [self.grade, self.id])
        CONNECTION.commit()