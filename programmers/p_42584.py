# source : https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    
    # answer에는 가격이 떨어지지 않은 시간을 보관하기 위해 prices의 길이만큼 0으로 초기화
    answer = [0 for i in range(len(prices))]
    
    for i in range(len(prices)):
        now = prices[i] # 현재 주식 가격을 확인
        for j in range(i+1, len(prices)): # 이후의 주식 가격을 확인하여
            answer[i] += 1
            if now > prices[j]: # 현재보다 주식 가격이 떨어지면 시간 count 종료
                break
            
    return answer