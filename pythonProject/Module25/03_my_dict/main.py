"""
В этой программе написан класс MyDict
Который работает так же как словарь за исключением метода get
который вместо None возращает 0, если не находит ключ
"""


class MyDict(dict):
    def get(self, key):
        if key in self.keys():
            return super().get(key)
        else:
            return 0


name_dict = MyDict({
    1: 1,
    2: 2,
    3: 3

})


print(name_dict.get(2))
print(name_dict.get(5))
