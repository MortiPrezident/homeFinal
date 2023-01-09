class Person:
    """
    Базовый класс описывающий человека

    аргументы:
            name(str) - имя человека
            surname(str) - фамилия человека
            age(int) - возраст человека

    """

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        """
        геттер  для получения имени
        :return: __name
        :rtype: str
        """
        return self.__name

    def get_surname(self):
        """
        геттер  для получения фамилии
        :return: __surname
        :rtype: str
        """
        return self.__surname

    def get_age(self):
        """
        геттер  для получения возраста
        :return: __age
        :rtype: int
        """
        return self.__age

    def set_name(self, name):
        """
        сеттер для изменения имени

        :param name: имя
        :type: str
        """
        if name.isalpha():
            print("имя {name_one} изменено на {name_second}".format(name_one=self.__name, name_second=name))
            self.__name = name
        else:
            print("Имя должно состоять только из букв")

    def set_age(self, age):
        """
        сеттер для изменения возраста

        :param age: возраст
        :type: int
        """
        if age.isdidgit():
            print("Возраст {} изменен на {}".format(self.__age, age))
        else:
            print("Возраст должен состоять только из цифр")

    def set_surname(self, surname):
        """
        сеттер для изменения фамилии

        :param surname: фамилия
        :type: str
        """
        if surname.isalpha():
            print("фамилия {name_one} изменено на {name_second}".format(name_one=self.__surname, name_second=surname))
            self.__surname = surname
        else:
            print("фамилия должна состоять только из букв")

    def __str__(self):
        """
        магический метод, который возращает имя, фамилию и возраст человека
        """
        return "Имя - {}\nФамилия - {}\nВозраст - {}".format(self.__name, self.__surname, self.__age)


class Employee(Person):
    """
    Дочерний класс "работник"

    аргументы:
            name(str) - имя человека
            surname(str) - фамилия человека
            age(int) - возраст человека
    методы:
        wage() - метод предназначенный для расчёта заработной платы, у каждого дочернего класса он переписан
        __str__() - магический метод, который помимо информации родителя также выводит заработную плату
    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def wage(self):
        pass

    def __str__(self):
        return super().__str__() + "\nзаработная плата {wage}".format(wage=self.wage())


class Manager(Employee):
    """
    дочерний класс  "менеджер"
    аргументы:
            name(str) - имя человека
            surname(str) - фамилия человека
            age(int) - возраст человека

    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def wage(self):
        """
        метод возращающий значение заработной платы, она у менеджера 13000
        """
        return 13000


class Agent(Employee):
    """
    дочерний класс  "Агент"

    __salary - сумма оклада агента
    __sales - сумма продаж агента

    аргументы:
            name(str) - имя человека
            surname(str) - фамилия человека
            age(int) - возраст человека
            sales(int) - продажи агента

    """

    __salary = 5000

    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales

    def wage(self):
        """
        метод предназначенный для расчёта заработной платы
        Заработная плата Agent определяется как оклад 5000 + 5% от объёма продаж
        """
        return self.__salary + self.__sales * 0.05

    def get_salary(self):
        """
        геттер для получение информации об окладе агента
        :return: self.__salary
        :rtype: int
        """
        return self.__salary

    def set_salary(self, new_salary):
        """
        сеттер предназначенный для изменения оклада

        :param new_salary: новый оклад
        :type:int
        """
        if new_salary.isdidgit():
            print("Оклад изменён")
            self.__salary = new_salary
        else:
            print("Оклад должен быть числовым значением")

    def get_sale(self):
        """
        геттер для получение информации об продажах агента

        :return: self.__sales
        :rtype: int
        """
        return self.__sales

    def set_sale(self, sale_second):
        """
        сеттер предназначенный для изменения информации о продажах агента
        :type: int
        """
        if sale_second.isdidgit():
            print("Объем продаж изменён")
            self.__sales = sale_second
        else:
            print("Объем продаж должен быть числовым значением")


class Worker(Employee):
    """
    Дочерний класс (работник)

    __hour - атрибут, который хранит количество отработанных работником часов

    аргументы:
            name(str) - имя человека
            surname(str) - фамилия человека
            age(int) - возраст человека
            hout(int) - часы работы

    """

    def __init__(self, name, surname, age, hour):
        super().__init__(name, surname, age)
        self.__hour = hour

    def wage(self):
        """
        метод wage() предназначен для расчета заработной платы
        заработная плата работника определяется как 100 * число отработанных часов
        :rtype: int
        """
        return self.__hour * 100

    def get_hour(self):
        """
        геттер, возращающий количество отработанных работником часов

        :return: self.__hour
        :rtype:int
        """
        return self.__hour

    def set_hour(self, new_hour):
        """
        сеттер предназначенный для изменения количества отработанных часов

        :param new_hour: новое количество часов
        :type: int
        """
        if new_hour.isdidgit():
            print("Число отработанных часов изменено")
            self.__hour = new_hour
        else:
            print("Часы должны быть числового типа")


person_list = [Manager("Иван", "Иванов", 25), Manager("Иван", "Иванов", 35), Manager("Игорь", "Иванов", 25),
               Agent("Александр", "Нечепоренко", 25, 18000), Agent("Александр", "Нечепоренко", 18, 50000),
               Agent("Александр", "Богатов", 45, 650000), Worker("Павел", "Королев", 22, 180),
               Worker("Алексей", "Королев", 22, 160), Worker("Игорь", "Королев", 22, 400)
               ]

for person in person_list:
    """
    цикл который проходи по элементам списка,
    которые являются объектами и печатает информацию об этих объектах
    """
    print(person)
    print()
