class Solution(object):
    def findGCD(self, nums):
        a=max(nums)
        b=min(nums)
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        return gcd(a,b)
        