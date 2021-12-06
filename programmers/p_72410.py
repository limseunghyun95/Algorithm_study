# source : https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    
    answer = new_id
    
    # 소문자 처리
    answer = answer.lower()
    
    # 불필요 문자 처리
    temp = ""
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ["-", "_", "."]:
            temp += c
    answer = temp
    
    # 마침표가 연속적인 문자 처리
    temp = ""
    count = 0
    for c in answer:
        if c == ".":
            count += 1
        else:
            if count >= 1:
                temp += "." + c
                count = 0
            else:
                temp += c
    if count != 0:
        temp += "."
    answer = temp
        
    # 마침표가 처음과 끝일때 문자 처리
    if len(answer) != 0:
        if answer[0] == ".":
            if len(answer) != 1:
                answer = answer[1:]
            else:
                answer = ""
    if len(answer) != 0:
        if answer[-1] == ".":
            if len(answer) != 1:
                answer = answer[:-1]
            else:
                answer = ""

    # 빈 문자열에 대한 처리
    if len(answer) == 0:
        answer = "a"
                
    # 문자열의 길이가 16자 이상인 경우에 대한 처리
    if len(answer) >= 16:
        answer = answer[:15]
    
    # 마지막 글자가 마침표일때 처리
    if answer[-1] == ".":
        answer = answer[:-1]
        
    # 문자열의 길이가 2이하인 경우에 대한 처리
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))
    
    return answer