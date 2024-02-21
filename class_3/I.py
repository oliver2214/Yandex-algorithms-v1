n = int(input())
general = set()
all = set()

c = int(input())
for i in range(c):
    lang = input()
    general.add(lang)
all.update(general)

for _ in range(n - 1):
    c = int(input())
    new_st = set()
    for i in range(c):
        lang = input()
        new_st.add(lang)

    general = general & new_st
    all.update(new_st)

print(len(general))
print(*general, sep='\n')
print(len(all))
print(*all, sep='\n')
