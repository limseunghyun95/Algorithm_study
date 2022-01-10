# source : https://www.acmicpc.net/problem/15829

import sys

L = int(sys.stdin.readline())
data = sys.stdin.readline().strip()
answer = 0

ch_num = dict()

for i in range(26):
    ch_num[chr(97 + i)] = i + 1 # ascii 코드를 이용해 알파벳 소문자에 대한 딕셔너리 초기화

for index, value in enumerate(data):
    answer += ch_num[value] * (31**index) # 해쉬 계산
    
print(answer % 1234567891)