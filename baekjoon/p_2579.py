# source : https://www.acmicpc.net/problem/2579

import sys

n = int(sys.stdin.readline().strip())

stairs = []

for _ in range(n):
    
    stairs.append(int(sys.stdin.readline().strip()))

dp = [0 for _ in range(len(stairs) + 1)]

dp[1] = stairs[0]

if n >= 2:
    
    dp[2] = dp[1] + stairs[1]

    for i in range(3, n+1):
        
        dp[i] = max(stairs[i- 1] + stairs[i - 2] + dp[i - 3], stairs[i - 1] + dp[i - 2])

print(dp[-1])