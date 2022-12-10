name_list = list()

while True:
    try:

        name = input("Введите имя: ")
        if not name.strip().isalpha():
            raise TypeError("Нужно вводить только буквы")
        name_list.append(name)
        if len(name_list) == 3:
            break
    except TypeError:
        print("ошибочка")


print(name_list)