# source : https://www.acmicpc.net/problem/11399

import sys

N = int(sys.stdin.readline().strip())
P = list(map(int, sys.stdin.readline().strip().split()))

answer = 0

P = sorted(P)

for i in range(N):
    answer += sum(P[:i+1])
    
print(answer)