class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        result=0
        for i in range(len(arr)-2):
            l=i+1
            r=len(arr)-1
            while l<r:
                sm=arr[i]+arr[l]+arr[r]
                    
                if sm>=sum:
                    r-=1
                    
                else:
                    result = result + (r-l)
                    l+=1
                    
        return result
                    
          
