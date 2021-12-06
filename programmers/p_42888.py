# source : https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    
    answer = []
    user = dict()
    
    for r in record:
        line = r.split(" ")
        
        if line[0] in ["Enter", "Change"]:
            user[line[1]] = line[2]

    for r in record:
        line = r.split(" ")
        
        if line[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(user[line[1]]))
        elif line[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(user[line[1]]))
    
    return answer