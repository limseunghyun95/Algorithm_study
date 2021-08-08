# source : https://www.acmicpc.net/problem/10989

# 정렬 중 데이터의 갯수가 많아 러닝타임을 최소화하고 수의 범위가 주어진 경우, 계수 정렬을 이용하여 해결하자
import sys

N = int(sys.stdin.readline()) # 입력받을시 sys.stdin.readline을 사용하면 훨씬 더 빠르다
array = [0] * 10001

for i in range(N):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)