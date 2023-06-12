def sum(a,b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)


print('Введите первое слагаемое: ', end='')
a = int(input())
print('Введите второе слагаемое: ', end='')
b = int(input())
s = sum(a, b)
print(a, '+', b,'=', s)
