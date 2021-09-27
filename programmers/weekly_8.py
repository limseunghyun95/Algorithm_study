# source : https://programmers.co.kr/learn/courses/30/lessons/86491


# 명함을 가로 혹은 세로 모든 방향으로 끼워넣어도 되므로 각 명함의 크기를 비교하여 가장 큰 수를 세로, 가장 작은 수를 가로로 두어 최종적으로 가로 세로 각각의 가장 큰 값으로 곱한다.
def solution(sizes):

    answer = 0

    for index, size in enumerate(sizes):

        if size[0] > size[1]: # 가장 작은 수를 가로, 가장 큰 수를 세로로 둔다. 
            temp = sizes[index][0]
            sizes[index][0] = sizes[index][1]
            sizes[index][1] = temp

    answer = max(size[0] for size in sizes) * max(size[1] for size in sizes)

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))