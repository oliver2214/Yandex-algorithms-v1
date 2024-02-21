s = input()

for length in range(len(s), -1, -1):
    for i in range(len(s) - length + 1):
        if s[i:i + length] == s[i:i + length][::-1]:
            print(s[i:i + length])
            break
