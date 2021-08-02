# source : https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):

    for i in range(1, count + 1):
        money -= price * i
    
    if money > 0:
        return 0
    else:
        return -1 * money


solution(3, 20, 4)