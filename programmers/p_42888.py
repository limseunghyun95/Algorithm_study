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
            
    print(answer)
        
    
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])