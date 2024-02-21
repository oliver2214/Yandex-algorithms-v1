def check(params, a, b, d):
    n, w, h = params
    return (w // (a + 2 * d)) * (h // (b + 2 * d)) < n


def lbinsearch(params, a, b):
    l, r = 0, min(params[1], params[2])
    while l < r:
        d = (l + r + 1) // 2
        if check(params, a, b, d):
            r = d - 1
        else:
            l = d
    return l


n, a, b, w, h = [int(el) for el in input().split()]
params = (n, w, h)
print(lbinsearch(params, a, b))
