n = int(input())

words = dict()

for _ in range(n):
    word1, word2 = input().split()
    words[word1] = word2

desired = input()
res = words.get(desired)
if res:
    print(res)
else:
    for key in words.keys():
        if desired == words[key]:
            print(key)
            break
