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


file = "test2.py"

path_name = "R:\homeFinal"

final = search_file(path_name, file)

if final:
    text = open('history_search_two.txt', "a", encoding='utf-8')
    print("путь до файла {}".format({final}))
    text.write("\n" + final)
else:
    print("файл не найден")