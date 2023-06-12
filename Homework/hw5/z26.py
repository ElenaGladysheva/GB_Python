def pow(a,b):
    if b == 1:
        return a
    else:
        return a * pow(a, b - 1)


print('Введите число: ', end='')
a = int(input())
print('Введите степень: ', end='')
b = int(input())
c = pow(a, b)
print('Число', a, 'в степени', b, 'равно', c)
