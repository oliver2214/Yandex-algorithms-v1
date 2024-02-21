n = int(input())
cntr = 0
m = set()
for _ in range(n):
    a, b = map(int, input().split())
    if a < 0 and b < 0:
        a, b = abs(a), abs(b)
    elif a < 0:
        a = a + b
    elif b < 0:
        b = a + b

    if a + b == n - 1 and (a, b) not in m:
        cntr += 1
    m.add((a, b))

print(cntr)
