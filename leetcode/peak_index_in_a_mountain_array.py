# source: https://leetcode.com/problems/peak-index-in-a-mountain-array/?envType=study-plan&id=binary-search-i


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start = 0
        end = len(arr) - 1

        max_value = -1
        max_index = -1
        while start <= end:
            point1 = arr[start]
            point2 = arr[end]

            if point1 >= point2:
                end -= 1
                if point1 > max_value:
                    max_value = point1
                    max_index = start
            else:
                start += 1
                if point2 > max_value:
                    max_value = point2
                    max_index = end

        return max_index
