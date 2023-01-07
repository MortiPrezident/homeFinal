class Person:
    __count = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.__count += 1
        
    def __str__(self):
        return "Имя: {}\nAge: {}".format(self.__name, self.__age)
        
        
    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Ne dopustimi voszrast")

man = Person("Andrey", 10)
man.set_age(15)
print(Person._Person__count)
print(man._Person__age)