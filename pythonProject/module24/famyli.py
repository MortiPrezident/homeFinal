# Реализуйте класс «Семья», который состоит из атрибутов «Имя»,
# Деньги» и «Наличие дома» и объекты которого могут выполнять следующие действия:
#
# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.


class Famyli:
    surname = "Petrovi"
    money = 8 ** 5
    have_house = False

    def info(self):
        print(f"surname - {self.surname}\n"
              f"money - {self.money}\n"
              f"have_house - {self.have_house}")

    def work(self, coin):
        self.money += coin

    def buy_house(self, price_house, discount = 0):
        price_house += price_house * discount / 100
        if self.money >= price_house:
            self.have_house = True
            print("Поздравляю, вы купили дом")
        else:
            print(f"Жаль но вам не хватает {price_house - self.money}. Заработайте")


famyli_one = Famyli()

famyli_one.info()
famyli_one.buy_house(10**5)
famyli_one.work(320000)
famyli_one.buy_house(10**5, discount=30)
famyli_one.info()
