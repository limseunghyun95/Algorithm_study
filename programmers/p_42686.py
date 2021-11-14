# source : https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    
    answer = []

    while progresses:
        
        stack = []

        for i in range(len(progresses)):
            p = progresses[i]
            if p >= 100:
                if i == 0:
                    stack.append(i)
                elif i-1 in stack:
                    stack.append(i)
            else:
                progresses[i] += speeds[i]
        
        for _ in range(len(stack)):
            progresses.pop(0)
            speeds.pop(0)
        
        if len(stack) > 0:
            answer.append(len(stack))
    
    return answer