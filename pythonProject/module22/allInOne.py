import os



def all_in_one(abs_path):


    file = open("scripts.txt", "w", encoding="utf-8")
    for i_elem in os.listdir(abs_path):
        path = os.path.join(abs_path, i_elem)
        if path.endswith(".py"):
            file_two = open(path, "r", encoding="utf-8")
            file.write(file_two.read() + "\n" + "*" * 40 + "\n")
            file_two.close()
    else:
        file.close()


absolute_path = "R:\homeFinal\pythonProject\module22"
all_in_one(absolute_path)