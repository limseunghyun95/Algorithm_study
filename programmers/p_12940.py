# source : https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    
    answer = []
    
    i = 2
    gcd = 1
    
    while True:
 
        if i >= max(n, m):
            break
        
        if n % i == 0 and m % i == 0:
            n = n // i
            m = m // i
            gcd *= i
            i = 2
        else:
            i += 1
        
    answer.append(gcd)
    answer.append(gcd * n * m)
    
    return answer