class Solution(object):
    def findDuplicate(self, nums):
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]

            if slow==fast:
                slow=0
                while fast!=slow:
                    slow=nums[slow]
                    fast=nums[fast]
                return slow
        return 0
                    


        