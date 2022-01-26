# source : https://www.acmicpc.net/problem/11047

import sys

N, K = map(int, sys.stdin.readline().strip().split())
answer = 0
coin = []

for _ in range(N):
    
    coin.append(int(sys.stdin.readline().strip()))
    
for c in coin[::-1]:
    answer += K // c
    K %= c
    
print(answer)