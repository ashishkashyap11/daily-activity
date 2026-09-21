class Solution(object):
    def fun(self,n):  
        sm = 0        
        while n > 0:             
            a = n % 10
            a = a ** 2
            sm = sm + a
            n = n // 10  
        return sm 
    def isHappy(self, n):
        slow =n
        fast=n
        while fast!=1:
            slow=self.fun(slow)
            fast=self.fun(fast)
            fast=self.fun(fast)

            if slow==fast and slow!=1:
                return False
        return True

        
        