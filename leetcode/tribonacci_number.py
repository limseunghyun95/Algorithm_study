# source : https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n):
        
        if n in [0, 1]:
            return n
        
        fibo = [0 for i in range(n+1)]
        
        fibo[0], fibo[1], fibo[2] = 0, 1, 1
        
        for i in range(3, n+1):
            fibo[i] = fibo[i-1] + fibo[i-2] + fibo[i-3]
            
        return fibo[n]