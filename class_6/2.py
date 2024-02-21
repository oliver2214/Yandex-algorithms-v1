def check(cur, x, seq):
    return seq[cur] >= x


def lbinsearch(x, seq):
    l, r = 0, len(seq) - 1
    while l < r:
        cur = (l + r) // 2
        if check(cur, x, seq):
            r = cur
        else:
            l = cur + 1
    return l


n, k = [int(el) for el in input().split()]
n_list = [int(el) for el in input().split()]
k_list = [int(el) for el in input().split()]

for i in range(k):
    p = lbinsearch(k_list[i], n_list)
    if p != 0 and k_list[i] - n_list[p - 1] <= n_list[p] - k_list[i]:
        print(n_list[p - 1])
    else:
        print(n_list[p])
