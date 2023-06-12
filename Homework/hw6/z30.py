print('Введите первой элемент прогрессии: ', end='')
a1 = int(input())
print('Введите разность: ', end='')
d = int(input())
print('Введите кол-во элементов: ', end='')
n = int(input())

pg = []
for i in range(0, n):
    pg.append(a1 + i * d)

print('Прогрессия:', pg)
