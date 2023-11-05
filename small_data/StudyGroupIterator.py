from small_data.Student import Student
from small_data.StudyGroup import StudyGroup
from small_data.Teacher import Teacher
from typing import List

from small_data.TeachersGroup import TeachersGroup


class StudyGroupIterator(Teacher, Student):

    __counter: int

    __teacher = List[Teacher]

    __students = List[Student]

    def __init__(self, study_group: StudyGroup):
        self.__teacher = study_group.getUsers()
        self.__students = study_group.getUsers()
        self.__counter = 0

    """
    Метод получения следующего значения счётчика по отношению к преподавателю
    """
    def hasNext(self):
        return self.__counter < len(self.__teacher or self.__students)

    """
    Метод создания следующего значения счётчика по отношению к преподавателю
    """
    def next(self):
        if not self.hasNext():
            return None
        self.__counter += 1
        return self.__teacher[self.__counter - 1] and self.__students[self.__counter - 1]

