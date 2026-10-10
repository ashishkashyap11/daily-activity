class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f={}
        fq={}
        ans=[]
        f['b']=1
        f['a']=1
        f['l']=2
        f['o']=2
        f['n']=1

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

        