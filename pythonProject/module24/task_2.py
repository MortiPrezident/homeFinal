# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса
# (то есть передаваться в init). Реализуйте такое изменение класса.

class Toyota:

    def __init__(self, color="green", money=850000, speed_max=200, current_speed=0):
        self.color = color
        self.money = money
        self.speed_max = speed_max
        self.current_speed = current_speed
    def info(self):
        print(
            "color - {}\nmoney - {}\nmax_speed - {}\ncurrent_speed - {}\n".format(
                self.color, self.money, self.speed_max, self.current_speed
            ))

    def speed(self, mur):
        self.current_speed = mur


car_1 = Toyota(current_speed=60)
car_2 = Toyota()
car_3 = Toyota()


car_2.current_speed = 80
car_3.current_speed = 20

car_1.info()
car_2.speed(160)
car_2.info()