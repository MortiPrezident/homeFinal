# Реализуйте итератор-счётчик,
# который не принимает никаких атрибутов и имеет только один статический атрибут — счётчик.
# Итератор увеличивает счётчик и возвращает предыдущее значение. У вас должен получиться бесконечный итератор.
#
# То есть при вызове такого кода в основной программе


class СountIterator:
    __count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__count += 1
        if self.__count == 1000000:
            raise StopIteration
        return self.__count - 1


my_iter = СountIterator()

for i_elem in my_iter:
    print(i_elem)

