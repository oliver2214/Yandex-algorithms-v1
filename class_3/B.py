# st1 = set(input().split())
# res = []
# for el in input().split():
#     if el in st1:
#         res.append(int(el))
# print(*sorted(res))


print(*sorted(list(map(int, (set(input().split()) & set(input().split()))))))
