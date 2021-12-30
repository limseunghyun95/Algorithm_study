# source : https://www.acmicpc.net/problem/5692

def factorial(n):
    
    if n == 1:
        return n
    
    dp = [0 for i in range(n+1)]
    
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = i * dp[i-1]
    
    return dp[i]

if __name__ == "__main__":
    
    answer = []

    while True:
        
        data = input()
        
        if data == "0": # 0은 마지막 입력이면서 제외
            break
        
        _sum = 0

        for index, value in enumerate(list(data)):
            
            _sum += factorial(int(len(data) - index)) * int(value)
        
        answer.append(_sum)
            
    print("\n".join(list(map(str, answer))))