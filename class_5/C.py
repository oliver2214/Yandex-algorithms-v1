n = int(input())
prefixsum = [[0, 0]] * (n)
_, prev_y = map(int, input().split())

for i in range(1, n):
    _, cur_y = map(int, input().split())

    up = prefixsum[i - 1][0] + cur_y - prev_y if cur_y - prev_y > 0 else prefixsum[i - 1][0]
    down = prefixsum[i - 1][1] + prev_y - cur_y if cur_y - prev_y < 0 else prefixsum[i - 1][1]
    prefixsum[i] = [up, down]
    prev_y = cur_y

m = int(input())
for _ in range(m):
    s, f = map(int, input().split())
    if f >= s:
        print(prefixsum[f-1][0] - prefixsum[s-1][0])
    else:
        print(prefixsum[s-1][1] - prefixsum[f-1][1])
