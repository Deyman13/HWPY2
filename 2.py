list_1 = list(map(int, input("Введите числа через пробел: ").split(" ")))
product = list()
for i in range(int(len(list_1) / 2 + (1 if len(list_1) % 2 == 1 else 0))):
    product.append(list_1[i] * list_1.pop())
print(product)


from random import randint as r
list_2 = list([r(-20, 20) for num in range(int(input("Введите размерность списка: ")))])
print(list_2)
for i in range(int(len(list_2) / 2 + (1 if len(list_2) % 2 == 1 else 0))):
    print(list_2[i] * list_2.pop(), end=", ")


    