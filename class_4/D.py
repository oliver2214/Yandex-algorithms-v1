n = int(input())

keyboard = dict()
for i, value in enumerate(input().split()):
    keyboard[i + 1] = int(value)

k = int(input())

for pin in input().split():
    keyboard[int(pin)] -= 1

for key in keyboard.keys():
    if keyboard[key] < 0:
        print("YES")
    else:
        print("NO")
