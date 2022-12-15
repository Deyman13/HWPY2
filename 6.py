def swap(lst, k):
    if k < 0:
        k = abs(k)
        for i in range(k):
            lst.append(lst.pop(0))
    else:
        for i in range(k):
            lst.insert(0, lst.pop())
    return lst


n = int(input())
lst = []
for i in range(n):
    number = int(input())
    lst.append(number)
print(lst)
k = int(input())
print(swap(lst, k))
