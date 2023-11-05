from small_data.User import User


class Teacher(User):

    __teacher_id = []

    def __init__(self, first_name, surname, patronymic, teacher_id = None):
        super().__init__(first_name, surname, patronymic)
        self.__teacher_id = teacher_id

    def getTeacherId(self):
        return self.__teacher_id


    """
    Строчный метод для вывода информации о студенте в консоль
    """
    def __str__(self):
        return (f"Teacher: firstName='{super().getFirstName()}', "
                f"surName='{super().getSurname()}', patronymic='{super().getPatronymic()}', TeacherID = {self.__teacher_id}")
