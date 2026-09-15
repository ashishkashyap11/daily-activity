class Solution(object):
    def isPalindrome(self, x):
        '''return str(num) == str(num)[::-1]'''
        if x < 0:
            return False

        original_x = x
        reversed_x = 0

        while x > 0:
            remainder = x % 10          
            reversed_x = (reversed_x * 10) + remainder  
            x = x // 10              

        return original_x == reversed_x
