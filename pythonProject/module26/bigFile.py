

def big(path):
    amount = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            summation = max(map(int, line.rstrip().split()))
            yield summation


all_sum = 0

for i in big("C:\\Users\\Пользователь\\PycharmProjects\\home\\module26\\file\\number.txt"):
    all_sum += i

print(all_sum)