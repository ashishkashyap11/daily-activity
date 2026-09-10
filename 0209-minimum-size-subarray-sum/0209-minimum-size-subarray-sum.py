class Solution(object):
    def minSubArrayLen(self, target, nums):
        low=0
        high=0
        result = float('inf')
        sm=0

        while high<len(nums):
            sm=sm+nums[high]

            while sm>=target:
                length=high-low+1
                result=min(result,length)
                sm=sm-nums[low]
                low+=1
            high+=1
        if result == float('inf'):
            return 0

        else:
            return result







        