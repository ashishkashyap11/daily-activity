class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans1=0
        ans2=0
        for i in range (1,n+1):
            if i%m!=0:
                ans1=i+ans1
            else:
                ans2=ans2+i
    
        return ans1-ans2

        