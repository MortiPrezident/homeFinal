# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать свои или запросить их у пользователя)
# и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.

class Student:
    def __init__(self, name, number, level):
        self.name = name
        self.number = number
        self.level = level
        self.average = sum(self.level) / 5

    def info(self):
        print(f"ФИ - {self.name}\nГруппа - {self.number}\nСредний бал - {self.average}")


with open("student_info.txt", "r", encoding="utf-8") as file:
    students = list()
    for i_elem in file:
        info_list = i_elem.split()
        name_surname = info_list[0] + " " + info_list[1]
        group = info_list[2]
        evaluations = [int(i_num) for i_num in info_list[3:]]
        students.append(Student(name_surname, group, evaluations))


def my_key(ave):
    return ave.average


students = sorted(students, key=my_key, reverse=True)
for student in students:
    student.info()
