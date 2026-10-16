class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        mid=(low + high)//2
        guess=nums[mid]

        while low<=high: 
            if target>guess:
                low=mid+1
            if target<guess:
                high=mid-1
            if target==guess:
                return mid
            mid=(low + high)//2
            guess=nums[mid]

        return -1


        