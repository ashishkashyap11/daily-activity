class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        n=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>nums[n-1]:
                if target == nums[mid]:
                    return mid
                if nums[mid]<target:
                    low=mid+1
                if nums[mid]>target:
                    if target >= nums[0]:
                        high=mid-1
                    else:
                        low=mid+1
            else:
                if target == nums[mid]:
                    return mid
                if nums[mid]>target:
                    high=mid-1
                if nums[mid]<target:
                    if nums[n-1] >= target:
                        low=mid+1
                    else:
                        high=mid-1        
        return -1
