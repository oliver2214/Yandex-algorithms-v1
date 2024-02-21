n, k = map(int, input().split())
seq = list(map(int, input().split()))

prefixsum = [0] * (n + 1)
for i in range(1, n + 1):
    prefixsum[i] = prefixsum[i-1] + seq[i - 1]
cntr = 0
l, r = 0, 1
while r != n + 1:
    if prefixsum[r] - prefixsum[l] == k:
        cntr += 1
        r += 1
        l += 1
    elif prefixsum[r] - prefixsum[l] >= k:
        l += 1
    else:
        r += 1

print(cntr)
