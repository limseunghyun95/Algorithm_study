# source : https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    
    answer = []
    
    for i in range(1, n+1):
        answer.append(x*i)
        
    return answer