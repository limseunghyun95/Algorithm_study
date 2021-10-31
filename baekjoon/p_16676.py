# source : https://www.acmicpc.net/problem/16676

# 근우의 연봉 최댓값
N = input()
S = "1" * (len(N) -1)+ "0"

if len(N) == 1:
    print(1)
else:
    if int(N) > int(S):
        print(len(N))
    else:
        print(len(N) - 1)