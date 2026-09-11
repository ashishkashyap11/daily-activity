class Solution(object):
    def totalFruit(self, fruits):
        k=2
        low=0
        high=0
        freq={}
        res=-1

        for high in range(0,len(fruits)):
            if fruits[high] in freq:
                freq[fruits[high]]+=1
            else:
                freq[fruits[high]] = 1
            
            while len(freq)>k:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1

            if len(freq)==k or len(freq)<k:
                length=high-low+1
                res=max(res,length)

        return res
        