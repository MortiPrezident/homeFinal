import os

path = input("Введите путь: ")

search = input("введите искомую директорию: ")


def gen_files_path(path: str, search: str):
    for i_elem in os.walk(path):
        if i_elem[0].endswith(search):
            print(f"Папка найдена, вот путь - {i_elem[0]}")
            break
        print(i_elem[0])


gen_files_path(path, search)
