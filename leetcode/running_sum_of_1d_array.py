# source; https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            temp = 0
            for j in range(0, i+1):
                temp += nums[j]
            result.append(temp)

        return result

print(Solution().runningSum([1,2,3,4]))