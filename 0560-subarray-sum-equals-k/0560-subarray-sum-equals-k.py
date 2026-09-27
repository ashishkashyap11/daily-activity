class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        summ = 0
        f = {}
        f[0] = 1
        
        for i in range(len(nums)):
            summ += nums[i]
            ques = summ - k
            
            if ques in f:
                freq = f[ques]
                res += freq
                
            if summ in f:
                f[summ] += 1
            else:
                f[summ] = 1
                
        return res
