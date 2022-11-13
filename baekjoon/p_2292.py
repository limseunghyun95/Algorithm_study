# source: https://www.acmicpc.net/problem/2292
import sys

n = int(input())

pass_cnt = 1
start_num = 1
end_num = 1

while True:
    num_range = range(start_num, end_num + 1)
    if n in num_range:
        break
    else:
        start_num = start_num + 1
        end_num = end_num + (pass_cnt * 6)
        pass_cnt += 1

print(pass_cnt)
