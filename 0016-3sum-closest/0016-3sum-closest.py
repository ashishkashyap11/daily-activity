class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        maxdiff = float('inf')
        result=0
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1

            while l<r:
                sm=nums[i]+nums[l]+nums[r]
                diff=abs(sm-target)

                if maxdiff>diff:
                    maxdiff=diff
                    result=sm
 
                if sm == target:
                    return result

                if sm < target:
                    l += 1

                else:
                    r -= 1

        return result
            




        