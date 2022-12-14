# Реализуйте иерархию классов, описывающих имущество налогоплательщиков.
# Она должна состоять из базового класса Property и производных от него классов Apartment, Car и CountryHouse. 

# Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор,
# и метод расчёта налога, переопределённый в каждом из производных классов.
# Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500. 

# Каждый дочерний класс должен иметь конструктор с одним параметром, передающий
# свой параметр конструктору базового класса.
# Разработайте интерфейс программы.
# Пусть она запрашивает у пользователя количество его денег и стоимость имущества,
# а затем выдаёт налог на соответствующее имущество и показывает, сколько денег ему не хватает (если это так).

class Property():
    '''
    Базовый класс, описывающий имущество.
    
    Аргументы:
            worth(int): передается стоимость имущества

    '''
    def __init__(self, worth):
        self.__worth = int(worth)
    
    def nalog(self):
        '''
        Метод предназначенный для подсчёта налога
        В дочерних классах написаны свои методы
        '''
        pass
    
    def get_worth(self):
        '''
        геттер, который возращает стоимость недвижимости
        '''
        return self.__worth

class Apartment(Property):
    '''
    Дочерний класс(квартира)
    '''
    def __init__(self, worth):
        super().__init__(worth)

    def nalog(self):
        tax = self.get_worth() / 1000
        print(f'Сумма налога = {tax}')
        return tax

class Car(Property):
    '''
    Дочерний класс(Машина)
    '''
    def __init__(self, worth):
        super().__init__(worth)
    
    def nalog(self):
        tax = self.get_worth() / 200
        print(f'Сумма налога = {tax}')
        return tax


class CountryHouse(Property):
    '''
    Дочерний класс(Дача)
    '''
    def __init__(self, worth):
        super().__init__(worth)

    def nalog(self):
        tax = self.get_worth() / 500
        print(f'Сумма налога = {tax}')
        return tax



def taxes():
    '''
    Основная функция, с помощью которой пользователь взаимодействует с программой
    
    Аргументы:
            money
            car
            balance
            aprtment
            house
    
    '''
    money = int(input('Введите колличество ваших денег'))
    car = Car(input('Введите стоимость машины'))
    balance = money - car.nalog() - car.get_worth()
    if balance < 0:
        print(f'вам не хватает {-balance}')
    aprtment = Apartment(input('Введите стоимость квартиры'))
    balance = money - aprtment.nalog() - aprtment.get_worth()
    if balance < 0:
        print(f'вам не хватает {-balance}')
    house = CountryHouse(input('Введите стоимость дома'))
    balance = money - house.nalog() - house.get_worth()
    if balance < 0:
        print(f'вам не хватает {-balance}')

taxes()    
    
# Что оценивается

# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода. 
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
# Для создания нового класса на основе уже существующего используется наследование.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
# Классы и методы/функции имеют прописанную документацию.
