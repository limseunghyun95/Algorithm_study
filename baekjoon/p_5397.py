case = int(input()) # 케이스 수 수신

result = []

for i in range(case):
    L = input() # 문자열 수신
    left = []
    right = []

    for ch in L:
        if ch == "<":
            if len(left) != 0:
                right.append(left.pop())
        elif ch == ">":
            if len(right) != 0:
                left.append(right.pop())
        elif ch == "-":
            if len(left) != 0:
                left.pop()
        else:
            left.append(ch)
    
    left.extend(reversed(right))
    result.append("".join(left))

print("\n".join(result))