from random import random


class RandomAmount:

    def __init__(self):
        self.__another = random()

    def __iter__(self):
        self.number = int(input('кол-во элементов: '))
        self.__count = -1
        return self

    def __next__(self):
        self.__count += 1
        if self.__count == self.number:
            raise StopIteration
        else:
            self.__another += random()
            return self.__another


obj = RandomAmount()

for i in obj:
    print("{:.3f}".format(i))

for j in obj:
    print("{:.3f}".format(j))