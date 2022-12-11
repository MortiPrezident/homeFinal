# У родителя есть:
#
# Имя.
# Возраст.
# Список детей.
# И он может:
#
# Сообщить информацию о себе.
# Успокоить ребёнка.
# Покормить ребёнка.

# У ребёнка есть:
# Имя.
# Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
# Состояние спокойствия.
# Состояние голода.
# Реализация состояний на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-нибудь ещё интереснее.

class Parents:
    def __init__(self, name="Ivan", age=36, child_list=None):
        if child_list is None:
            self.child_list = [Child()]
        else:
            self.child_list = child_list
        self.name = name
        self.age = age
        if self.age < 17:
            print("Некорректный возраст у родителя, автоматически установлен минимальный возраст")
            self.age = 17
        for child in self.child_list:
            if self.age - child.age < 16:
                print("Некорректный возраст у ребенка, автоматически установлен минимальный возраст")
                child.age = 1

    def info(self):
        print("Имя:  {}\nВозраст: {}\nДети:"
              .format(self.name, self.age))
        for child in self.child_list:
            print("Имя:  {}\nВозраст: {}\nСостояние спокойствия: {}\nCостояние голода: {}"
                  .format(child.name, child.age, child.condition_calm, child.condition_hungry))

    def calm(self, child_name):
        for child in self.child_list:
            if child.name.lower() == child_name.lower():
                child.condition_calm = True
                print(f"Вы успокоили ребенка с именем {child_name}")
                break
        else:
            print("У вас нет ребенка с таким именем")

    def feed(self, child_name):
        for child in self.child_list:
            if child.name.lower() == child_name.lower():
                child.condition_hungry = True
                print(f"Вы успокоили ребенка с именем {child_name}")
                break
        else:
            print("У вас нет ребенка с таким именем")


class Child:
    def __init__(self, name="Egor", age=1, condition_calm=False, condition_hungry=False):
        self.name = name
        self.age = age
        self.condition_calm = condition_calm
        self.condition_hungry = condition_hungry


ivan = Parents()
ivan.info()
ivan.calm("egor")
ivan.info()
