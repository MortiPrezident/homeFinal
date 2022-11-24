import os


def search_file(cur_path, file_name):
    print(f"Переходим в {cur_path}")
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print(f"    Смотрим {path}")
        if i_elem == file_name:
            return path
        if os.path.isdir(path):
            result = search_file(path, file_name)
            if result:
                break
            else:
                print(f"Переходим в {cur_path}")
    else:
        result = None
    return result


file = "securiti.txt"

path_name = "F:\PycharmProjects"

final = search_file(path_name, file)

print("путь до файла {}".format({final}))
