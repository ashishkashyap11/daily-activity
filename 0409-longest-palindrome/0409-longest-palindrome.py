class Solution:
    def longestPalindrome(self, s: str) -> int:
        f={}
        ans1=0
        ans2=0
        if len(set(s)) == 1:
            return len(s)
        for i in range(len(s)):
            if s[i] in f :
                f[s[i]]+=1
            else:
                f[s[i]]=1

        for j in f:
            if f[j] % 2==0:
                ans1=ans1+f[j]
            else:
                ans1 = ans1 + (f[j] - 1)
                ans2 = 1
        return ans1+ans2
        
        
        