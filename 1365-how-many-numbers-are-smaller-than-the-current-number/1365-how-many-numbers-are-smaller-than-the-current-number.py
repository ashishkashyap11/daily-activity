class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        ans = []
        i = 0
        
        while i < len(nums):
            count = sorted_nums.index(nums[i])
            ans.append(count)
            i += 1
            
        return ans

        