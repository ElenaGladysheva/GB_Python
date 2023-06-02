s = int(input())
p = int(input())

for i in range(1, s):
    a = s - i
    if a * i == p:
        print(a, i)
        break