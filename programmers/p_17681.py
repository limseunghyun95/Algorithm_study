# source : https://programmers.co.kr/learn/courses/30/lessons/17681

def convert_bin(n, line):
    
    exp = n - 1
    result = []
    for i in range(n):
        if line >= 2 ** exp:
            line -= 2 ** exp
            result.append(1)
        else:
            result.append(0)
        exp -= 1
        
    return result


def solution(n, arr1, arr2):

    answer = []
    
    bin_arr1 = []
    bin_arr2 = []
    
    for line1, line2 in zip(arr1, arr2):
        bin_arr1.append(convert_bin(n, line1))
        bin_arr2.append(convert_bin(n, line2))
    
    for a1, a2 in zip(bin_arr1, bin_arr2):
        line = []
        for i, j in zip(a1, a2):
            if i == 1 or j == 1:
                line.append("#")
            else:
                line.append(" ")
        answer.append("".join(line))

    return answer