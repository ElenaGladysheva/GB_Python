n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
ch = int(input())
count = 0
for i in range(len(s)):
    if s[i] == ch:
        count += 1
print(count)
