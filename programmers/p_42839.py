# source : https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def check_prime(num):

    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def solution(numbers):

    answer = 0

    overlap = dict()

    for i in range(1, len(numbers) + 1):

        com = permutations(numbers, i)

        for c in com:
            num = int("".join(c))
            
            if check_prime(num) and num not in overlap.keys():
                answer += 1
            overlap[num] = True
            
    return answer