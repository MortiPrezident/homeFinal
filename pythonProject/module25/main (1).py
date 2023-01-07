# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).

# Также есть два дочерних класса:

# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению. 
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).

class Unit:
    
    def __init__(self):
        self.point = 100
        
    def damage(self, damag):
        self.point -= damag
        print(f"Ваш юнит получил урон, у вас осталось{self.point}hp")
        
        
class Soldat(Unit):
    
    def __init__(self, name):
        super().__init__()
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print("pohol nahui")
            
            
class Grazhdanin(Unit):
    
    def __init__(self, name):
        super().__init__()
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        
        if name.isalpha():
            self.__name = name
        else:
            print("pohol nahui")
            
    def damage(self, damags):
        self.point -= damags 
        print(f"Ваш юнит получил урон, у вас осталось {self.point}hp")

            
soldat = Soldat("Valera")
man = Grazhdanin("Маша")

soldat.damage(20)
man.damage(10)
