class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low=0
        high=len(arr)-1
        ans=0
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<arr[mid+1]:
                low=mid+1
            if arr[mid]>arr[mid+1]:
                ans=mid
                high=mid-1
        return ans
        