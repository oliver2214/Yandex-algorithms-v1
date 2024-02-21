def check(x, y, n, t):
    return t // x + t // y >= n


def lbinsearch(x, y, n):
    l, r = 0, n * max(x, y)
    while l < r:
        t = (l + r) // 2
        if check(x, y, n, t):
            r = t
        else:
            l = t + 1
    return l


n, x, y = [int(el) for el in input().split()]
print(lbinsearch(x, y, n - 1) + min(x, y))
