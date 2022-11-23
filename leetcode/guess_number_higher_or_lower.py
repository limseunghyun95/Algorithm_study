# source: https://leetcode.com/problems/guess-number-higher-or-lower/

# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            mid = (end + start) // 2

            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                end = mid - 1
            elif res == 1:
                start = mid + 1
