from collections.abc import Iterable


number = int(input("Введите число: "))


class MyIter:
    def __init__(self, num: int):
        self.__count = 0
        self.number = num

    def __iter__(self):
        return self

    def __next__(self) -> Iterable[int]:
        if self.__count < self.number:
            self.__count += 1
            return self.__count ** 2
        else:
            raise StopIteration


my_iter = MyIter(number)

for elem in my_iter:
    print(elem)


def my_gen(num: int):
    for i_elem in range(1, num + 1):
        yield i_elem ** 2


print()

for gen_elem in my_gen(number):
    print(gen_elem)

print()

expression = (elem ** 2 for elem in range(1, number + 1))

for elem in expression:
    print(elem)