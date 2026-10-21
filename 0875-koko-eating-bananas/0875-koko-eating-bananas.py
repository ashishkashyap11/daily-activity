class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            hours = 0

            for i in range(0,len(piles)):
                temp = piles[i] // mid
                hours = hours + temp

                if piles[i] % mid != 0:
                    hours = hours + 1

            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low