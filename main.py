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
            i += 1
            return  (b/c)
    def __lt__(self, other):
        return self.averege() < other.averege()
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.averege()}' \
              f'\nКурсы в процесе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
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
    def __lt__(self, other):
        return self.averege() < other.averege()
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


# _____________________Создание экземплеров класса Student______________________________________
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_2 = Student('Sem', 'Carter', 'your_gender')
student_2.courses_in_progress += ['PHP']
student_2.finished_courses += ['Git']
student_3 = Student('Slava', 'Volkov', 'your_gender')
student_3.courses_in_progress += ['PHP']
student_3.finished_courses += ['Git']
student_4 = Student('Pol', 'Willam', 'your_gender')
student_4.courses_in_progress += ['Python']
student_4.finished_courses += ['Git']
# _____________________Создание экземплеров класса Lector______________________________________
lector_1 = Lector('Some', 'Buddy')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['Git']
lector_2 = Lector('Sam', 'Harald')
lector_2.courses_attached += ['PHP']
lector_2.courses_attached += ['Python']
# _____________________Создание экземплеров класса Reviewer______________________________________
Reviewer_1 = Reviewer('Gleb', 'Orlov')
Reviewer_1.courses_attached += ['Python']
Reviewer_2 = Reviewer('Sam', 'Davidson')
Reviewer_2.courses_attached += ['Git']
Reviewer_3 = Reviewer('Clarc', 'Kent')
Reviewer_3.courses_attached += ['PHP']
# __________________________Выстовление оценнок Лекторам_____________________________________________
student_1.rate_hw_lector(lector_1, 'Python', 8)
student_4.rate_hw_lector(lector_1, 'Python', 7)
student_2.rate_hw_lector(lector_2, 'PHP', 9)
student_3.rate_hw_lector(lector_2, 'PHP', 10)
# __________________________Выстовление оценнок Студентам_____________________________________________
Reviewer_1.rate_hw_student(student_1, 'Python', 10)
Reviewer_3.rate_hw_student(student_2, 'PHP', 9)
Reviewer_3.rate_hw_student(student_3, 'PHP', 7)
Reviewer_1.rate_hw_student(student_4, 'Python', 7)
# ________________________Вывод методов______________________
print(Reviewer_1)
print('')
print(Reviewer_2)
print('')
print(Reviewer_3)
print('')
print(lector_1)
print('')
print(lector_2)
print('')
print(lector_1 < lector_2)
print('')
print(student_1)
print('')
print(student_2)

# ____________________Создание списка Студентов и Лекторов_________________
list_student = [student_1, student_2, student_3, student_4]
list_lector = [lector_1, lector_2]
#_________________________________________Funchion for Student__________________________________
def averege_student (list_s, language_s):
    res = 0.0
    count_ln = 0
    for list in list_s:
        if language_s == (list.courses_in_progress[0]):
            res = res + list.averege()
            count_ln += 1
    return res/count_ln



print('')
print(averege_student (list_student, 'PHP'))
#_________________________________________Funchion for Lector__________________________________
def averege_lector (list_s, language_s):
    res = 0.0
    count_ln = 0
    for list in list_s:
        if language_s == (list.courses_attached[0]):
            res = res + list.averege()
            count_ln += 1
    return res/count_ln



print('')
print(averege_lector(list_lector, 'PHP'))


