def check(n, m, layer, t):
    return t < (2 * n + 2 * m - layer * 4) * layer


def lbinsearch(n, m, t):
    l, r = 0, min(n, m) // 2
    while l < r:
        layer = (l + r + 1) // 2
        if check(n, m, layer, t):
            r = layer - 1
        else:
            l = layer
    return l


n = int(input())
m = int(input())
t = int(input())

print(lbinsearch(n, m, t))
