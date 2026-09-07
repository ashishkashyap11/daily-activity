class Solution(object):
    def sortedSquares(self, nums):
        a=[]
        b=[]
        sq=[]
        for num in nums:
            if num>0:
                b.append(num)
            else:
                a.append(num)
        if len(a)==0:
            for num in nums:
                sq.append(num**2)
            return sq
        if len(b)==0:
            for num in nums:
                sq.append(num**2)
            sq.reverse()
            return sq
        i=0
        j=0
        res=[0] * len(nums)
        im=0
        for x in range(len(a)):
            a[x] = a[x]**2 
        a.reverse()
        for x in range(len(b)):
            b[x] = b[x]**2
        while(i<len(a) and j<len(b)): 
            if a[i]<=b[j]:
                res[im]=a[i]
                im=im+1
                i=i+1
            else:
                res[im]=b[j]
                im=im+1
                j=j+1
        while(j<len(b)):
                res[im]=b[j]
                im=im+1
                j=j+1
        while(i<len(a)):
                res[im]=a[i]
                im=im+1
                i=i+1
        return res
        

        