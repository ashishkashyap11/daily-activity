class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f = {"b":1,"a":1,"l":2,"o":2,"n":1}
        fq={}
        ans=float('inf')

        for j in range(len(text)):
            if text[j] in fq:
                fq[text[j]]+=1
            else:
                fq[text[j]]=1
        
        for k in f:
            if k in fq:
                div = fq[k] // f[k]
                ans=min(ans,div)
            else:
                return 0
        return ans             

        