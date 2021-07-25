N = int(input())

m = list()
for i in range(N):
    m.append(int(input()))

sort = list(map(str, sorted(m)))
print("\n".join(sort))