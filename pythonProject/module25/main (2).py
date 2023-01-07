# Иногда для реализации дочерних классов используется так называемый класс-роль,
# где также описываются общие атрибуты и методы, но в программе инициализируются
# объекты только дочерних классов, а базовый класс-роль не трогается. К примеру,
# что общего у бабочки и ракеты? Они обе могут летать и приземляться. 

# Реализуйте класс «Может летать». 
# Атрибуты:
# Высота = 0.
# Скорость = 0.
# Методы:
# Взлететь (в теле прописать pass).
# Лететь (в теле прописать pass).
# Приземлиться (установить высоту и скорость в значение 0).
# Вывести высоту и скорость на экран.
 
# Затем реализуйте два дочерних класса: 
# «Бабочка», который может:
# Взлететь (высота = 1).
# Лететь (скорость = 0.5).
# «Ракета», которая может:
# Взлететь (высота = 500, скорость = 1000).
# Приземлиться (высота = 0, взрыв).
# Взорваться (тут уже что угодно).

class CanFly():
    __height = 0
    __speed = 0
    
    def zoom(self):
        pass
    
    def fly(self):
        pass
    
    def fly_land(self):
        self.__height = 0
        self.__speed = 0        
    
    def set_height(self, didgit):
        self.__height = didgit
    
    def set_speed(self, didgit):
        self.__speed = didgit
        
    def info(self):
        print('speed = {speed}\nHeight = {height}'.format(speed=self.__speed, height=self.__height))
        
        
class Butterfly(CanFly):
    
    def zoom(self):
        self.set_height(1)
        
        
    def fly(self):
        self.set_speed(0.5)
        
class Rocet(CanFly):
    
        def zoom(self):
            self.set_height(500) 
            self.set_speed(1000)
            print("letit")    
        def fly_land(self):
            self.set_height(0)
            print("BOOM BOOM BOOM")
            
buter = Butterfly()
buter.zoom()
buter.fly()
buter.info()
rok = Rocet()
rok.zoom()
rok.info()
rok.fly_land()
rok.info()

        
        