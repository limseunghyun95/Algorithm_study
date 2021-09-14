# source : https://www.acmicpc.net/problem/5585

answer = 0
money = int(input())

chn = 1000 - money # 거스름돈 계산

for i in [500, 100, 50, 10, 5, 1]: # 크기가 큰 잔돈부터 시작하여 갯수 카운트
    
    if chn >= i:
        answer += int(chn / i) 
        chn = chn % i    

print(answer)
