class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        
        while low<=high:

            mid=(low + high)//2
            guess=nums[mid]

            if target>guess:
                low=mid+1
            if target<guess:
                high=mid-1
            if target==guess:
                return mid
            

        return -1


        