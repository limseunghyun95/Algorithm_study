# source : https://www.acmicpc.net/problem/1439

s = input()

result = [0, 0]

for i in [0, 1]:
    prev = -2
    for idx, value in enumerate(s):
        if int(value) != i:
            if idx != prev + 1:
                result[i] += 1
            prev = idx

print(min(result))
