# source : https://www.acmicpc.net/problem/10816

import sys
    
n = int(sys.stdin.readline())
n_card = sorted(list(map(int, sys.stdin.readline().split(" "))))

m = int(sys.stdin.readline())
m_card = list(map(int, sys.stdin.readline().split(" ")))

# 딕셔너리로 변형
temp = dict()

for item in n_card:
    
    if item in temp.keys():
        temp[item] += 1
    else:
        temp[item] = 1
        
n_card = temp

answer = []

for i in m_card:
    try:
        answer.append(str(n_card[i]))
    except:
        answer.append("0")

print(" ".join(answer))