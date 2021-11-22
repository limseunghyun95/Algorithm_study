# source : https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    
    answer = ''
    
    for i in range(1, n+1):
        if i % 2 != 0:
            answer += "수"
        else:
            answer += "박"
    
    return answer

print(solution(4))