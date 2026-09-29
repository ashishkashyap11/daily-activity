class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        summ=0
        ans=0
        rem=0
        f={}
        f[0]=1
        for i in range(len(nums)):
            summ=summ+nums[i]
            #summ = sum(nums[0:i+1])
            rem=summ%k
            if 0>rem:
                rem=rem+k
            if rem in f:
                ans+=f[rem]

            if rem in f:
                f[rem]+=1
            else:
                f[rem]=1
            
            
        return ans



        