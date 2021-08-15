# source : https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):

    answer = 0

    # 초기화 (합계, 인덱스 번호)
    queue = deque([(0, 0)]) # 중복을 위해 set 이용

    while queue: # 스택이 비어있을때까지 반복
        _sum, idx = queue.popleft()

        if _sum == target and idx == len(numbers): # 모두 순회하고, 합계가 target인 경우에만 count up
            answer += 1

        else:
            if idx < len(numbers): # numbers 범위에 벗어나지 않은 선에서 deque에 값 추가
                number = numbers[idx]
                queue.append((_sum + number, idx + 1))
                queue.append((_sum - number, idx + 1))

    return answer        

print(solution([1, 1, 1, 1, 1], 3))