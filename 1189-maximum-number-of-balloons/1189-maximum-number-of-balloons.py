class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f={}
        fq={}
        ans=[]
        s="balloon"
        for i in range(len(s)):
            if s[i] in f:
                f[s[i]]+=1
            else:
                f[s[i]]=1
        for j in range(len(text)):
            if text[j] in fq:
                fq[text[j]]+=1
            else:
                fq[text[j]]=1
        
        for k in f:
            if k in fq:
                div = fq[k] // f[k]
                ans.append(div)
            else:
                return 0

        return min(ans)                

        