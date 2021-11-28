# source : https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    
    answer = ''
    
    for i in s:
        
        if i == " ":
            answer += " "
        else:
            if i >= "a" and i <= "z":
                ascii = ord(i)+n
                if ascii > 122:
                    answer += chr(ascii - 26)
                else:
                    answer += chr(ascii)
            elif i >= "A" and i <= "Z":
                ascii = ord(i)+n
                if ascii > 90:
                    answer += chr(ascii - 26)
                else:
                    answer += chr(ascii)
                            
    return answer