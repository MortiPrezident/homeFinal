# По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор,
# который также в цикле будет бесконечно выдавать значения.
#
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.



def infinity(num):

    for i in range(2, num):
        amount = 0
        for j in range(2, i):
            if i % j == 0:
                amount += 1
        if amount == 0 and i != 2:
            yield i


# class СountIterator:
#     __count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__count += 1
#         if self.__count == 1000000:
#             raise StopIteration
#         return self.__count - 1
#
#
# my_iter = СountIterator()
# for i_elem in my_iter:
#     print(i_elem)

my_gen = infinity(50)
for j_elem in my_gen:
    print(j_elem)