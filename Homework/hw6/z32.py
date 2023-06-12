print('Введите количество элементов в массиве: ', end='')
n = int(input())
print('Введите элементы массива: ')
a = []
for i in range(0, n):
    a.append(int(input()))

print('Введите начало интервала: ', end='')
s = int(input())
print('Введите конец интервала: ', end='')
e = int(input())

ind = []
for i in range(0, n):
    if (a[i] >= s) and (a[i] <= e):
        ind.append(i)

print('Индексы, попавшие в итервал:', ind)
