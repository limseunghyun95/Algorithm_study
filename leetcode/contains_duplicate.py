# source : https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        if len(nums) == 1:
            return False
        
        prev = nums[0]
        for n in nums[1:]:
            if prev == n:
                return True
            prev = n

        return False
