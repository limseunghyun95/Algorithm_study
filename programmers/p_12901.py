# source : https://programmers.co.kr/learn/courses/30/lessons/12901

from datetime import date

def solution(a, b):
    
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    diff = (date(2016, a, b) - date(2016, 1, 1)).days
    
    return days[diff % 7]