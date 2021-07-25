N = int(input())

member = []
for i in range(N):
    age, name = input().split(" ")
    member.append([int(age), name])

for j in sorted(member, key = lambda x : x[0]):
    print(j[0], j[1])