# source : https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    
    answer = True
    
    if len(s) in [4, 6]:
        for i in s:
            if i not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                answer = False
    else:
        answer = False
        
    return answer