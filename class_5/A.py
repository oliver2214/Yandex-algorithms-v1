n = int(input())
shirts = list(map(int, input().split()))
m = int(input())
pants = list(map(int, input().split()))

n_it = 0
m_it = 0
result = (shirts[n_it], pants[m_it])
while not (m_it == m or n_it == n):
    if abs(shirts[n_it] - pants[m_it]) < abs(result[1] - result[0]):
        result = (shirts[n_it], pants[m_it])
    if shirts[n_it] - pants[m_it] > 0:
        m_it += 1
    else:
        n_it += 1

print(*result)
