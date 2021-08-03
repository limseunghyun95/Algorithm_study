# source : https://www.acmicpc.net/problem/11650

N = int(input())

matrix = []

for _ in range(N):
    x, y = map(int, input().split(" "))
    matrix.append((x, y))

for i in sorted(matrix, key = lambda x : (x[0], x[1])): 
    print(i[0], i[1])