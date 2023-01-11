import os

# Реализуйте функцию-генератор,
# которая берёт все питоновские файлы в директории и вычисляет количество строк в каждом файле,
# игнорируя пустые строки и строки комментариев. По итогу функция-генератор должна
# с помощью yield каждый раз возвращать количество строк в очередном файле.


path = os.path.abspath("./")


def my_genearation(path: str):
    for i_elem in os.walk(path):
        if len(i_elem[2]) >= 1:
            for name_file in i_elem[2]:
                if name_file.endswith(".py"):
                    print(f"количество строк в {name_file} = ", end="")
                    with open(name_file, "r", encoding="utf-8") as file:
                        count = 0
                        for line_file in file:
                            if line_file.strip().startswith("#"):
                                continue
                            elif line_file.startswith("\n"):
                                continue
                            count += 1

                        yield count


for i in my_genearation(path):
    print(i)