def solution(priorities, location):

    answer = 1
    k = priorities[location]

    while True:

        if k == max(priorities) and location == 0:
            break
        else:
            data = priorities[0]

            if data == max(priorities):
                answer += 1
            else:
                priorities.append(data)
            priorities.pop(0)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        print(priorities, location)
    return answer

a = solution([2, 1, 3, 2], 2)
print(a)