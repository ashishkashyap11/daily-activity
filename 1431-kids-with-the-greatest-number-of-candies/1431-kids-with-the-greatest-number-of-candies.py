class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        gr=max(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i]>=gr:
                result.append(True)
            else:
                result.append(False)
        return result
        
            
        
        