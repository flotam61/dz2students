from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        ow1 = mean(self.grades[k] for k in self.grades)
        if not isinstance(self, Student):
            print()
        return f"Имя: {self.name}, фамилия {self.surname}. " \
               f"Средняя оценка за дз: {ow1}. " \
               f"Курсы в процессе изучения: {self.courses_in_progress}. " \
               f"Завершенные курсы {self.finished_courses}"

    def __lt__(self, name):
        ow1 = mean(self.grades[k] for k in self.grades)
        ow2 = mean(name.grades[k] for k in name.grades)
        if not isinstance(self, Student):
            print("Сравнивайте студентов!")
            return
        if ow1 > ow2:
            print(self.name, "учиться лучше. Средняя оценка ", ow1, ".")
        elif ow1 < ow2:
            print(self.name, "учиться хуже. Средняя оценка ", ow1, ".")
        return

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def ratelector(self, lecture, cource, grade):
        if isinstance(lecture, Lecture) and cource in self.courses_in_progress and cource in lecture.courses_attached:
            if cource in lecture.students_grade:
                lecture.students_grade[cource] += grade
            else:
                lecture.students_grade[cource] = grade
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.students_grade = {}

    def __lt__(self, name):
        ow1 = mean(self.students_grade[k] for k in self.students_grade)
        ow2 = mean(name.students_grade[k] for k in name.students_grade)
        if not isinstance(self, Lecture):
            print("Сравнивайте лекторов!")
            return
        if ow1 > ow2:
            print(self.name, "оценки лучше. Средняя оценка ", ow1, ".")
        elif ow1 < ow2:
            print(self.name, "оценки хуже. Средняя оценка ", ow1, ".")
        return

    def __str__(self):
        ow1 = mean(self.students_grade[k] for k in self.students_grade)
        if not isinstance(self, Lecture):
            print()
        return f"Имя: {self.name}, фамилия {self.surname}. " \
               f"Средняя оценка за лекции: {ow1} "


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        if not isinstance(self, Reviewer):
            print()
            return
        return f" Имя: {self.name}, Фамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'Man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
new_student = Student("Alex", "Eriksen", "Man")
new_student.courses_in_progress += ['Python']
new_student.courses_in_progress += ['Git']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
new_mentor = Mentor("Vika", "Tam")
new_mentor.courses_attached += ['Git']

new_reviewer = Reviewer("Max", "Pro")
new_reviewer.courses_attached += ['Python']
new_reviewer.courses_attached += ['Git']
best_reviewer = Reviewer("Oleg", "Pro")
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Git']
new_reviewer.rate_hw(best_student, 'Python', 10)
new_reviewer.rate_hw(best_student, 'Git', 8)
new_reviewer.rate_hw(new_student, 'Python', 9)
new_reviewer.rate_hw(new_student, 'Git', 6)

new_lecture = Lecture("Ivan", "Ivanov")
new_lecture.courses_attached += ["Python"]
new_lecture.courses_attached += ['Git']
best_lecture = Lecture("Dima", "Vasilevskiy")
best_lecture.courses_attached += ["Python"]
best_lecture.courses_attached += ['Git']
best_student.ratelector(new_lecture, "Python", 10)
best_student.ratelector(new_lecture, "Git", 9)
new_student.ratelector(best_lecture, "Python", 8)
new_student.ratelector(best_lecture, "Git", 3)

students = [new_student, best_student]
lectors = [new_lecture,best_lecture]


def midgrades_students(students, courses):
    if courses == "Python":
        midg = []
        for mid in students:
            midg.append(mid.grades["Python"])
        return print("Средняя оценка за домашние задания по всем студентам в рамках курса", courses, mean(midg))
    elif courses == "Git":
        midg = []
        for mid in students:
            midg.append(mid.grades["Git"])
        return print("Средняя оценка за домашние задания по всем студентам в рамках курса", courses, mean(midg))


def midgrades_lectors(lectors, courses):
    if courses == "Python":
        midg = []
        for mid in lectors:
            midg.append(mid.students_grade["Python"])
        return print("Средняя оценка за лекции всех лекторов в рамках курса", courses, mean(midg))
    elif courses == "Git":
        midg = []
        for mid in lectors:
            midg.append(mid.students_grade["Git"])
        return print("Средняя оценка за лекции всех лекторов в рамках курса", courses, mean(midg))

