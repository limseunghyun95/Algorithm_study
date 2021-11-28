# source : https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    
    players = dict()
    
    for c in completion:
        if c not in players.keys():
            players[c] = 1
        else:
            players[c] += 1

    for p in participant:
        if p not in players.keys():
            return p
        elif players[p] == 0:
            return p
        else:
            players[p] -= 1