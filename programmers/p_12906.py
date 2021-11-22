# source : https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    
    answer = []
    
    answer.append(arr[0])
    
    for i in arr[1:]:
        if answer[-1] != i:
            answer.append(i)
        
    return answer