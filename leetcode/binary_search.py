# source: https://leetcode.com/problems/binary-search/?envType=study-plan&id=binary-search-i


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)

        if target > nums[-1] or target < nums[0]:
            return -1

        while start <= end:
            mid = (end + start) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

        return -1