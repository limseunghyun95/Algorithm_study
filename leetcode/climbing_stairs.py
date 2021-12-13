# source : https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        
        if n <= 2:
            return n
        
        dp = [0 for i in range(n+1)]
        dp[0] = 0 # 없는 값이지만 계산을 쉽게 하기 위해 0으로 초기화
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]