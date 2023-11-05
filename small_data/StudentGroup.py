from abc import ABC
from small_data.Student import Student
from typing import Iterable, List


class StudentGroup(Iterable[Student], ABC):

    _students: List[Student]

    def __init__(self, students: List[Student]):
        self._students = students

    """
    Метод получения студента
    """
    def getStudents(self):
        return self._students

    """
    Строчный метод вывода информации о студенте
    """
    def __str__(self):
        return "StudentGroup" + "students=" + str(self._students)

    """
    Итерация
    """
    def __iter__(self):
        return self
