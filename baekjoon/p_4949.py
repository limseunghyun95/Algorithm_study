# source: https://www.acmicpc.net/problem/4949

while True:
    line = input()

    if line == ".":
        break

    result = True
    stack = []
    for c in line:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")" or c == "]":
            if len(stack) == 0:
                result = False
                break
            data = stack.pop(-1)
            if c == ")" and data != "(":
                result = False
                break
            elif c == "]" and data != "[":
                result = False
                break
    if len(stack) != 0:
        result = False

    print("yes" if result else "no")
