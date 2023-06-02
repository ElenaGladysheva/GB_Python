n = int(input())
m = int(input())
lis1 = []
lis2 = []
for i in range(n):
    lis1.append(int(input()))
for i in range(m):
    lis2.append(int(input()))
set1 = set(lis1)
set2 = set(lis2)
res = set1.intersection(set2)
res = list(res)
res.sort()
for i in range(len(res)):
    print(res[i], end=" ")
