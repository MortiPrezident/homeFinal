file = open('F:\\task\group_1.txt', 'r', encoding='utf-8')

summa = 0

for i in file:
    info = i.split()
    summa += int(info[2])

print(summa)