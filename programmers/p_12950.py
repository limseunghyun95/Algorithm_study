# source : https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        for a1, a2 in zip(arr1[i], arr2[i]):
            temp.append(a1 + a2)
        answer.append(temp)
            
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))