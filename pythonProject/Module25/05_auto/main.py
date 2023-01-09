from math import fabs


# Автомобиль имеет координаты своего положения и угол, описывающий направление движения.
# Он может быть изначально поставлен в любую точку с любым направлением (конструктор),
# может проехать в выбранном направлении определённое расстояние и может повернуть,
# то есть изменить текущее направление на любое другое (передаём привет математике и формулам).
# Реализуйте класс автомобиля, а также класс, который будет описывать автобус.


class Car:
    """
    основной класс(машина) он  имеет координаты своего положения и угол, описывающий направление движения.
    Он может быть изначально поставлен в любую точку с любым направлением,
    может проехать в выбранном направлении определённое расстояние и может повернуть

    __length - в эту переменную записывается, расстояние которое проезжает автомобиль

    Аргументы:
    coordinate_x(int): координата х
    coordinate_y(int): координата y
    corner(int): угол под котором стоит автомобиль изначально(он может быть одним из 15 вариантов)

    В методе __init__ есть проверка на корректность передаваемых данных, в противном случае вызывается исключение

    """
    __length = 0

    def __init__(self, coordinate_x, coordinate_y, corner):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        if fabs(corner) in [0, 45, 90, 135, 180, 225, 270, 315, 360]:
            self.corner = corner
        else:
            raise Exception("угол указан не правильно")

    def move(self):
        """
        метод предназначенный для движения автомобиля

        В переменную direction записывается угол поворота, если угол передается корректный,
        то с помощью метода __angle_definition() в атрибут corner записывается новый угол, под которым будет ехать машина.
        в переменную distance записывается расстояние, которое проедет автомобиль.

        В зависимости от нового угла и дистанции атрибуты с координатами меняют своё значение
        """
        direction = int(input("Укажите угол поворота: "))
        if fabs(direction) in [0, 45, 90, 135, 180, 225, 270, 315, 360]:
            self.corner = self.__angle_definition(direction)
        else:
            raise Exception("угол указан не правильно")
        distance = int(input("укажите дистанцию"))
        self.__length += distance
        if self.corner in [0, 360, -180]:
            self.coordinate_x += distance
        elif self.corner in [45, -225]:
            self.coordinate_x += distance
            self.coordinate_y += distance
        elif self.corner in [90, -270]:
            self.coordinate_y += distance
        elif self.corner in [135, -315]:
            self.coordinate_x -= distance
            self.coordinate_y += distance
        elif self.corner in [180, -360]:
            self.coordinate_x -= distance
        elif self.corner in [225, -45]:
            self.coordinate_x -= distance
            self.coordinate_y -= distance
        elif self.corner in [270, -90]:
            self.coordinate_y -= distance
        elif self.corner in [315, -135]:
            self.coordinate_x += distance
            self.coordinate_y -= distance

    def __angle_definition(self, new_corner):
        """
        метод позволяющий определить в какую сторону с учётом нового угла поворота будет двигаться автомобиль
        :param new_corner: угол на который поворачиваем
        :type: int
        :rtype: int
        :return: возращается новый угол движения
        """
        if new_corner >= 0:
            if self.corner + new_corner <= 360:
                return self.corner + new_corner
            else:
                high = [self.corner, new_corner]
                high.sort(reverse=True)
                return 360 - (high[0] - high[1])
        elif new_corner < 0:
            if self.corner + new_corner <= - 360:
                return fabs(self.corner + new_corner) - 360
            else:
                return new_corner + self.corner

    def turn(self):
        """
        метод с помощью которого машина поварачивает
        """
        direction = int(input("Введите угол поворота"))
        if fabs(direction) in [0, 45, 90, 135, 180, 225, 270, 315, 360]:
            self.corner = self.__angle_definition(direction)
        else:
            raise Exception("угол указан не правильно")


