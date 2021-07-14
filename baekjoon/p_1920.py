N = int(input())

A = dict()

data = list(map(int, input().split(" ")))

for i in data:
    A[i] = True

M = int(input())

result = []

data2 = list(map(int, input().split(" ")))

for j in data2:
    if j in A.keys():
        result.append("1")
    else:
        result.append("0")

print("\n".join(result))