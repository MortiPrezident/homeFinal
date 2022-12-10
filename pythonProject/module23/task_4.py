count = 0


with open("words.txt", "r", encoding="utf-8") as file:
    with open("errors.log", "w", encoding="utf-8") as file_two:
        for i_elem in file:
            try:
                if i_elem.endswith("\n"):
                    i_elem = i_elem[:-1]
                if not i_elem.replace(" ", "").isalpha():
                    file_two.write(i_elem + "\n")
                    raise ValueError("Ошибка, встетилось число")
                if i_elem.lower().replace(" ","")[::-1] == i_elem.lower().replace(" ", "") :
                    count += 1
            except ValueError:
                print("ошибка", "встетилось число")
print(f"Встреченно палиндромов {count}")