class Bus(Car):
    """
    Дочерний класс(автобус). Он может впускать и выпускать пасажиров, может ездить и поворачивать

     Аргументы:
                coordinate_x(int): координата х
                coordinate_y(int): координата y
                corner(int): угол под котором стоит автобус изначально(он может быть одним из 15 вариантов)

    Атрибуты:
                money(int) - хранит количество заработанных денег
                passenger(int) - количество пассажиров
                __length(int) - расстояние, которое проехал автобус
                __capacity(int) - вместимость автобуса

    """
    money = 0
    passenger = 0
    __length = 0
    __capacity = 100

    def __init__(self, coordinate_x, coordinate_y, corner):
        super().__init__(coordinate_x, coordinate_y, corner)

    def log_in(self):
        """
        метод, впускающий людей в автобус

        amount(int) - переменная, которая хранит количество входящих пасажиров
        если вместимость автобуса позволяет впустить, ввденое пользователем количество пассажиров
        то изменяется количество пасажиров и денег
        """
        while True:
            amount = int(input("Сколько пассажиров заходит - "))
            if self.__capacity > amount + self.passenger:
                self.passenger += amount
                self.money += self.passenger * 26
                break
            else:
                print("Превышена вместимость автобуса\n"
                      f"Сейчас можно вместить до {self.__capacity - self.passenger} человек")

    def log_out(self):
        """
        метод, выпускающий людей из автобуса

        amount(int) - переменная, которая хранит количество выходящих пасажиров
        если число выходящих, меньше чем пассажиров, то уменьшаем число пассажиров и обрываем цикл
        в другом случае сообщаем пользователю о неккоректном вводе
        """
        while True:
            amount = int(input("Сколько пассажиров выходят - "))
            if self.passenger < amount:
                print("В автобусе нет такого колличество пассажиров, введите корректную информацию")
            else:
                self.passenger -= amount
                break

    def __str__(self):
        """
        магический метод предоставляющий информацию об автобусе
        """
        text = "координаты на которых стоит автобус - (x = {x} y = {y})\n" \
               "Угол по которому едет - {angle}\n" \
               "Количество пассажиров - {pas}\n" \
               "Пройденное расстоение - {__length}\n" \
               "заработано денег - {money} р.".format(
                x=self.coordinate_x, y=self.coordinate_y, angle=self.corner, pas=self.passenger, __length=self.__length,
                money=self.money)

        return text

    def move(self):
        """
        метод предназначенный для движения автобуса

        В переменную direction записывается угол поворота, если угол передается корректный,
        то с помощью метода __angle_definition() в атрибут corner записывается новый угол, под которым будет ехать автобус.
        в переменную distance записывается расстояние, которое проедет автомобиль.

        В зависимости от нового угла и дистанции атрибуы: coordinate_x, coordinate_y, money меняют своё значение
        """
        print("Угол может быть равен значениям: 0, 45, 90, 135, 180, 225, 270, 315, 360, -45,"
              "-90, -135, -180, -225, -270, -315, -360")
        direction = int(input("Укажите угол поворота: "))
        if fabs(direction) in [0, 45, 90, 135, 180, 225, 270, 315, 360]:
            self.corner = self._Car__angle_definition(direction)
        else:
            raise Exception("угол указан не правильно")
        distance = int(input("укажите дистанцию - "))
        self.__length += distance
        if self.corner in [0, 360, -180]:
            self.coordinate_x += distance
            self.money += self.passenger * 5 * distance
        elif self.corner in [45, -225]:
            self.coordinate_x += distance
            self.coordinate_y += distance
            self.money += self.passenger * 5 * distance
        elif self.corner in [90, -270]:
            self.coordinate_y += distance
            self.money += self.passenger * 5 * distance
        elif self.corner in [135, -315]:
            self.coordinate_x -= distance
            self.coordinate_y += distance
            self.money += self.passenger * 5 * distance
        elif self.corner in [180, -360]:
            self.coordinate_x -= distance
            self.money += self.passenger * 5 * distance
        elif self.corner in [225, -45]:
            self.coordinate_x -= distance
            self.coordinate_y -= distance
            self.money += self.passenger * 5 * distance
        elif self.corner in [270, -90]:
            self.coordinate_y -= distance
            self.money += self.passenger * 5 * distance
        elif self.corner in [315, -135]:
            self.coordinate_x += distance
            self.coordinate_y -= distance
            self.money += self.passenger * 5 * distance


def go():
    """
    Функция поездки автобуса

    bus(obj) - объект автобуса
    search(str) - вопрос на который отвечает пользователь

    В этой функции создана симуляции езды автобуса
    """
    bus = Bus(1, 1, 315)
    print(bus)
    print("Вы приехали на остановку!")
    bus.log_in()
    while True:
        print("Едем дальше!")
        bus.move()
        print("Вы приехали на остановку!")
        bus.log_out()
        bus.log_in()
        print(bus)
        search = input("Едем дальше?\n"
                       "1 - Да. 2 - нет.\n")
        if search == "1":
            continue
        else:
            break


go()
