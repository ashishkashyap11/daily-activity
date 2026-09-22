class Solution(object):
    def maxSubArray(self, nums):
        i=0
        bestending=nums[i]
        ans=nums[i]
        for i in range(1,len(nums)):
            v1=bestending+nums[i]
            v2=nums[i]
            bestending=max(v1,v2)
            ans=max(ans,bestending)
        return ans        