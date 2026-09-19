class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        
        slow=0
        fast=1
        
        while fast!=len(nums):
            if nums[slow]==nums[fast]:
                return nums[slow]
            slow+=1
            fast+=1

        