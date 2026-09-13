class Solution(object):
    def minWindow(self, s, t):

        if not s or not t or len(s) < len(t):
            return ""

        # Frequency map for characters in t
        need = [0] * 256
        for char in t:
            need[ord(char)] += 1

        have = [0] * 256
        
        # Helper function to check if 'have' satisfies 'need'
        def fun(have_vec, need_vec):
            for i in range(256):
                if have_vec[i] < need_vec[i]:
                    return False
            return True

        low = 0
        res = float('inf')
        start = -1

        # Sliding window
        for high in range(len(s)):
            have[ord(s[high])] += 1

            # Shrink the window as long as it contains all required characters
            while fun(have, need):
                length = high - low + 1
                if res > length:
                    res = length
                    start = low
                
                have[ord(s[low])] -= 1
                low += 1

        if res == float('inf'):
            return ""
            
        return s[start:start + res]
