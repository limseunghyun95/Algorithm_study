# source : https://www.acmicpc.net/problem/2217

import sys

N = int(sys.stdin.readline().strip())
ropes = []

for _ in range(N):
    ropes.append(int(sys.stdin.readline().strip()))

answer = 0
for i, r in enumerate(sorted(ropes)):
    answer = max([answer, (N-i) * r])
    
print(answer)