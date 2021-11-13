# source : https://www.acmicpc.net/problem/9012

t = int(input())

answer = []

for _ in range(t):
    
    stack = []    
    ps = input()
    temp = False
    
    for i in ps:
        
        if len(stack) == 0:
            if i == ")":
                answer.append("NO")
                temp = True
                break
            else:
                stack.append(i)
        else:
            if i == "(":
                stack.append(i)
            else:
                data = stack.pop()
                if data != "(":
                    stack.append(data)
                    stack.append(i)
    
    if temp != True:
        if len(stack) == 0:
            answer.append("YES")
        else:
            answer.append("NO")

print("\n".join(answer))