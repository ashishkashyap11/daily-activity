class Solution(object):
    def maxSubarraySumCircular(self, nums):

        i=0
        ans=float('-inf')
        maxend=nums[i]
        maxans=nums[i]
        minans=nums[i]
        minend=nums[i]
        totalsum=sum(nums)

        for i in range(1,len(nums)):

            v1=maxend+nums[i]
            v2=nums[i]

            v3=minend+nums[i]
            v4=nums[i]

            maxend=max(v1,v2)
            minend=min(v3,v4)
            minans=min(minans,minend)
            maxans=max(maxans,maxend)

            kuli=totalsum-minans

            ans=max(maxans,kuli)   

        if maxans < 0:
            return maxans

        return ans

