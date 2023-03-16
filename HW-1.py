class Student:
    
#  инициализация экземпляра класса, задаем имя, фамилию, пол     
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.current_courses = []
        self.marks = {}

#  реализация возможности выставления оценок лектору        
    def take_mark(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and course in lecturer.course_attached and course in self.current_courses:
            if course in lecturer.marks:
                lecturer.marks[course] += [mark]
            else:
                lecturer.marks[course] = [mark]
        else:
            print('ошибка, нет такого лектора')

#  подсчет среднего балла студента. 
#  cначала находим средний балл по каждому курсу, затем общий средний балл            
    def get_average(self):
        average_mark = None
        res = 0
        for i in self.marks:
            res += sum(self.marks[i]) / len(self.marks[i])
        if not len(self.marks) == 0:
            average_mark = res / len(self.marks)
        return average_mark

# изменение вывода магического метода __str__   
    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average()}\nКурсы в процессе изучения: {', '.join(self.current_courses)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return res


class Mentor:
   # course_marks_dict = {'English': [], 'Git': [], 'Python': []}
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.course_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.marks = {}

    def __str__(self):
        res = f"Преподаватель\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Student.get_average(self)}"
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
        
    def __str__(self):
        res = f"Преподаватель\nИмя: {self.name}\nФамилия: {self.surname}"
        return res

    def take_marks(self, student, course, mark):
        if isinstance(student, Student) and course in student.current_courses and course in self.course_attached:
            if course in student.marks:
                student.marks[course] += [mark]
             #   self.course_marks_dict[course].append(mark)
            else:
                student.marks[course] = [mark]
            #    self.course_marks_dict[course] = [mark]
        else:
            return print('ошибка, нет такого курса или студента')

            
#  Функция поиска среднего балла на курсе, зная список студентов на входе:            
def overal_average_mark_stud(course, student_list):
    marks_list = []
    for student in student_list:
        marks_list += student.marks[course]
    res = sum(marks_list) / len(marks_list)
    return f'Cредний балл студентов на курсе "{course}" - {res}'


#  Функция поиска средней оценки луктора на курсе, зная список лекторов на входе: 
def overal_average_mark_lect(course, lecturers_list):
    marks_list = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer):
            marks_list += lecturer.marks[course]
        else:
            return 'Нет такого лектора в списке'
    res = sum(marks_list) / len(marks_list)
    return f'Cредняя оценка лекторов на курсе "{course}" - {res}'

#      Для упрощения, примем, что:
#        - всего в базе два студента (у каждого по 2 курса в процессе изучения и один завершенный)
#        - всего в базе два преподавателя, лектор и ревьюер (пусть оба преподают и проверяют на всех курсах)
#        - студент №1 поставил оценки 10, 9 за первый курс и 7, 8 за ивторой, а также получил за дз оценки 10, 9 за первый курс  и 9, 8 за второй
#        - студент №2 не ставил оценки, но получил 8 и 7 за свой первый  курс и 10 за второй

#  Назначаем студентов:
maksim = Student('Maksim', 'Shapaev', 'male')
maksim.current_courses += ['Python']
maksim.current_courses += ['Git']
maksim.finished_courses += ['English']
olga = Student('Olga', 'Petrova', 'female')
olga.current_courses += ['Python']
olga.current_courses += ['Git']
olga.finished_courses += ['English']

#  Назначаем преподавателей:
oleg = Lecturer('Oleg', 'Bulygin')
oleg.course_attached += ['Git']
oleg.course_attached += ['Python']
alena = Reviewer('Alena', 'Batitskaya')
alena.course_attached += ['Git']
alena.course_attached += ['Python']

#  Выставляем оценки лекторам:
maksim.take_mark(oleg, 'Git', 10)
maksim.take_mark(oleg, 'Git', 9)
maksim.take_mark(oleg, 'Python', 7)
maksim.take_mark(oleg, 'Python', 8)

#  Выставляем оценки студентам:
alena.take_marks(maksim, 'Git', 10)
alena.take_marks(maksim, 'Git', 9)
alena.take_marks(olga, 'Git', 8)
alena.take_marks(olga, 'Git', 7)
alena.take_marks(maksim, 'Python', 9)
alena.take_marks(maksim, 'Python', 8)
alena.take_marks(olga, 'Python', 10)

#  Вывод личных дел после заполнения:
print(maksim)
print()
print(olga)
print()
print(oleg)
print()
print(alena)
print()

#  средний балл студентов по курсу:
print(overal_average_mark_stud('Git', [maksim, olga]))
print(overal_average_mark_stud('Python', [maksim, olga]))

#  средняя оценка лекторов по курсу::
print(overal_average_mark_lect('Git', [oleg]))
print(overal_average_mark_lect('Python', [oleg]))
print(overal_average_mark_lect('Git', [alena]))

# End
