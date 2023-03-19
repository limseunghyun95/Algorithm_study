# source: https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = 0
        left_sum = 0
        right_sum = 0
        for i in range(1, len(nums)):
            right_sum += nums[i]

        while index != len(nums):
            if index == 0:
                pass
            else:
                left_sum += nums[index-1]
                right_sum -= nums[index]

            if left_sum == right_sum:
                return index

            index += 1

        return -1
