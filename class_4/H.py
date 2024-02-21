g, s = map(int, input().split())
cntr = 0
gdict = dict()
for ch in input():
    gdict[ch] = gdict[ch] + 1 if gdict.get(ch) else 1


text = input()

cur_dict = dict()
for ch in text[0:0+g-1]:
    cur_dict[ch] = cur_dict[ch] + 1 if cur_dict.get(ch) else 1

for i in range(s - g + 1):
    begin_ch = text[i-1:i]
    if cur_dict.get(begin_ch) is not None:
        if cur_dict.get(begin_ch) == 1:
            del cur_dict[begin_ch]
        elif cur_dict.get(begin_ch) > 1:
            cur_dict[begin_ch] -= 1

    end_ch = text[i + g - 1: i + g]
    cur_dict[end_ch] = cur_dict[end_ch] + 1 if cur_dict.get(end_ch) else 1

    if cur_dict == gdict:
        cntr += 1

print(cntr)
