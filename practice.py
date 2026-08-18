
#Relational Data

from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine("sqlite:///:memory:", echo=False)
Base = declarative_base()



class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # List of course objects taught by this teacher
    courses = relationship("Course", back_populates="teacher")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

     #Foreign Key
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    

    # Courses belonging to a teacher
    teacher = relationship("Teacher", back_populates="courses")

   

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
db = session()


#add Teacher
new_teacher = Teacher(name="Jordan")

db.add(new_teacher)
db.commit()


#two courses linked to the teacher
course1 = Course(title="Intro to python", teacher_id=new_teacher.id)
course2 = Course(title="Database Systems", teacher_id=new_teacher.id)
course3 = Course(title="Machine Learning", teacher_id=new_teacher.id)

db.add(course1)
db.add(course2)
db.add(course3)
db.commit()


#Fetch teacher Jordan from DB
teacher = db.query(Teacher).filter(Teacher.id==1).first()

print(f"Teacher: {teacher.name}")
print("Courses taught:")

for course in teacher.courses:
    print(f" - {course.title}")


