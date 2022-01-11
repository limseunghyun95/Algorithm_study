#source : https://www.acmicpc.net/problem/12865

import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0] * (K+1) for _ in range(N + 1)] # 가방의 무게를 기준으로 dp 생성

for i in range(1, N + 1):
    
    w, v = map(int, sys.stdin.readline().strip().split())
    
    for j in range(1, K + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j] , dp[i - 1][j - w] + v)
    
print(dp[N][K])