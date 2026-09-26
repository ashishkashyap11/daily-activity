class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left=0
        right=0
        n=len(nums)
        sm=sum(nums)
        if left==sm-nums[left]:
            return 0
        else:
            for i in range(1,n):
                left=left+nums[i-1]
                right=sm-left-nums[i]
                if left==right:
                    return i
            return -1



