BRUCE_WILLIS = 42

try:
    input_data = input('Введите строку: ')

    leeloo = int(input_data[4])

    result = BRUCE_WILLIS * leeloo

    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError as name:
    print(type(name), "невозможно преобразовать к числу")
except IndexError:
    print("Выход за границы строки")
except:
    print("какая то другая ошибка")