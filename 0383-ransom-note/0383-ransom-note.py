class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        if len(set(ransomNote))>len(set(magazine)):
            return False
        n=len(ransomNote)
        m=len(magazine)
        f={}
        fq={}
        for i in range(m):
            if magazine[i] in f:
                f[magazine[i]]+=1
            else:
                f[magazine[i]]=1
        for j in range(n):
            if ransomNote[j] in fq:
                fq[ransomNote[j]]+=1
            else:
                fq[ransomNote[j]]=1

            if ransomNote[j] in f and f[ransomNote[j]]>=fq[ransomNote[j]]:
                continue
            else:
                return False
        return True
        