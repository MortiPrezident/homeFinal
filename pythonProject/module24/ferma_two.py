# садовник, у которого есть:
# Имя.
# Грядка с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой).
# И он может:
#
# Ухаживать за грядкой.
# Собирать с неё урожай (количество картошки ― пустой список).
import garden

class Gardener:
    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def care(self):
        self.garden.grow_garden()

    def harvest(self):
        if self.garden.all_rip():
            self.garden.potatos.clear()
            print("Урожай собран")

gard = Gardener("Semen", garden.PotatoGarden(8))

gard.harvest()
for _ in range(3):
    gard.care()
gard.harvest()