# source : https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        
        num_dict = dict()
        
        for i in nums:
            if i in num_dict.keys():
                return True
            else:
                num_dict[i] = True
                
        return False