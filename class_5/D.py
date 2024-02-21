n, r = map(int, input().split())

seq = list(map(int, input().split()))
first, last = 0, 1
cntr = 0
while last < n:
    while last < n and seq[last] - seq[first] <= r:
        last += 1
    cntr += n - last
    first += 1

print(cntr)
