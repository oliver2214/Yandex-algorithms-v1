n, k = map(int, input().split())

seq = list(map(int, input().split()))
cntr = 0

color = dict()
for i in range(k):
    color[seq[i]] = color[seq[i]] + 1 if color.get(seq[i]) else 1
    cntr += 1

l, r = 0, k - 1
ans = [1, n]
while r < n - 1 or l < n - k + 1:
    while r < n - 1 and len(color) != k:
        r += 1
        cntr += 1
        color[seq[r]] = color[seq[r]] + 1 if color.get(seq[r]) else 1
    if cntr - 1 < ans[1] - ans[0] and len(color) == k:
        ans = [l + 1, r + 1]
    l += 1
    cntr -= 1
    color[seq[l - 1]] -= 1
    if color[seq[l - 1]] == 0:
        del color[seq[l - 1]]


print(*ans)
