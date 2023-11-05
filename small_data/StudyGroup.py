from abc import ABC
from typing import Iterable, List

from small_data.Student import Student
from small_data.StudentGroup import StudentGroup
from small_data.Teacher import Teacher


class StudyGroup(Iterable[Teacher], List[StudentGroup], ABC):

    _teacher: Teacher

    _students: StudentGroup

    def __init__(self, teacher: Teacher, students: StudentGroup):
        self._teacher = teacher
        self._students = students

    def getUsers(self):
        return self._students or self._teacher

    def __str__(self):
        return f'Study group: \n Teacher = {self._teacher} \n Students = {self._students}'
