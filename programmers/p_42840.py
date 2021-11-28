# source : https://programmers.co.kr/learn/courses/30/lessons/42840

def cycle_generator(pattern):
    
    saved = []
    
    for e in pattern:
        yield e
        saved.append(e)
    
    while saved:
        for e in saved:
            yield e
            
    
def solution(answers):
    
    answer = []
    
    pt_1 = cycle_generator([1, 2, 3, 4, 5])
    pt_2 = cycle_generator([2, 1, 2, 3, 2, 4, 2, 5])
    pt_3 = cycle_generator([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    cnt = [0, 0, 0]
    
    for i in range(len(answers)):
    
        if answers[i] == pt_1.__next__():
            cnt[0] += 1
        if answers[i] == pt_2.__next__():
            cnt[1] += 1
        if answers[i] == pt_3.__next__():
            cnt[2] += 1
    
    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            answer.append(i+1)
    
    return answer