class Solution(object):
    def maxAbsoluteSum(self, nums):
        i=0
        maxend=nums[i]
        minend=nums[i]
        ans=abs(nums[i])
        for i in range(1,len(nums)):
            maxend=max(maxend+nums[i],nums[i])
            minend=min(minend+nums[i],nums[i])
            ma=abs(maxend)
            mi=abs(minend)
            ans=max(ma,mi,ans)
        return ans


        