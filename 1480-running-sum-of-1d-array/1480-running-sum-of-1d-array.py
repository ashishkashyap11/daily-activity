class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=0
        ans=[]
        low=0
        for low in range(len(nums)):
            result=result+nums[low]
            ans.append(result)
                
        return ans
        