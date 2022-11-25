import os

file = open("R:\homeFinal\pythonProject\module22\group_1.txt", 'r', encoding='utf-8')

list_name = []

for i_elem in file:
    print(i_elem, end="")
    list_name.append(str(len(i_elem)))

file.close()

text = "\n".join(list_name)

file_two = open("sym.count.txt", "w", encoding="utf-8")

file_two.write(text)
file_two.close()