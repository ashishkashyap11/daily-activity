class Solution(object):
    def countDigits(self, num):
        ans=0
        temp=num
        while temp>0:
            r=temp%10
            temp=temp//10
            if num%r==0:
                ans+=1
                
        return ans


        