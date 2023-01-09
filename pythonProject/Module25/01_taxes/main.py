
class Property:
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
            money - переменная, которая хранит колличество денег
            car - объект класса(машина)
            balance - переменная, с помощью которой высчитывается хватает ли денег на покупку
            aprtment - объект класса(квартира)
            house - объект класса (дача)
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
