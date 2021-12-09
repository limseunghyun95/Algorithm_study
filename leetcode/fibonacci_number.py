# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n):

        if n in [0, 1]:
            return n
        
        fibo = [0 for i in range(n+1)]
        
        fibo[0] = 0
        fibo[1] = 1
        
        for i in range(2, n+1):
            fibo[i] = fibo[i-1] + fibo[i-2]
        
        return fibo[n]