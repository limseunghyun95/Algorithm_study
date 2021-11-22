# source : https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    
    answer = 0
    
    if a >= b:
        big, small = a, b
    else:
        big, small = b, a
        
    for i in range(small, big + 1):
        answer += i
    
    return answer