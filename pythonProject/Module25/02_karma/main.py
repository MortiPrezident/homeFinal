from random import randint

"""
В данной программе описаны собственные классы(исключения)
классы: 
    KillError - ошибка убийства ;
    DrunkError - ошибка отравления водой;
    CarCrashError - ошибка автокатастрофы;
    GluttonyError - Ошибка обжорства;
    DepressionError - Ошибка депрессии.
    
У всех этих классво есть скрытый атрибут: 
        __message - в него записывается название ошибки


Так же у всех классов есть методы:
        get_message - геттер с помощью которого получаем информацию о переменной __message
        __str__ - магический метод, который возращает тект нашей ошибки
"""

KARMA = 500


class KillError(Exception):
    def __init__(self):
        self.__message = "KillError"

    def get_message(self):
        return self.__message

    def __str__(self):
        return f"Буддиста убили"


class CarCrashError(Exception):
    def __init__(self):
        self.__message = "CarCrashError"

    def get_message(self):
        return self.__message

    def __str__(self):
        return f"Буддист умер от автокатастрофы"


class DrunkError(Exception):
    def __init__(self):
        self.__message = "DrunkError"

    def get_message(self):
        return self.__message

    def __str__(self):
        return f"Буддист умер от водяного отравления"


class GluttonyError(Exception):
    def __init__(self):
        self.__message = "GluttonyError"

    def get_message(self):
        return self.__message

    def __str__(self):
        return f"Буддист умер от переедания"


class DepressionError(Exception):
    def __init__(self):
        self.__message = "DepressionError"

    def get_message(self):
        return self.__message

    def __str__(self):
        return f"Буддист умер от депрессии"


def one_day():
    """
    Функция с вероятность 1 к 10 вызывает одно из пяти исключений,
    Если исключение не вызвано карма увеличивается на число от (1 до 7)
    Ксли карма больше или равна константе KARMA(то количество которое буддист должен набрать),
    то программа завершается
    переменные:
                firs_carma - переменная в которой хранится текуoее количество кармы
                car - объект класса CarCrashError()
                kill - объект класса KillError()
                drunk - объект класса DrunkError()
                gluttony - объект класса GluttonyError()
                depression - объект класса DepressionError()


    """
    firs_carma = 0
    car = CarCrashError()
    kill = KillError()
    drunk = DrunkError()
    gluttony = GluttonyError()
    depression = DepressionError()
    with open("karma.log", "a", encoding="utf-8") as file:
        while True:
            if firs_carma >= KARMA:
                print("Буддист набрал нужное колличество кармы!")
                break
            if randint(1, 10) == 1:
                error = randint(1, 5)
                if error == 1:
                    file.write(car.get_message() + '\n')
                    raise CarCrashError
                elif error == 2:
                    file.write(kill.get_message() + '\n')
                    raise KillError
                elif error == 3:
                    file.write(drunk.get_message() + '\n')
                    raise DrunkError
                elif error == 4:
                    file.write(gluttony.get_message() + '\n')
                    raise GluttonyError
                elif error == 5:
                    file.write(depression.get_message() + '\n')
                    raise DepressionError
            else:
                firs_carma += randint(1, 7)


one_day()
