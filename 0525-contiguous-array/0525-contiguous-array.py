class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans=0
        zero=0
        one=0
        f={}
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            if diff == 0 :
                ans=max(ans,i+1)
            if diff in f:
                idx=f[diff]
                length=i-idx
                ans=max(length,ans)
            else:
                f[diff]=i
        return ans


        
        