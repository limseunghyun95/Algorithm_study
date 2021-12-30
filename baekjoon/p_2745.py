# source : https://www.acmicpc.net/problem/2745

import sys

N, B = sys.stdin.readline().strip().split(" ")

answer = 0

for index, value in enumerate(N):
    
    exp = len(N) - index - 1
    
    if value.isalpha():
        num = ord(value) - 55 # ord(문자) : 문자를 ascii code로 변환 -> 문자를 숫자로 변환하기 위함
    else:
        num = int(value)
    
    answer += num * int(B)**exp
    
print(answer)