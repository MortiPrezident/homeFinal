class Points:
    count = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Points.count += 1
    def info(self):
        print("координаты точки ({}:{})\nВсего точек:{}".format(self.x, self.y, self.count))


point = Points()
point_2 = Points(5, 7)
point_3 = Points(4, 2)
point_3.info()

