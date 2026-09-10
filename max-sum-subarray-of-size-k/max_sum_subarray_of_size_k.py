class Solution:
    def maxSubarraySum(self, arr, k):
        low=0
        high=k-1
        sm=0
        result=0
        
        for i in range(low,high+1):
            sm=sm+arr[i]
            
        result=sm
            
        while high<len(arr)-1:
            low+=1
            high+=1
            
            sm=sm-arr[low-1]
            sm=sm+arr[high]
            
            result=max(result,sm)
            
        return result
