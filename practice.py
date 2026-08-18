
#Relational Data

from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy import declarative_base, relationship, sessionmaker


engine = create_engine("sqlite:///:memory:", echo=False)
Base = declarative_base



class Teacher(Base):
    tablename = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # List of course objects taught by this teacher
    courses = relationship("Course", back_populates="teacher")


class Course(Base):
    coursename = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    # Courses belonging to a teacher
    teachers = relationship("Teacher", back_populates="course")

    #Foreign Key
    teacher_id = Column(Integer, ForeignKey("teachers.id"))


Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
db = session()


#add Teacher
new_teacher = Teacher(name="Dr.Smith")

db.add(new_teacher)
db.commit()


#two courses linked to the teacher
course1 = Course(title="Intro to python", teacher_id=new_teacher.id)
course2 = Course(title="Database Systems", teacher_id=new_teacher.id)

db.add(course1)
db.add(course2)
db.commit()


teacher = db.query(Teacher).filter().first()

