# source : https://www.acmicpc.net/problem/5585

n = int(input())
coin = [500, 100, 50, 10, 5, 1]

answer = 0
n = 1000 - n

for c in coin:
    cnt = int(n / c)
    answer += cnt
    n %= c
    
print(answer)