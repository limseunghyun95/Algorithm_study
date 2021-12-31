# source : https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    
    answer = ''
    
    keypad = [[1,2,3], [4,5,6], [7,8,9], [10, 0, 11]]
    
    l_point = [3, 0]
    r_point = [3, 2]
    
    for num in numbers:
 
        if num in [1,4,7]: # 1,4,7 은 왼손 엄지 이용
            answer += "L"
            if num == 1:
                l_point = [0, 0]
            elif num == 4:
                l_point = [1, 0]
            else:
                l_point = [2, 0]
        elif num in [3,6,9]: # 3,6,9 는 오른손 엄지 이용
            answer += "R"
            if num == 3:
                r_point = [0, 2]
            elif num == 6:
                r_point = [1, 2]
            else:
                r_point = [2, 2]
        else: # 2,5,8,0 처리
            if num == 2:
                l_dis = abs(l_point[0] - 0) + abs(l_point[1] - 1)
                r_dis = abs(r_point[0] - 0) + abs(r_point[1] - 1)
                if l_dis > r_dis:
                    answer += "R"
                    r_point = [0, 1]
                elif r_dis > l_dis:
                    answer += "L"
                    l_point = [0, 1]
                else:
                    if hand == "right":
                        answer += "R"
                        r_point = [0, 1]
                    else:
                        answer += "L"
                        l_point = [0, 1]
            elif num == 5:
                l_dis = abs(l_point[0] - 1) + abs(l_point[1] - 1)
                r_dis = abs(r_point[0] - 1) + abs(r_point[1] - 1)
                if l_dis > r_dis:
                    answer += "R"
                    r_point = [1, 1]
                elif r_dis > l_dis:
                    answer += "L"
                    l_point = [1, 1]
                else:
                    if hand == "right":
                        answer += "R"
                        r_point = [1, 1]
                    else:
                        answer += "L"
                        l_point = [1, 1]
            elif num == 8:
                l_dis = abs(l_point[0] - 2) + abs(l_point[1] - 1)
                r_dis = abs(r_point[0] - 2) + abs(r_point[1] - 1)
                if l_dis > r_dis:
                    answer += "R"
                    r_point = [2, 1]
                elif r_dis > l_dis:
                    answer += "L"
                    l_point = [2, 1]
                else:
                    if hand == "right":
                        answer += "R"
                        r_point = [2, 1]
                    else:
                        answer += "L"
                        l_point = [2, 1]       
            elif num == 0:
                l_dis = abs(l_point[0] - 3) + abs(l_point[1] - 1)
                r_dis = abs(r_point[0] - 3) + abs(r_point[1] - 1)
                if l_dis > r_dis:
                    answer += "R"
                    r_point = [3, 1]
                elif r_dis > l_dis:
                    answer += "L"
                    l_point = [3, 1]
                else:
                    if hand == "right":
                        answer += "R"
                        r_point = [3, 1]
                    else:
                        answer += "L"
                        l_point = [3, 1]
                        
        print(num, l_point, r_point)
    return answer