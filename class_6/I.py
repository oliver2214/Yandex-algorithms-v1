def check(m, params):
    n, r, c, heights = params
    groups_count = 0

    i = 0
    while i <= len(heights) - c and groups_count < r:
        rez = heights[i:i + c]
        if rez[-1] - rez[0] <= m:
            groups_count += 1
            i += c
        else:
            i += 1

    if groups_count >= r or i == 0:
        return True
    return False


def lbinsearch(params):
    l, right = 0, params[3][-1] - params[3][0]
    while l < right:
        m = (l + right) // 2
        if check(m, params):
            right = m
        else:
            l = m + 1
    return l

n, r, c = [int(el) for el in input().split()]
heights = list()

for _ in range(n):
    heights.append(int(input()))
heights.sort()
params = (n, r, c, heights)

print(int(lbinsearch(params)))
