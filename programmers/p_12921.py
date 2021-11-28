# source : https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    
    sieve = [True] * (n + 1)
    
    sieve[0] = False # 0, 1은 소수가 아님
    sieve[1] = False

    for i in range(2, n+1):
        if sieve[i] == True:
            mul = 2
            while i * mul <= n:
                sieve[i * mul] = False
                mul += 1
                
    return len([i for i in sieve if i == True])