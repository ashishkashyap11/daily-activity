# class Solution:
#     def findMin(self, nums: list[int]) -> int:
#         low=0
#         high=len(nums)-1
#         ans = float('inf')
#         while low<=high:
#             mid=(low+high)//2
#             if nums[mid]>nums[high]:
#                 low=mid+1
#             else:
#                 ans=min(ans, nums[mid])
#                 high=mid-1
#         return ans
        

class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1

        if nums[high] > nums[0]:
            return nums[0]

        while(low <= high):
            mid = (low + high) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
                
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                low = mid + 1
            else:
                high = mid - 1

        