# source : https://www.acmicpc.net/problem/1439

import sys
S = sys.stdin.readline().strip()

result = [0, 0]

for i in [0, 1]:
    is_continue = False
    for idx, value in enumerate(S):
        if value != str(i):
            if is_continue == False:
                result[i] += 1
                is_continue = True
        else:
            is_continue = False   

print(min(result))
