# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
#
# Основной код:


class Primes:
    index = -1

    def __init__(self, num):
        self.number = num
        self.__count = 2
        self.__simply_num = []

    def __iter__(self):
        self.simply()
        return self

    def simply(self):
        for i in range(2, self.number + 1):
            self.__count += 1
            amount = 0
            for j in range(2, self.__count):
                if self.__count % j == 0:
                    amount += 1
            if amount == 0:
                self.__simply_num.append(self.__count)

    def __next__(self):

        self.index += 1
        if self.index < len(self.__simply_num):
            return self.__simply_num[self.index]
        else:
            raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem)

