# source : https://www.acmicpc.net/problem/2839

N = int(input())

answer = 0

while N >= 0: # N이 0 이상일 때까지 반복
    if N % 5 == 0: 
        answer += N // 5
        break # N이 5의 배수라면 3kg 봉지를 고려할 필요가 없기 때문에 종료
    N -= 3 # 5의 배수가 아니라면 하나의 3kg 봉지에 설탕을 담는다. # 만일 N이 3보다 작으면 반복문 종료
    answer += 1

if N < 0:  
    print(-1)
else:
    print(answer)