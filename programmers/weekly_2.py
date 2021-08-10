def calc_score(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def solution(scores):

    answer = []

    for i in range(len(scores)):
        s_score = []
        for j in range(len(scores)):
            s_score.append(scores[j][i])
        if (s_score[i] == max(s_score) and s_score.count(max(s_score)) == 1) or (s_score[i] == min(s_score) and s_score.count(min(s_score)) == 1):
            s_score.remove(s_score[i])
        answer.append(calc_score(sum(s_score) / len(s_score)))
            
    return "".join(answer)


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))