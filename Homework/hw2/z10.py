n = int(input())
c0 = 0
c1 = 0
for i in range(n):
    a = int(input())
    if a == 1:
        c1 += 1
    else:
        c0 += 1
print(min(c1, c0))
