class Solution(object):
    def maxProduct(self, nums):
        i=0
        maxend=nums[i]
        minend=nums[i]
        ans=nums[i]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=minend*nums[i]
            v3=maxend*nums[i]
            maxend=max(v1,v2,v3)
            minend=min(v1,v2,v3)
            ans=max(ans,minend,maxend)
        return ans
            
        