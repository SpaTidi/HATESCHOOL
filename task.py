from datetime import *
from collections import defaultdict

class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        super().__init__(message)

class Homework:
    def __init__(self, text, numOfDays):
        self.text = text
        self.deadline = timedelta(numOfDays)
        self.created = datetime.now()
    
    def is_active(self):
        return datetime.now() < self.created + self.deadline

class HomeworkResult:
    def __init__(self, homework, solution, author):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.now()

class People():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student(People):
    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError()

class Teacher(People):
    homework_done = defaultdict(set)

    def create_homework(self, text, numOfDays):
        return Homework(text, numOfDays)

    def check_homework(self, homeworkResult):
        if len(homeworkResult.solution) > 5:
            self.homework_done[homeworkResult.homework].add(homeworkResult)
            return True
        else:
            return False
    
    @classmethod
    def reset_results(cls, homework=None):
        if homework:
            cls.homework_done.pop(homework, None)
        else:
            cls.homework_done.clear()

if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print(Exception)
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()