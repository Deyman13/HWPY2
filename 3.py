list_1 = list(map(float, input("Введите вещественные числа через пробел: ").split(" ")))
list_2 = []
for i in list_1:
    if i % 1 != 0:
        list_2.append(round(i % 1, 2))
print(max(list_2) - min(list_2))


list_3 = list(map(float, input("Введите вещественные числа через пробел: ").split(" ")))
list_4 = [round(i % 1, 2) for i in list_3 if i % 1 != 0]
print(max(list_4) - min(list_4))


list_5 = list(map(float, input("Введите вещественные числа через пробел: ").split(" ")))
print(max([round(i % 1, 2) for i in list_5 if i % 1 != 0]) - min([round(i % 1, 2) for i in list_5 if i % 1 != 0]))


print(max([round(i % 1, 2) for i in list(map(float, input("Введите вещественные числа через пробел: ").split(" "))) if i % 1 != 0]) - min([round(i % 1, 2) for i in list(map(float, input("Введите вещественные числа через пробел: ").split(" "))) if i % 1 != 0]))





