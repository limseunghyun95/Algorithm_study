# source : https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        
        for i, n in enumerate(nums):
            
            diff = target - n
            
            for j, m in enumerate(nums):
                if j <= i:
                    continue
                if m == diff:
                    return [i, j]
