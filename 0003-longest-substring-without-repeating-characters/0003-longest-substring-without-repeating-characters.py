class Solution(object):
    def lengthOfLongestSubstring(self, s):
        high=0
        low=0
        freq={}
        res=-1
        for high in range(len(s)):
            if s[high] in freq:
                freq[s[high]]+=1
            else:
                freq[s[high]] = 1
            klength=high-low+1
            while len(freq)<klength:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                klength=high-low+1
            length=high-low+1
            res=max(length,res)
        if res==-1:
            return 0
        else:
            return res



            



        