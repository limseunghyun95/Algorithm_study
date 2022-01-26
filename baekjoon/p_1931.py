# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline().strip())
meets = []

for _ in range(N):
    meets.append(list(map(int, sys.stdin.readline().strip().split())))
    
meets = sorted(meets, key = lambda x : (x[1], x[0])) # 종료하는 시간 기준으로 정렬하고 종료하는 시간이 동일하다면 시작하는 시간이 빠른 순으로 정렬

st_time = 0
answer = 0
log = [] # 어떤 회의가 포함되어있는지 확인용

for i in meets:
    
    if i[0] >= st_time:
        answer += 1
        log.append(i)
        st_time = i[1]
        
# print(log)
print(answer)