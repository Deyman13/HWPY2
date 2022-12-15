# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
print(bin(int(input())).replace("0b", ""))

number = int(input("Введите число в десятичной системе счисления: "))
const = number
for i in range(2, 10):
    number = const
    temp = ""
    while number > 0:
        temp = str(number % i) + temp
        number = number // i
    print(f'Число {const} в {i}-чной системе счисление = {temp}')


