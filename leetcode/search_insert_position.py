# source: https://leetcode.com/problems/search-insert-position/?envType=study-plan&id=binary-search-i


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end + start) // 2

            point = nums[mid]
            if point == target:
                return mid
            if point > target:
                end = mid - 1
            elif point < target:
                start = mid + 1

        return start
