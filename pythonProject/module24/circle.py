import math


# На координатной плоскости рисуются круги, у каждого круга следующие параметры:
# координаты X и Y центра круга и значение R ― радиус круга. По умолчанию центр находится в (0, 0), а радиус равен 1.
# Реализуйте класс «Круг», который инициализируется по этим параметрам. Круг также может:
# Находить и возвращать свою площадь.
# Находить и возвращать свой периметр.
# Увеличиваться в K раз.
# Определять, пересекается ли он с другой окружность


class Circle:

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def square_circle(self):
        square = math.pi * (self.radius ** 2)
        print(f"Площадь круга равна: {square}")
        return square

    def perimeter_circle(self):
        perimeter = 2 * math.pi * self.radius
        print(f"Периметр круга  равен:  {perimeter}")

    def increase_circle(self, multiplier):
        self.radius = self.radius * multiplier
        print(f"Круг увеличился в {multiplier} раз\nТеперь его радиус равен{self.radius}")

    def intersection_circle(self, circle_one, circle_two):
        distance = math.pow(circle_one.x, 2) - 2 * circle_one.x * circle_two.x + math.pow(circle_two.x, 2) \
                   + math.pow(circle_one.y, 2) - 2 * circle_one.y * circle_two.y + math.pow(circle_two.y, 2)
        radius_sum = math.pow(circle_one.radius, 2) + 2 * circle_one.radius * circle_two.radius + math.pow(
            circle_two.radius, 2)
        radius_diff = math.pow(circle_one.radius, 2) - 2 * circle_one.radius * circle_two.radius + math.pow(
            circle_two.radius, 2)
        if distance <= radius_sum and distance >= radius_diff:
            print("Окружности пересекаются")
        else:
            print("Окружности не пересекаются")


circle_one = Circle(4, 3, 2)
circle_two = Circle(4, 4, 3.2)

Circle.intersection_circle(Circle, circle_one, circle_two)
