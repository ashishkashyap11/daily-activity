class Solution(object):
    def checkInclusion(self, s1, s2):
        n = len(s1)
        m = len(s2)
        
        if n > m:
            return False
            
        omb = [0] * 256
        smb = [0] * 256
        
        for char in s1:
            omb[ord(char)] += 1
            
        low = 0
        for high in range(m):
            smb[ord(s2[high])] += 1
            
            if high - low + 1 > n:
                smb[ord(s2[low])] -= 1
                low += 1
                
            if smb == omb:
                return True
                
        return False
