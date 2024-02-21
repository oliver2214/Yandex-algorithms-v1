# не решил

def check(a, w, h, n):
    return (a // w) * (a // h) >= n


def lbinsearch(w, h, n):
    l, r = max(w, h), min(w, h) * n
    while l < r:
        a = (l + r) // 2
        if check(a, w, h, n):
            r = a
        else:
            l = a + 1
    return l


w, h, n = [int(el) for el in input().split()]
print(lbinsearch(w, h, n))
