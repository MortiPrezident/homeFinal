file = open("numbers.txt", "r", encoding="utf-8")

summation = 0

for i_elem in file:
    summation += int(i_elem)

file.close()

file = open("answer.txt", "w", encoding="utf-8")

file.write(str(summation))