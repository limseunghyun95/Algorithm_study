# source : https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):

    able_lst = [0 for _ in range(n)]

    lost = sorted(lost)
    reserve = sorted(reserve)

    # 체육복을 가지고 있는 학생에 대한 값 변경
    for i in range(n):
        if i+1 not in lost:
            able_lst[i] = 1
    
    for lt in lost: # 도난당했지만 여유분이 있는 학생 처리
        if lt in reserve:
            reserve.remove(lt)
            able_lst[lt-1] = 1

    for lt in lost:

        if lt - 1 in reserve: # 대여 가능한 범위에 대한 처리
            able_lst[lt-1] = 1
            reserve.remove(lt-1)
            
        elif lt + 1 in reserve: # 대여 가능한 범위에 대한 처리
            able_lst[lt-1] = 1
            reserve.remove(lt+1)
            
    return sum(able_lst)
