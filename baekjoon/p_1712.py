# source: https://www.acmicpc.net/problem/1712

import sys

a, b, c = list(map(int, sys.stdin.readline().split()))

if c == b:  # ZeroDivdeError 방지
    print(-1)
    sys.exit(0)  # 0이 아닌 경우, NZEC 에러가 발생.

answer = int(a / (c - b)) + 1

if answer <= 0:
    print(-1)
else:
    print(answer)
