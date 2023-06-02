n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))
m = 0
for i in range(n):
    iprev = i - 1
    inext = (i + 1) % n
    if lis[iprev] + lis[i] + lis[inext] > m:
        m = lis[iprev] + lis[i] + lis[inext]
print(m)
