# source : https://www.acmicpc.net/problem/1026

import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

answer = 0

for i, j in zip(sorted(A, reverse = True), sorted(B)):
    answer += i*j
    
print(answer)