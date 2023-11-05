from service.StudyGroupService import StudyGroupService
from view.StudentView import StudentView
from view.TeacherView import TeacherView


class StudyGroupController:

    __study_service: StudyGroupService = []

    __student_view: StudentView = []

    __teacher_view: TeacherView = []

    def CreateGroup(self, teacher, students):
        self.__study_service.createStudyGroup(teacher, students)
        self.__student_view.sendOnConsoleUserGroup(self.__study_service.getStudyGroup())
        self.__teacher_view.sendOnConsoleUserGroup(self.__study_service.getStudyGroup())


