list_1 = list(map(int, input().split(" ")))
sum = 0
for i in range(len(list_1)):
    if i % 2 == 1:
        sum += list_1[i]
print(sum)



