from typing import List

from small_data.Student import Student
from small_data.StudyGroup import StudyGroup
from small_data.Teacher import Teacher


class StudyGroupService:

    __study_group: StudyGroup

    def createStudyGroup(self, teacher: List[Teacher], students: List[Student]):
        self.__study_group = StudyGroup(teacher, students)

    def getStudyGroup(self):
        return self.__study_group
