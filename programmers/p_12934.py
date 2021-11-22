# source : https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    
    import math
    
    i = math.sqrt(n)
    
    if float.is_integer(i):
        return (int(i) + 1) ** 2
    else:
        return -1