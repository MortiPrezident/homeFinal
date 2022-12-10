class Employee:

    def __init__(self, name="ivan", salary=8000):
        self.name = name
        self.salary = salary

    def info(self):
        print(
            "Name: {}\nSalary: {}".format(self.name, self.salary)
        )

name = Employee("Danila", 285000)

name.info()