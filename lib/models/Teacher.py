from database import CONNECTION, CURSOR
from models.Student import Student

class Teacher: 
    def __init__(self, name, years_experience):
        self.id = None
        self.name = name
        self.years_experience = years_experience

    def __repr__(self):
        return f"My name is {self.name} and I have been teaching for {self.years_experience} years."


# Creating a table for teachers
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS teachers(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                years_experience INTEGER
            );
        """)
       
        CONNECTION.commit()

# dropping a table for teachers

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS teachers;")
        CONNECTION.commit()

# creating a new instance (row) of the Teacher class (in teachers table) and getting the newly auto generated ID from the instance

    def create(self):
        CURSOR.execute("INSERT INTO teachers (name, years_experience) VALUES (?, ?)", [self.name, self.years_experience])
        CONNECTION.commit()
        self.id = CURSOR.execute("SELECT * FROM teachers ORDER BY id DESC LIMIT 1").fetchone()[0]
        return self
    
#deleting an instance of "Teacher"

    def delete(self):
        CURSOR.execute("DELETE from teachers WHERE id = ?", [self.id])
        CONNECTION.commit()

#reading or SELECTING all teachers
    @classmethod
    def get_all(cls):
        teachers = []
        rows = CURSOR.execute("SELECT * FROM teachers;").fetchall()
        for row in rows:
            teacher = cls(name=row[1], years_experience=row[2])
            teacher.id = row[0]
            teachers.append(teacher)
        return teachers
    
#reading the students "belonging" to a teacher

    @property
    def students_of_teacher(self):
        my_students = []
        rows = CURSOR.execute("""SELECT students.id, students.name, students.grade, students.teacher_id
            FROM students
            JOIN teachers ON students.teacher_id = teachers.id
            WHERE teachers.id = ?""", [self.id]).fetchall()
        for row in rows:
            student = Student(name=row[1], grade=row[2], teacher_id=row[3])
            student.id = row[0]
            my_students.append(student)
        return my_students
    
#SELECT ... WHERE id ...

    @classmethod
    def select_by_id(cls, teacher_id):
        row = CURSOR.execute("SELECT * FROM teachers WHERE id = ?", [teacher_id]).fetchone()
        if row:
            teacher = cls(name=row[1], years_experience=row[2])
            teacher.id = row[0]
            return teacher
        return None