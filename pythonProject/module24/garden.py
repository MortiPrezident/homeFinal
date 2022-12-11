class Potato:
    ripeness = {0: "Пусто", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.height = 0

    def info(self):
        print("картошка {} сейчас {}".format(self.index, self.ripeness[self.height]))

    def rip(self):
        if self.ripeness[self.height] == "Зрелая":
            return True
        else:
            return False

    def grow(self):
        self.height += 1
        self.info()


# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно,
# взращивать всю эту картошку, а также предоставлять информацию о зрелости всей картошки на своей территории.


class PotatoGarden:

    def __init__(self, count):
        self.potatos = [Potato(index) for index in range(1, count + 1)]

    def grow_garden(self):
        print("картошка прорастает!")
        for i_potato in self.potatos:
            i_potato.grow()
        print()

    def all_rip(self):
        if all([i_potato.rip() for i_potato in self.potatos]):
            print("Вся картошка созрела. Можно собирать!")
            return True
        else:
            print("Картошка ещё не созрела")
            return False

    def grow_info(self):
        for i_potato in self.potatos:
            i_potato.info()
