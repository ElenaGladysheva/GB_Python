m = int(input())
n = int(input())
k = int(input())

if m * n < k:
    print("no")
else:
    if k % n == 0 and m >= k // n:
        print("yes")
    elif k % m == 0 and n >= k // m:
        print("yes")
    else:
        print("no")