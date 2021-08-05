# source : https://www.acmicpc.net/problem/2747
import sys

def fibo(N):

    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        n_1 = 0
        n_2 = 1
        sum = 0
        for i in range(1, N):
            sum = n_1 + n_2
            n_1 = n_2
            n_2 = sum
            
        return sum

N = int(sys.stdin.readline())

print(fibo(N))