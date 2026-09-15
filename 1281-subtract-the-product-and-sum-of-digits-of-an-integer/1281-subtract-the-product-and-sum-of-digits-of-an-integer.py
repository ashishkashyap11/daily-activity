class Solution(object):
    def subtractProductAndSum(self, n):
        temp=n
        pro=1
        sm=0
        while temp>0:
            r=temp%10
            sm=sm+r
            pro=pro*r
            temp=temp/10
        return pro-sm
        