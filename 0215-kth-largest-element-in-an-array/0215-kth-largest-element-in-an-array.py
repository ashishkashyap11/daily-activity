import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # k_largest = heapq.nlargest(k, nums)
        # return k_largest[k-1]
        h=[]
        for i in nums:
            heapq.heappush(h, i)
            if len(h)>k:
                heapq.heappop(h)
        return h[0]
        