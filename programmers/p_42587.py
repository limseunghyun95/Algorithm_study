# source : https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    
    answer = 0
    pointer = location
    
    while priorities:
        
        job = priorities.pop(0)
        
        if len(priorities) != 0:
            if job < max(priorities):
                priorities.append(job)
            else:
                answer += 1
                if pointer == 0:
                    break
        else:
            answer += 1
            break
        
        if pointer == 0:
            pointer = len(priorities) - 1
        else:
            pointer -= 1

    return answer

print(solution([3], 0))