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
    def averege(self):
        i = 0
        b = 0
        c = 0
        a = list(self.grades.values())
        while i < len(a):
            b = b + sum(a[i])
            c = c + len(a[i])
            i = i + 1
            return  (b/c)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.averege()}' \
              f'\nКурсы в процесе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):
    b = 0
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lector = {}

    def averege(self):
        i = 0
        b = 0
        c = 0
        a = list(self.grades_lector.values())
        while i < len(a):
            b = b + sum(a[i])
            c = c + len(a[i])
            i = i + 1
            return  (b/c)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.averege()}'
        return res


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
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['PHP']



cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['PHP']
cool_lector = Lector('Some', 'Buddy')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['PHP']


best_student.rate_hw_lector(cool_lector, 'Python', 5)
best_student.rate_hw_lector(cool_lector, 'Python', 5)
best_student.rate_hw_lector(cool_lector, 'PHP', 5)

cool_mentor.rate_hw_student(best_student, 'PHP', 10)
cool_mentor.rate_hw_student(best_student, 'Python', 10)
cool_mentor.rate_hw_student(best_student, 'Python', 10)






print(cool_mentor)
print('')
print(cool_lector)
print('')
print(best_student)