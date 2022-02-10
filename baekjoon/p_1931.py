# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline().strip())
meets = []

for _ in range(N):
    s_t, e_t = map(int, sys.stdin.readline().strip().split())
    meets.append([s_t, e_t])

sorted_meets = sorted(meets, key = lambda x : (x[1], x[0]))

start_time = 0
answer = 0

for m in sorted_meets:

    if start_time == 0 or m[0] >= start_time:
        answer += 1
        start_time = m[1]

print(answer)