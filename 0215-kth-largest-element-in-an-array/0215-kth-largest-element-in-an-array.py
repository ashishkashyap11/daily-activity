# import heapq

# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         minh = []

#         for i in range(len(nums)):
#             heapq.heappush(minh, nums[i])

#             if len(minh) > k:
#                 heapq.heappop(minh)

#         ans = minh[0]
#         return ans

# import heapq

# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         mh = []

#         for i in range(len(nums)):
#             heapq.heappush(mh, -nums[i])

#         for i in range(k - 1):
#             heapq.heappop(mh)

#         ans = -mh[0]
#         return ans

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        
        for i in range(k):
            heapq.heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heapreplace(min_heap, nums[i])

        return min_heap[0]

