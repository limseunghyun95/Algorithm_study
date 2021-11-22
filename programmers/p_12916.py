# source : https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    
    answer = True
    
    p_cnt = 0
    y_cnt = 0
    
    for i in s.lower():
        if i == "p":
            p_cnt += 1
        elif i == "y":
            y_cnt += 1
            
    if p_cnt != y_cnt:
        answer = False

    return answer