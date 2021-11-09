# source : https://www.acmicpc.net/problem/1012

'''
    flood fill
    - 주어진 시작점으로부터 연결된 영역들을 찾는 알고리즘
    - 다차원 배열의 어떤 칸과 연결된 영역을 찾는 알고리즘
'''

import sys
sys.setrecursionlimit(10**6) # 백준에서 재귀 깊이는 1000으로 설정되어 있어. 미추가시 recursionError 가 발생될 수 있다.

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        
        x, y = map(int, input().split())
        field[x][y] = 1
        
    def dfs(x, y):
        
        if x < 0 or y < 0 or x >= M or y >= N:
            return False
        if field[x][y] == 1:
            field[x][y] = 0
            dfs(x, y + 1)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x - 1, y)
            return True
        else:
            return False
        
    answer = 0

    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                answer += 1
                
    print(answer)