# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть
# своя модель, и каждый может сделать два действия: сообщить свою модель и идти по воде. 

# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю.
# У него есть ещё два действия: погрузить и выгрузить груз с корабля. 

# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся
# вместе с моделью. Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.

# Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты
# и методы в отдельный класс «Корабль» и используйте наследование. Не забудьте про функцию super в дочерних классах.




class Ship:
    def __init__(self, model):
        self.__model = model
        
    def __str__(self):
        return 'model ship: {model}'.format(model=self.__model)
        
    def sail(self):
        print("Ship ran ran ran")
        

class WarShip(Ship):
    
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun
        
    def attack(self):
        print(f'warShip attak s pomoshiy {self.gun}')
        

war_ship = WarShip('zxc2', "GUNGUNGUN")

war_ship.attack()

class CargoShip(Ship):
    
    def __init__(self, model):
        super().__init__(model)
        self.gruz = 0
        
    def pogruzka(self):
        self.gruz += 100
    
    def vigruzka(self):
        self.gruz -= 100
        
        
        
cargo = CargoShip("cargo")
        
cargo.pogruzka()
cargo.vigruzka