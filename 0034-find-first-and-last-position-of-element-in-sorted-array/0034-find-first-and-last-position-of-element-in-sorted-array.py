class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        high=len(nums)-1
        low=0
        l=-1
        
        while low<=high:
            guess=(low+high)//2
            if nums[guess]==target:
                l=guess
                high=guess-1
                       
            if nums[guess]<target:
                low=guess+1
            else:
                high=guess-1
        
        low = 0
        high = len(nums) - 1
        r=-1

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] == target:
                r = guess
                low = guess + 1  

            elif nums[guess] < target:
                low = guess + 1
            else:
                high = guess - 1
        
        return l,r


        