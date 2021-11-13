# source : https://www.acmicpc.net/problem/10773
# 시간 초과 이슈로 pypy3로 실행해야함

k = int(input())

answer = []

for _ in range(k):
    
    num = int(input())
    
    if num == 0:
        if len(answer) != 0:
            answer.pop()
    else:
        answer.append(num)
        
print(sum(answer))