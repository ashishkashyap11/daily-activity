class Solution(object):
    def removeDuplicates(self, nums):
        off = 0
        cm = 1
        res = 1

        while cm < len(nums):
            if nums[off] == nums[cm]:
                cm += 1

            else:
                nums[off + 1] = nums[cm]
                off += 1
                res += 1
                cm += 1

        return res