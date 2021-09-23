# source : https://www.acmicpc.net/problem/2012

N = int(input())
ranks = []

answer = 0

for _ in range(N):
    ranks.append(int(input()))

for index, rank in enumerate(sorted(ranks)):

    answer += abs((index + 1) - rank)

print(answer)