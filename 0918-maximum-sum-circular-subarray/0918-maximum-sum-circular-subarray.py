class Solution(object):
    def maxSubarraySumCircular(self, nums):
        i = 0
        maxend = nums[i]
        maxans = nums[i]
        minend = nums[i]
        minans = nums[i]
        totalsum = sum(nums)

        for i in range(1, len(nums)):
            v1 = maxend + nums[i]
            v2 = nums[i]

            v3 = minend + nums[i]
            v4 = nums[i]

            maxend = max(v1, v2)
            maxans = max(maxans, maxend)

            minend = min(v3, v4)
            minans = min(minans, minend)

        # 1. Handle all-negative edgecase first
        if maxans < 0:
            return maxans

        # 2. Calculate the circular maximum sum once at the end
        kuli = totalsum - minans
        return max(maxans, kuli)
