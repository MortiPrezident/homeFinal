import os


def search_file(cur_path, file_name, list_file=None):

    if list_file is None:
        list_file = list()

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem == file_name:
            list_file.append(path)
        if os.path.isdir(path):
            search_file(path, file_name, list_file)
    return list_file


file = "securiti.txt"

path_name = "F:\PycharmProjects"

final = search_file(path_name, file)

for i_output in final:
    print(i_output)