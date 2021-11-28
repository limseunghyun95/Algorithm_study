# source : https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    
    d.sort()
    cnt = 0
    
    for item in d:
        
        if budget >= item:
            cnt += 1
            budget -= item
        else:
            break            
    
    return cnt