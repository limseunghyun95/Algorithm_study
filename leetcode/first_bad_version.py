# source: https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            print(left, right, mid)
            mid = (right + left) // 2

            if isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

        return left
