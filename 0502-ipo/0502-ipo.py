import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        minheap = []

        for i in range(len(capital)):
            pair = [capital[i], profits[i]]
            heapq.heappush(minheap, pair)

        res = w
        count = 0
        maxheap = []

        while count < k:

            while minheap and minheap[0][0] <= res:
                pair = heapq.heappop(minheap)
                heapq.heappush(maxheap, -pair[1])

            if not maxheap:
                break

            topp = -heapq.heappop(maxheap)
            res += topp
            count += 1

        return res