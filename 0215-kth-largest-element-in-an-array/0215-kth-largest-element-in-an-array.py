import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k_largest = heapq.nlargest(k, nums)
        return k_largest[k-1]
        