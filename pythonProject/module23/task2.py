import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = ""

name_file = "ages.txt"
result_file = "result.txt"
file = open(name_file, "r")
file_two = open(result_file, "x")
try:

    for i_elem in file:
        text += alphabet[random.randint(0, len(alphabet) - 1)] + "-" + i_elem + "\n"
    file.close()

    file_two.write(text)

except PermissionError as exc:
    print(type(exc), "На чтение ожидался файл, но это оказалась директория.")
except TypeError as exc:
    print(type(exc), "Неверный тип данных или некорректное значение")
except FileExistsError as exc:
    print(type(exc), "Попытка создания файла, который уже существует.")
finally:
    file_two.close()
# Попытка создания файла, который уже существует.
# На чтение ожидался файл, но это оказалась директория.
# Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
