# source : https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    
    answer = True
    
    digit_sum = 0
    
    for i in str(x):
        digit_sum += int(i)
    
    if x % digit_sum != 0:
        answer = False
                
    return answer