# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию, которая эмулирует работу
# цикла for с помощью цикла while и проходит во всем элементам итерируемого объекта.
# Не забудьте про исключение «конца итерации».

n = [i for i in range(5)]

iterator = iter(n)

while True:
    try:
        print(next(iterator))
    except StopIteration as exc:
        break