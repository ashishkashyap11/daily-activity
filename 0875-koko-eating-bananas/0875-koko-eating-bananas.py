class Solution: 
    def helper(self, piles: list[int], speed: int) -> int:
        h = 0
        for i in range(0, len(piles)):
            h += piles[i] // speed
            if piles[i] % speed != 0: 
                h += 1
        return h 

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = -1
        while low <= high:
            mid = (low + high) // 2
            hour = self.helper(piles, mid)
            if hour > h:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res
