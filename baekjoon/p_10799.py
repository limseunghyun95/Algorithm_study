# source : https://www.acmicpc.net/problem/10799

n = input()

stack = []
answer = 0

for idx in range(len(n)):
    
    if n[idx] == "(":
        stack.append(n[idx])
    else:
        data = stack.pop()
        if data == "(":
            answer += len(stack)
        else:
            answer += 1
            
print(answer)