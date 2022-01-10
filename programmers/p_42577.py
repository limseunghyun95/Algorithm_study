# source : https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    
    answer = True
    
    phone_book = sorted(phone_book, key = lambda x : (x, len(x)))
    
    phone_dict = dict()
    
    for i, v in enumerate(phone_book):
        phone_dict[i] = v
        
    for i in range(len(phone_book) - 1):
        if phone_dict[i+1].startswith(phone_dict[i]):
            return False 

    return True