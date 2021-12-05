def solution(s):
    
    answer = 1001
    
    for i in range(1, len(s) + 1):
        comp = ""
        count = 1
        previous = ""
        for j in range(0, len(s), i):
            part = s[j:j+i]
            
            if j == 0:
                previous = part
            else:
                if previous == part:
                    count += 1
                else:
                    if count == 1:
                        comp += previous
                    else:
                        comp += str(count) + previous
                    previous = part
                    count = 1
            
        if count == 1:
            comp += previous
        else:
            comp += str(count) + previous
        
        answer = min([len(comp), answer])
        
    return answer

print(solution("aabbaccc"))