# source : https://www.acmicpc.net/problem/2217

import sys

N = int(sys.stdin.readline().strip())
ropes = []

for _ in range(N):
    ropes.append(int(sys.stdin.readline().strip()))
    
print(min(ropes) * len(ropes))