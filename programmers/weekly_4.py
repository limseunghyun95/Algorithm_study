def solution(table, languages, preference):

    answer = None
    max_point = 0

    for row in table:
        job = row.split(" ")[0]
        langs = row.split(" ")[1:]
        
        total = 0
        for lang, pref in zip(languages, preference):
            try:
                point = 5 - langs.index(lang)
            except ValueError as ve:
                point = 0
            total += point * pref

        if total > max_point:
            max_point = total
            answer = job
        elif total == max_point:
            if answer > job:
                answer = job
            
    return answer


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))