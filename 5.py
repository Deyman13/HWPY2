def negafib1(num):
    if num >= 0:
        index = range(num + 1)
        temp_list = [0, 1]
        for i in index[2:]:
            temp_list.append(temp_list[i - 1] + temp_list[i - 2])
        return temp_list[num]
    else:
        index = range(-(num - 1) + 1)
        temp_list = [1, 0]
        for i in index[2:]:
            temp_list.append(temp_list[i - 2] - temp_list[i - 1])
        temp_list.reverse()
    return temp_list[0]
number = int(input("Введите число: "))
print([negafib1(num) for num in range(-number, number + 1)])



n = int(input("Введите число: "))
def negafib2(n):
    temp_list = []
    fstnum, scdnum = 1, 1
    for num in range(n):
        temp_list.append(fstnum)
        fstnum, scdnum = scdnum, fstnum + scdnum
    fstnum, scdnum = 0, 1
    for num in range (n + 1):
        temp_list.insert(0, fstnum)
        fstnum, scdnum = scdnum, fstnum - scdnum
    return temp_list
print(negafib2(n))

# данное решение выдает результат почти идеальный, за исключением одного - 
negafib3 = lambda n: n if n < 2 else negafib3(n - 1) + negafib3(n - 2)
negafib4 = lambda n: negafib3(n) if n >= 0 else round(negafib4(abs(n)) * (-1)**(n + 1))
print([negafib4(num) for num in range(-number, number + 1)])









            






