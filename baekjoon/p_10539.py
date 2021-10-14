# source : https://www.acmicpc.net/problem/10539

N, B = input(), list(map(int, input().split(" ")))

A = []

for index, B_value in enumerate(B):
    
    A_value = (B_value * (index + 1)) - sum(A[:index + 1]) 
    A.append(A_value)

print(" ".join(list(map(str, A))))
