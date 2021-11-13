# source : https://www.acmicpc.net/problem/10828

n = int(input())

stack = []
answer = []

for _ in range(n):
    
    line = input()
    
    if "push" in line:
        cmd, value = line.split()
        stack.append(value)
    elif "pop" == line:
        if len(stack) == 0:
            answer.append("-1")
        else:
            answer.append(stack.pop())
    elif "size" == line:
        answer.append(str(len(stack)))
    elif "empty" == line:
        if len(stack) == 0:
            answer.append("1")
        else:
            answer.append("0")
    elif "top" == line:
        if len(stack) == 0:
            answer.append("-1")
        else:
            answer.append(stack[-1])
            
print("\n".join(answer))