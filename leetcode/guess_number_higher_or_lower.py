# source: https://leetcode.com/problems/guess-number-higher-or-lower/

# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        
        while start <= end:
            mid = (end + start) // 2
            
            if guess(mid) == 0:
                return mid
                
            if guess(mid) == -1:
                end = mid - 1
            elif guess(mid) == 1:
                start = mid + 1