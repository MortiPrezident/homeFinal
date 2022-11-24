import os

path_name = input("Путь: ")


def icon(abs_path):

    if os.path.exists(abs_path):

        if os.path.isdir(abs_path):
            print("Это папка")

        if os.path.islink(abs_path):

            print("Это ссылка")
        if os.path.isfile(abs_path):
            print("Это файл")
            x = os.path.getsize(abs_path)
            print("Размер файла: ", x)


    else:
        print("Указанного пути не существует")

icon(path_name)