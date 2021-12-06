# source : https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    
    answer = []
    comp_days = []
    job = []
    
    for p, s in zip(progresses, speeds): # 각 기능별 완료까지의 작업 수 계산
        d = 0
        while p + (s * d) < 100:
            d += 1
        comp_days.append(d)
    
    while comp_days: # 기능이의 완료날짜를 계산하여 배포가 가능한지 확인 후 결과값에 추가
        day = comp_days.pop(0) 
        if len(job) > 0:
            if job[0] >= day:
                job.append(day)
            else:
                answer.append(len(job))
                job = []
                job.append(day)
        else:
            job.append(day)
            
    if len(job) > 0: # 남은 기능이 있다면 추가
        answer.append(len(job))     
    
    return answer