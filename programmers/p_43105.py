# source : https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    
    answer = 0
    
    for i in range(1, len(triangle)):
        current_data = triangle[i]
        previous_data = triangle[i-1]
        for j, data in enumerate(current_data):
            if j == 0:
                triangle[i][j] = data + previous_data[j]
            elif j == len(current_data) - 1:
                triangle[i][j] = data + previous_data[-1]
            else:
                triangle[i][j] = max(previous_data[j-1], previous_data[j]) + data
                
    return max(triangle[-1])