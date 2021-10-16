class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw_lector(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades_lector:
                lector.grades_lector[course] += [grade]
            else:
                lector.grades_lector[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lector = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']



cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached)
cool_lector = Lector('Some', 'Buddy')
cool_lector.courses_attached += ['Python']

best_student.rate_hw_lector(cool_lector, 'Python', 7)
best_student.rate_hw_lector(cool_lector, 'PHP', 8)

cool_mentor.rate_hw_student(best_student, 'Python', 10)
cool_mentor.rate_hw_student(best_student, 'Python', 10)
cool_mentor.rate_hw_student(best_student, 'Python', 10)

print(best_student.grades)
print(cool_lector.grades_lector)