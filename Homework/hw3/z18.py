n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
ch = int(input())
diff = 1000000000000
res = 0
for i in range(n):
    a = abs(s[i] - ch)
    if a < diff:
        diff = a
        res = s[i]
print(res)
