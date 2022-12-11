import random


# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. У того, кого бьют,
# оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение,
# какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

class Warriors:
    def __init__(self):
        self.health = 100

    def info(self):
        print(self.health, end="HP\n")


warrior_one = Warriors()
warrior_two = Warriors()


def fight():
    while True:
        num = random.randint(1, 2)
        if warrior_one.health != 0 and warrior_two != 0:
            if num == 1:
                print(f"Атаковал юнит под номером {num}")
                warrior_two.health -= 20
                print("У воина №2 осталось - ", end="")
                warrior_two.info()
            else:
                print(f"Атаковал юнит под номером {num}")
                warrior_one.health -= 20
                print("У воина №1 осталось - ", end="")
                warrior_one.info()
        else:
            if warrior_one.health == 0:
                print("Одержал победу №2")
                break
            else:
                print("Одержал победу №1")
                break

fight()