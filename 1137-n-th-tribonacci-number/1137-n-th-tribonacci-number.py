class Solution(object):
    def __init__(self):
        # Create a cache dictionary to remember past answers
        self.cache = {}

    def tribonacci(self, n):
        # 1. Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
            
        # 2. Check if we already calculated this n before
        if n in self.cache:
            return self.cache[n]
            
        # 3. Calculate and save the result into the cache
        self.cache[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
        return self.cache[n]
