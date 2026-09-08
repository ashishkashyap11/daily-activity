class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            sm = -1 * nums[i]

            while l < r:
                s = nums[l] + nums[r]

                if s == sm:
                    result.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < sm:
                    l += 1

                else:
                    r -= 1

        return result